import re


with open('day10_input.txt') as f:
    pipes = f.read().split('\n')

for i,j in enumerate(pipes):            #finding S'index
    m = re.search('S',j)
    if m is not None:
        start = [i,m.start(0)]
        break

print(start)

src='S'                   # source pipe.
crt_pipe = '-'   # '|'
hst = start               # history index -- to determine which direction it came from.
crt = [112,19]   #   [113,18]            # current index 
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
        break

print('crt pipe :',crt_pipe,'\nloc :',crt,'\ncount :',count/2)
print(count/2)



# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.