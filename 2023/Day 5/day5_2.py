import re


with open('day5_input.txt') as f:
    layers = f.read().split('\n\n')

intervals = []

for ranges_str in re.findall('(\d+) (\d+)',layers[0]):
    print(ranges_str)
    x1,n = map(int,ranges_str)
    x2=x1+n
    intervals.append((x1,x2,0))

# print(intervals)
print(len(layers))
min_loc = float('inf')
while intervals:
    x1,x2,lvl = intervals.pop()
    if lvl==7:
        min_loc=min(x1,min_loc)
        continue
    for i in re.findall('(\d+) (\d+) (\d+)',layers[lvl+1]):  #convert to the next lvl range
        z1,y1,n = map(int,i)
        diff = z1-y1
        y2 = y1+n
        if x2<=y1 or x1>=y2:   # NO OVERLAP
            continue
        if x1<y1:
            intervals.append((x1,y1,lvl))
            x1=y1
        if x2>y2:
            intervals.append((y2,x2,lvl))
            x2=y2
        intervals.append((x1+diff,x2+diff,lvl+1))            #convert to the next lvl range
        break
    else:
        intervals.append((x1, x2, lvl + 1))


print(min_loc)

