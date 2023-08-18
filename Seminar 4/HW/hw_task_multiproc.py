from multiprocessing import Pool
import time


def sum_list(lst):
    res = 0
    for i in lst:
        res += i

    return res


def task(lst):

    start_time = time.time()

    sep_list = [lst[i:i + 100_000] for i in range(0, 1_000_000, 100_000)]

    pool = Pool(processes=10)
    result = pool.map(sum_list, sep_list)

    return sum(result), time.time() - start_time
