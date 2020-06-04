import time
import concurrent.futures


start = time.perf_counter()

def sample(seconds):
    print(f'Sleeping {seconds}...')
    time.sleep(seconds)
    return f'Done in {seconds} seconds'




# run 10 times sample function parallel synchronously
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     seconds = [5, 4, 3, 2, 1]
#     results = [executor.submit(sample, second) for second in seconds]
# 
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())
# 

# run 10 times sample function parallel asynchronously
with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [5, 4, 3, 2, 1]
    results = executor.map(sample, seconds)
    for result in results:
        print(result)



finish = time.perf_counter()

print(f'Finish in {round(finish - start, 2)} seconds')
