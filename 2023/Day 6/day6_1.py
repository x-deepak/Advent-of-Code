import re

with open('day6_input.txt') as f:
    data = f.readlines()

time = re.findall('\d+',data[0])
time = list(map(int,time))

dist = re.findall('\d+',data[1])
dist = list(map(int,dist))


ls = 1
for i,j in zip(time,dist):
    count=0
    for k in range(1,i):

        if (k*(i-k)) > j:
            count+=1
    ls *= count

print(ls)


