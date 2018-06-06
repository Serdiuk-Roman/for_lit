# http://behave.readthedocs.io/en/latest/
# http://selenium-python.readthedocs.io/


# import asyncio


# async def slow_operation():
#     await asyncio.sleep(1)
#     return "Future is done"


# def get_result(future):
#     print(future.result())
#     loop.stop()


# loop = asyncio.get_event_loop()
# task = loop.create_task(slow_operation())
# task.add_done_callback(get_result)
# try:
#     loop.run_forever()
# finally:
#     loop.close()


# from datetime import datetime
# import asyncio


# async def slow_runtime(name):
#     await asyncio.sleep(3)
#     print("asy", name, datetime.now())
#     return datetime.now()

# print(datetime.now())
# loop = asyncio.get_event_loop()

# loop.run_until_complete(asyncio.gather(
#     slow_runtime("1"),
#     slow_runtime("2"),
#     slow_runtime("3"),
#     slow_runtime("4"),
#     slow_runtime("5"),
# ))
# loop.close()


# import asyncio

# async def factorial(name, number):
#     f = 1
#     for i in range(2, number+1):
#         print("Task %s: Compute factorial(%s)..." % (name, i))
#         await asyncio.sleep(1)
#         f *= i
#     print("Task %s: factorial(%s) = %s" % (name, number, f))

# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(
#     factorial("A", 2),
#     factorial("B", 3),
#     factorial("C", 4),
# ))
# loop.close()


import asyncio
from random import random


async def rundom_list(number):
    await asyncio.sleep(1)
    number_list = [
        round(random() * 100)
        for i in range(number)
    ]
    print(number_list)
    return number_list


async def sqrt_from_list(number):
    await asyncio.sleep(number)
    number_list = await rundom_list(number)
    res = [x**0.5 for x in number_list]
    print(res)
    return res

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    sqrt_from_list(3),
    sqrt_from_list(5),
    sqrt_from_list(2),
    sqrt_from_list(3),
    sqrt_from_list(4),
))
loop.close()
