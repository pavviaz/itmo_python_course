import time
import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


A, B = 0, math.pi / 2
N_ITER = 1_0_000_000
THREAD_COUNT = 12
EQUATION = math.cos


def compute_threads_work(length, download_threads):
    div, mod = divmod(length, download_threads)
    for _ in range(download_threads):
        yield (t := length - (div + bool(mod)), length)
        length = t
        mod -= 1 if mod else 0


def f_x(*args):
    a, h, f, to = args[0]

    acc = 0
    for i in range(f, to):
        acc += EQUATION(a + i * h) * h

    return acc


def thread_parallel(a, b, n, thrd_cnt):
    h = (b - a) / n
    timer_start = time.time()

    s = 0
    with ThreadPoolExecutor(max_workers=thrd_cnt) as pool:
        res = pool.map(f_x, [(a, h) + i for i in compute_threads_work(n, thrd_cnt)])
        for r in res:
            s += r

    timer_end = time.time()

    print(f"|||THREAD|||\ts = {s} in {timer_end - timer_start:0.4f} secs ")


def process_parallel(a, b, n, thrd_cnt):
    h = (b - a) / n
    timer_start = time.time()

    s = 0
    with ProcessPoolExecutor(max_workers=thrd_cnt) as pool:
        res = pool.map(f_x, [(a, h) + i for i in compute_threads_work(n, thrd_cnt)])
        for r in res:
            s += r

    timer_end = time.time()

    print(f"|||PROCESS|||\ts = {s} in {timer_end - timer_start:0.4f} secs ")


if __name__ == "__main__":
    for p in range(1, THREAD_COUNT * 2 + 1):
        print(f"NUM OF INSTANCES: {p}")
        thread_parallel(A, B, N_ITER, p)
        process_parallel(A, B, N_ITER, p)
        print("---------")
