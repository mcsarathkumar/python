import threading
from hashlib import sha512
lock = threading.Lock()

f = open("hash_thread.csv", "a")
def findhash(i, j):
    for i in range(i, j + 1):
        lock.acquire()
        f.write(f"{i}\t{sha512(str(i).encode()).hexdigest()}\n")
        lock.release()

if __name__ == "__main__":
    threads = []
    max_threads = 10
    target_val = 10000000
    start = 1
    increment = 0
    step = int(target_val / max_threads)

    for i in range(max_threads):
        increment += step
        thread = threading.Thread(target=findhash, args=(start, increment))
        start += step
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()