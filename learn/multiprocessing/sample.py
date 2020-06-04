import time
import multiprocessing


start = time.perf_counter()

def sample(seconds):
    print(f'Sleeping in {seconds}...')
    time.sleep(seconds)
    print(f'Done in {seconds}...')


# example with 2 process
# p1 = multiprocessing.Process(target=sample, args=(1,))
# p2 = multiprocessing.Process(target=sample, args=(1,))
# p1.start()
# p2.start()
# p1.join()
# p2.join()


# run 10 process
processes = []
for _ in range(10):
    p = multiprocessing.Process(target=sample, args=(1,))
    p.start()
    processes.append(p)

for process in processes:
    process.join()

finish = time.perf_counter()

print(f'Finish in {round(finish - start, 2)} seconds')

