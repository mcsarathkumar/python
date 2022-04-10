import multiprocessing
from hashlib import sha512
lock = multiprocessing.Lock()

f = open("hash_core.csv", "a")
def findhash(i, j):
    for i in range(i, j + 1):
        lock.acquire()
        f.write(f"{i}\t{sha512(str(i).encode()).hexdigest()}\n")
        lock.release()

if __name__ == "__main__":
    cores = []
    max_cores = 10
    target_val = 10000000
    start = 1
    increment = 0
    step = int(target_val / max_cores)

    for i in range(max_cores):
        increment += step
        core = multiprocessing.Process(target=findhash, args=(start, increment))
        start += step
        cores.append(core)
    for core in cores:
        core.start()
    for core in cores:
        core.join()