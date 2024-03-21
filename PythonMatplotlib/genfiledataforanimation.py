import time
import random

LIMIT_TIME = 10  # s
DATA_FILENAME = "data.txt"


def gen_data(filename, limit_time):
    start_time = time.time()
    elapsed_time = time.time() - start_time
    with open(filename, "w") as f:
        while elapsed_time < limit_time:
            f.write(f"{time.time():10.10f} {random.random():30.10f}\n")  # produces 64 bytes
            f.flush()
            elapsed = time.time() - start_time
            print(elapsed_time)


gen_data(DATA_FILENAME, LIMIT_TIME)