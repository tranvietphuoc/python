import threading
import time

start = time.perf_counter()


def sample(seconds):
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    print(f'Run in {seconds}...')


# run 2 functions at the same time - it runs synchronously
# t1 = threading.Thread(target=sample, args=())
# t2 = threading.Thread(target=sample, args=())
# t1.start()
# t2.start()

# t1.join()
# t2.join()

threads = []  # create a list of threads
# run multiple functions at the same time
for _ in range(10):
    t = threading.Thread(target=sample, args=(5,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish = time.perf_counter()

print(f'Finish in {round(finish - start, 2)} second(s)')

