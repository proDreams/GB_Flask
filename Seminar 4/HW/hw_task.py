from multiprocessing import freeze_support
from random import randint
import hw_task_async as aio
import hw_task_multiproc as mp
import hw_task_threads as th

if __name__ == "__main__":
    lst = [randint(1, 100) for _ in range(1_000_000)]
    sep_list = [lst[i:i + 100_000] for i in range(0, 1_000_000, 100_000)]

    th_result = th.task(sep_list)
    mp_result = mp.task(sep_list)
    aio_task = aio.task(sep_list)

    print(f"""Сумма элементов массива: {sum(lst)}
    
Результат многопоточного расчёта: {th_result[0]}
Затрачено времени: {th_result[1]:.4f}
    
Результат многопроцессорного расчёта: {mp_result[0]}
Затрачено времени: {mp_result[1]:.4f}
    
Результат асинхронного расчёта: {aio_task[0]}
Затрачено времени: {aio_task[1]:.4f}
""")