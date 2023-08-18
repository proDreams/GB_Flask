import threading
import time

res = 0


def sum_list(lst):
    global res
    for i in lst:
        res += i


def task(lst):
    threads = []
    start_time = time.time()

    sep_list = [lst[i:i + 100_000] for i in range(0, 1_000_000, 100_000)]

    for sep in sep_list:
        thread = threading.Thread(target=sum_list, args=[sep])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return res, time.time() - start_time
