import random
import time

s = set()

def gen_numbers():
    num = list(range(1,46))
    random.shuffle(num)
    return num[0:6]

while True:
    print(gen_numbers())
    time.sleep(1)
