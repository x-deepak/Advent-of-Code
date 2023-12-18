
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

start = 'AAA'
steps = 0
i=0
while True:
    if start=='ZZZ':
        break
    elif segments[0][i]=='L':
        start = nodes[start][0]
    elif segments[0][i]=='R':
        start = nodes[start][1]
    steps+=1
    i+=1
    if i==len(segments[0]):
              i=0

print(steps)  #low