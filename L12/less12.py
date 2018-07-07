# import multiprocessing


# def foo(num):
#     print("worker", num**1024)


# if __name__ == '__main__':
#     process = []
#     for i in range(100):
#         process.append(multiprocessing.Process(foo(i)))

#     for pr in process:
#         pr.start()

# очеред, росшареная памьять

# def lazy_range(up_to):
#     index = 0
#     while index < up_to:
#         yield index
#         index += 1


# gen = lazy_range(10)
# print(next(gen))
# gen.__next__()
# print(next(gen))


# import asyncio


# async def foo_bar(number, n):
#     while n > 0:
#         print('{} minus {}'.format(n, number))
#         await asyncio.sleep(1)
#         n -= number

# loop = asyncio.get_event_loop()
# tasks = [
#     asyncio.ensure_future(foo_bar(1, 12)),
#     asyncio.ensure_future(foo_bar(2, 15))
# ]
# loop.run_until_complete(asyncio.wait(tasks))

# soccet
