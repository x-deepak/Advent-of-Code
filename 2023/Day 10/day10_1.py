import re


with open('day10_input.txt') as f:
    pipes = f.read().split('\n')

for i,j in enumerate(pipes):            #finding S'index
    m = re.search('S',j)
    if m is not None:
        start = [i,m.start(0)]
        break

print(start)

start_list = []            #list_of_possible_start_pipes_from_S
if start[0]-1>=0 and pipes[start[0]-1][start[1]] in ['|','F','7']:
    s = ['|','F','7'].index(pipes[start[0]-1][start[1]])
    up= ['|','F','7'][s]
    up_tuple = (up,[start[0]-1,start[1]])
    start_list.append(up_tuple)
if start[0]+1<len(pipes) and pipes[start[0]+1][start[1]] in ['|','J','L']:
    s = ['|','J','L'].index(pipes[start[0]+1][start[1]])
    down= ['|','J','L'][s]
    down_tuple = (down,[start[0]+1,start[1]])
    start_list.append(down_tuple)
if start[1]-1>=0 and pipes[start[0]][start[1]-1] in ['-','F','L']:
    s = ['-','F','L'].index(pipes[start[0]][start[1]-1])
    left= ['-','F','L'][s]
    left_tuple = (left,[start[0],start[1]-1])
    start_list.append(left_tuple)
if start[1]+1<len(pipes[0]) and pipes[start[0]][start[1]+1] in ['-','7','J']:
    s = ['-','7','J'].index(pipes[start[0]][start[1]+1])
    right= ['-','7','J'][s]
    right_tuple = (right,[start[0],start[1]+1])
    start_list.append(right_tuple)


print(start_list)


# src='S'                   # source pipe.
# crt_pipe = '-'   # '|'
# hst = start               # history index -- to determine which direction it came from.
# crt = [112,19]   #   [113,18]            # current index 
# count = 0

src='S'                   # source pipe.
count_list = []
for crt_pipe,crt in start_list:
    hst = start
    count = 0
    while True:
        count += 1
        i,j = hst[0], hst[1]
        k,p = crt[0], crt[1]
        if crt_pipe=='J':                       # J pipe
            if i==k and k-1>=0:
                crt_pipe=pipes[k-1][p]
                hst=crt
                crt=[k-1,p]
            elif j==p and p-1>=0:
                crt_pipe=pipes[k][p-1]
                hst=crt
                crt=[k,p-1]
            else:
                break
        elif crt_pipe=='F':                       # F pipe
            if i==k and k+1<len(pipes):
                crt_pipe=pipes[k+1][p]
                hst=crt
                crt=[k+1,p]
            elif j==p and p+1<len(pipes[0]):
                crt_pipe=pipes[k][p+1]
                hst=crt
                crt=[k,p+1]
            else:
                break
        elif crt_pipe=='7':                       # 7 pipe
            if i==k and k+1<len(pipes):
                crt_pipe=pipes[k+1][p]
                hst=crt
                crt=[k+1,p]
            elif j==p and p-1>=0:
                crt_pipe=pipes[k][p-1]
                hst=crt
                crt=[k,p-1]
            else:
                break
        elif crt_pipe=='|':                       # | pipe
            if i<k and k+1<len(pipes):
                crt_pipe=pipes[k+1][p]
                hst=crt
                crt=[k+1,p]
            elif i>k and k-1>=0:
                crt_pipe=pipes[k-1][p]
                hst=crt
                crt=[k-1,p]
            else:
                break
        elif crt_pipe=='L':                       # L pipe
            if i==k and k-1>=0:
                crt_pipe=pipes[k-1][p]
                hst=crt
                crt=[k-1,p]
            elif j==p and p+1<len(pipes[0]):
                crt_pipe=pipes[k][p+1]
                hst=crt
                crt=[k,p+1]
            else:
                break
        elif crt_pipe=='-':                       # - pipe
            if j<p and p+1<len(pipes[0]):
                crt_pipe=pipes[k][p+1]
                hst=crt
                crt=[k,p+1]
            elif j>p and p-1>=0:
                crt_pipe=pipes[k][p-1]
                hst=crt
                crt=[k,p-1]
            else:
                break
        else:
            # print('crt pipe :',crt_pipe,'\nloc :',crt,'\ncount :',count)
            if crt_pipe=='S':
                count_list.append(count)
            break


print(count_list)

for i in count_list:
    print(i/2,end=' ')
print()




# print('crt pipe :',crt_pipe,'\nloc :',crt,'\ncount :',count/2)
# print(count/2)



# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.