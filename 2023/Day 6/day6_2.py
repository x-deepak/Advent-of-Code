import re

with open('day6_input.txt') as f:
    data = f.readlines()

time = re.findall('\d+',data[0])
time = ''.join(time)
time = int(time)
print(time)
dist = re.findall('\d+',data[1])
dist = ''.join(dist)
dist = int(dist)
print(dist)

ls = []
flag=False
for k in range(1,time):
    if (k*(time-k)) > dist and flag is False:
        ls.append(k)
        flag=True
    if flag is True and (k*(time-k)) <= dist:
        ls.append(k-1)
        break

print(ls)
print('ways = ', ls[1]-ls[0]+1)

# i noticed that the range starts early and last only a very small part of the full distance
# so i started iterating from start, logged the start of win-range and end of win-range then terminated the loop
