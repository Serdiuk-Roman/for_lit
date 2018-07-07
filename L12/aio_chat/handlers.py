import json
from aiohttp import web, log
import aiohttp_jinja2
import logging
from datetime import datetime


class LoginView(web.View):
    # Обработчик авторизации

    @aiohttp_jinja2.template('login.html')
    async def get(self):
        # помещаем данные в шаблон с помощью декоратора
        if self.request.cookies.get('user'):
            return web.HTTPFound('/')
        return {'title': 'Authentication'}

    async def post(self):
        # устанавливаем куки
        response = web.HTTPFound('/')
        data = await self.request.post()
        response.set_cookie('user', data['name'])
        return response


async def logout_handler(request):
    # симулируем logout
    response = web.HTTPFound('/')
    response.del_cookie('user')
    return response


@aiohttp_jinja2.template('index.html')
async def index_handler(request):
    title = request.match_info.get('channel', 'main')
    r = request.app['redis']
    cache = await r.lrange('channels:{}'.format(title), 0, -1)
    messages = (json.loads(x) for x in cache) if cache else []
    channels = ('ORANGERY', 'ISOLATOR', 'WHATEVER', 'MILKY WAY', 'COOKIES')
    return {'title': title, 'channels': channels, 'messages': messages}


async def websocket_handler(request):
    # Данный запрос имеет сложную структуру,
    # для визуального упрощения,
    # можно разделить на вложенные функции-корутины.

    current_user = request.cookies['user']

    # получаем значение переменной из url таким вот образом:
    channel = request.match_info.get('channel', 'main')
    # получаем список пользователей на канале
    channel_users = 'channels:{}:users'.format(channel)

    # ключ 'канала', списка с сообщениями, в redis
    channel_key = 'channels:{}'.format(channel)

    # Создаем экземпляр websocket ответа,
    # отключаем автоматическое закрытие ws,
    # причина будет приведена ниже.
    ws = web.WebSocketResponse(autoclose=False)
    await ws.prepare(request)

    # список ожидающих соединений на данном канале
    channel_waiters = request.app['waiters'][channel]
    channel_waiters.append(ws)

    r = request.app['redis']

    try:
        # 1. Открывающее сообщение — рассылаем всем лицам в
        # комнате обновленный список лиц, которые мы берем из redis
        # (у нас множество с приоритетом, для сохранения порядка вывода)

        count = int(await r.zcount(channel_users))

        await r.zadd(channel_users, count + 1, current_user)
        users = await r.zrange(channel_users)
        channel_waiters.broadcast(json.dumps({'user_list': users}))

        # С помощью асинхронного итератора получаем
        # входящие сообщения веб-сокета
        # Подробнее:
        # https://www.python.org/dev/peps/pep-0492/#asynchronous-iterators-and-async-for
        async for msg in ws:
            log.ws_logger.info('MSG: {}'.format(msg))
            # Здесь решаем, что будем делать с сообщениями,
            # полученными от браузера.
            # Некоторый эквивалент on_message WebsocketHandler от tornado.

            if msg.tp == web.MsgType.text:
                # Приводим сообщение в надлежащий вид
                data = json.loads(msg.data)
                data['time'] = datetime.now().strftime('%H:%M:%S %Y-%m-%d')
                data_json = json.dumps(data)

                # Помещаем сообщение в базу данных
                await r.rpush(channel_key, data_json)
                await r.ltrim(channel_key, -25, -1)

                # Рассылаем сообщение целевой аудитории :)
                # Там для каждого ожидающего в комнате
                # вызывается метод send_str
                channel_waiters.broadcast(data_json)

            elif msg.tp == web.MsgType.error:
                logging.error('connection closed with exception {}'
                              .format(ws.exception()))
    finally:
        # 2. В конце концов закрываем соединение
        # и удаляем ws из списка ожидающих
        if ws in channel_waiters:
            # Закрываем соединение и удаляем элемент из списка,
            # если посетитель ушел сам.
            await ws.close()
            log.ws_logger.info('Is WebSocket closed?: {}'.format(ws.closed))
            channel_waiters.remove(ws)

        # удаляем пользователя из множества пользователей
        await r.zrem(channel_users, current_user)
        # рассылаем обновленный список пользователей,
        # всем, кто остался ждать :)
        users = await r.zrange(channel_users)
        channel_waiters.broadcast(json.dumps({'user_list': users}))

    return ws
