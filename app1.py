import sys
import time
import random
from threading import Thread
from multiprocessing import Process


FIB_NUM_MIN = 100_000
FIB_NUM_MAX = 200_000
INSTANCE_COUNT = 10
COMP_AMT = 10


def f_x(num):
    sys.set_int_max_str_digits(999999)

    a, b = 0, 1
    if num == 1:
        return a

    for _ in range(num - 2):
        a, b = b, a + b

    return b


def thread_parallel():
    for i in range(COMP_AMT):
        p = [
            Thread(target=f_x, args=(random.randint(FIB_NUM_MIN, FIB_NUM_MAX), ))
            for _ in range(INSTANCE_COUNT)
        ]

        t = time.time()

        for _p in p:
            _p.start()
        for _p in p:
            _p.join()

        t = time.time() - t

        print(f"{i + 1}) |||THREAD|||\tComputed {INSTANCE_COUNT} fib numbers in {t} sec")


def process_parallel():
    for i in range(COMP_AMT):
        p = [
            Process(target=f_x, args=(random.randint(FIB_NUM_MIN, FIB_NUM_MAX), ))
            for _ in range(INSTANCE_COUNT)
        ]

        t = time.time()

        for _p in p:
            _p.start()
        for _p in p:
            _p.join()

        t = time.time() - t

        print(f"{i + 1}) |||PROCESS|||\tComputed {INSTANCE_COUNT} fib numbers in {t} sec")


def sync():
    for i in range(COMP_AMT):
        t = time.time()

        for _ in range(INSTANCE_COUNT):
            f_x(random.randint(FIB_NUM_MIN, FIB_NUM_MAX))

        t = time.time() - t

        print(f"{i + 1}) |||SYNC|||\tComputed {INSTANCE_COUNT} fib numbers in {t} sec")


if __name__ == "__main__":
    random.seed(0)
    print(
        "Computing 10 Fibonacci numbers from "
        f"{FIB_NUM_MIN} to {FIB_NUM_MAX} {COMP_AMT} times"
    )

    # sync()
    # thread_parallel()
    process_parallel()
    print("---------")
