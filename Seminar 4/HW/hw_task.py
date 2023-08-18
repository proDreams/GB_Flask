from multiprocessing import freeze_support
from random import randint
import hw_task_async as aio
import hw_task_multiproc as mp
import hw_task_threads as th

if __name__ == "__main__":
    lst = [randint(1, 100) for _ in range(1_000_000)]

    th_result = th.task(lst)
    mp_result = mp.task(lst)
    aio_task = aio.task(lst)

    print(f"""Сумма элементов массива: {sum(lst)}
    
Результат многопоточного расчёта: {th_result[0]}
Затрачено времени: {th_result[1]:.4f}
    
Результат многопроцессорного расчёта: {mp_result[0]}
Затрачено времени: {mp_result[1]:.4f}
    
Результат асинхронного расчёта: {aio_task[0]}
Затрачено времени: {aio_task[1]:.4f}
""")