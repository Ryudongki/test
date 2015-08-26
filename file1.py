import datetime
import time
import random

now = datetime.datetime.now()
delta = datetime.timedelta(minutes=1)

while True:
    now = now + delta
    file_name = now.strftime("%Y-%m-%d_DATA")
    data_time = now.strftime("%Y-%m-%d %H:%M")
    d1 = random.randrange(0, 9999)
    d2 = random.randrange(0, 9999)
    d3 = random.randrange(0, 9999)
    data = '{0}, {1:4d}, {2:4d}, {3:4d}\n'.format(data_time, d1, d2, d3)

    with open(file_name, 'a') as f:
        f.write(data)
    time.sleep(1 / 1000)
