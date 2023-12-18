
import re


with open('day8_input.txt') as f:
    segments = f.read().split('\n\n')

# print(segments[1])
nodes = {}
# print(re.findall(r'(\w+) = \((\w+), (\w+)\)',segments[1]))


for i,j,k in re.findall(r'(\w+) = \((\w+), (\w+)\)',segments[1]):
    nodes[i] = [j,k]

# print(segments[1][0])
# print(nodes)
start_list = []
for i in nodes.keys():
    if i.endswith('A'):
        start_list.append([i,0])

# print(start_list)
# start = 'XDA'

steps = [0,0,0,0,0,0]  # steps = [0,0]
while True:
    k= steps.index(min(steps))
    while True:

        if start_list[k][1]==len(segments[0]):
            start_list[k][1]=0
        i = start_list[k][1]
        if segments[0][i]=='L':
            start_list[k][0] = nodes[start_list[k][0]][0]
        elif segments[0][i]=='R':
            start_list[k][0] = nodes[start_list[k][0]][1]
        steps[k]+=1
        start_list[k][1]+=1
        if start_list[k][0][2]=='Z':
            break
    # print(start_list)
    # print(steps,start_list)
    if len(set(steps))==1:
        break

print(steps[0])  #low  

# [21409, 0, 0, 0, 0, 0]
# [21409, 14363, 0, 0, 0, 0]
# [21409, 14363, 15989, 0, 0, 0]
# [21409, 14363, 15989, 16531, 0, 0]
# [21409, 14363, 15989, 16531, 19241, 0]
# [21409, 14363, 15989, 16531, 19241, 19783]
# [21409, 28726, 15989, 16531, 19241, 19783]
# [21409, 28726, 31978, 16531, 19241, 19783]
# [21409, 28726, 31978, 33062, 19241, 19783]
# [21409, 28726, 31978, 33062, 38482, 19783]
# [21409, 28726, 31978, 33062, 38482, 39566]
# [42818, 28726, 31978, 33062, 38482, 39566]
# [42818, 43089, 31978, 33062, 38482, 39566]
# [42818, 43089, 47967, 33062, 38482, 39566]
# [42818, 43089, 47967, 49593, 38482, 39566]
# [42818, 43089, 47967, 49593, 57723, 39566]

