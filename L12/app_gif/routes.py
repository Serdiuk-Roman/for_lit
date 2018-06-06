from views import index, ws


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/ws', ws)
