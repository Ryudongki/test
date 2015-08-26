import glob

l = glob.glob('/home/user/PycharmProjects/practice/*_DATA')
l.sort()

for x in range(0, len(l)):
    s = ''
    with open(l[x], 'r') as f:
        s = f.read()

    with open('DATA', 'a') as f:
        f.write(s)