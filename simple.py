from hashlib import sha512

start = 1
target_val = 100000000

f = open("hash1.csv", "a")
for i in range(start, target_val + 1):
    f.write(f"{i}\t{sha512(str(i).encode()).hexdigest()}\n")
f.close()
