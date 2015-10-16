__author__ = 'bida'

count = 0
tmp = 0
for i in range(2012, 1, -1):
    if (i+tmp) % 10 == 1:
        count += 1
    tmp = (i+tmp)/10
print count
print count + str(tmp).count('1')

