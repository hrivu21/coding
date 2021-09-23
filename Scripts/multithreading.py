import threading
import time
import random

def func(secs):
	print('Start...')
	time.sleep(secs)
	print(f'Done...{secs}')

t1 = time.perf_counter()	

threads = []

for i in range(1,5):
	t = threading.Thread(target=func, args=(random.randint(1,3), ))
	t.start()
	threads.append(t)

for t in threads:
	t.join()

t2 = time.perf_counter()

print(t2-t1)

# import concurrent.futures
# import time

# start = time.perf_counter()


# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)...')
#     time.sleep(seconds)
#     print(f'Done Sleeping...{seconds}')
#     return


# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     results = executor.map(do_something, secs)

#     # for result in results:
#     #     print(result)

# # threads = []

# # for _ in range(10):
# #     t = threading.Thread(target=do_something, args=[1.5])
# #     t.start()
# #     threads.append(t)

# # for thread in threads:
# #     thread.join()

# finish = time.perf_counter()
# # for r in results:
# # 	print(r)

# print(f'Finished in {round(finish-start, 2)} second(s)')