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
pipe_set = []          # Assumming all chars in start_list reach S
for crt_pipe,crt in start_list:
    hst = start
    count = 0
    while True:
        pipe_set.append(tuple(crt))
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
    break


print(count_list)

for i in count_list:
    print('farthest cell: ',i/2,end=' ')
print()


print(len(pipe_set))

print(tuple(start) in pipe_set)



with open('day10_input2.txt','w') as ff:
    for index,j in enumerate(pipes):
        for index2,i in enumerate(j):
            if (index,index2) in pipe_set:
                ff.write(i)
            else:
                ff.write('.')
        ff.write('\n')


with open('day10_input2.txt','r') as cc:
    pipes2 = cc.read().split('\n')


cell = 0
for ind,i in enumerate(pipes2):
    flag=False
    for ind2,j in enumerate(i):
        # print(j)
        if j=='.' and flag==True:
            cell+=1
            print('index :',ind,ind2,'char :',j)
        if j in ['|','L','J'] and flag==False:
            flag=True
        elif j in ['|','L','J'] and flag==True:
            flag=False


print(cell)

