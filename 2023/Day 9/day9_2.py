import re

with open('day9_input.txt') as f:
    values = f.read().split('\n')


for i,j in enumerate(values):
    line = re.findall('\-{0,1}\d+',j)       # ----------> missed to capture - minus sign for nums. then spend 2 hr finding error in code.
    line = list(map(int,line))
    values[i] = line

def diff(seq):
    for i,v in enumerate(seq):
        if i+1==len(seq):
            break
        seq[i]=seq[i+1]-seq[i]
    seq.pop(-1)
    if len(seq)==0:
        seq.append(0)
    # print(seq)
    return seq

# print(diff([3,-3]))
# print(-3-3)

def org_value(value_list):
    v = [value_list[0]]
    while set(value_list)!={0}:
        value_list = diff(value_list)

        # print(value_list)
        v.append(value_list[0])
    # print(v)
    i = len(v)-1
    while i>0:
        v[i-1] = v[i-1] - v[i]
        v.pop(i)
        i -= 1
    return v[0]



total = 0
for i in values:
    total += org_value(i)


print(total)