import re
import numpy as np

with open('day11_input.txt','r+') as f:
    data= f.read()
    f.seek(0)
    new_lines = 0
    numbers = 1
    
    for ind,i in enumerate(data):

        # print(i,ind)
        if i=='#':
            f.seek(ind+new_lines)
            f.write('7')
            numbers +=1 
        if i=='.':
            f.seek(ind+new_lines)
            f.write('0')
            # numbers +=1 
        if i==r'\n':
            new_lines+=1




with open('day11_input.txt','r') as d:
    space = d.read().split('\n')


for ind,i in enumerate(space):
    ls = []
    for ind2,j in enumerate(i):
        ls.append(int(j))
    space[ind]=ls


# print(space[-1])


copy_arr = np.array(space)
h = len(copy_arr)
v = len(copy_arr[0])

arr_row = np.ones((h),dtype='i')

c=0
rows = []
while True:
    if set(copy_arr[c]) == set([0])  :
        rows.append(c)
        # copy_arr[c]= arr_row
    c+=1
    if c>=len(copy_arr):
        break


copy_arr = copy_arr.transpose()


v = len(copy_arr)

arr_col = np.ones((v),dtype='i')

c=0
cols = []
while True:
    if set(copy_arr[c]) == set([0]) :
        cols.append(c)
        # copy_arr[c]= arr_col
    c+=1
    if c>=len(copy_arr):
        break


print(rows)
print(cols)


copy_arr = copy_arr.transpose()








# print(copy_arr)

a = np.where(copy_arr==7)

# print(a)

num_indexes = []             #  no. of unique pairs ==  (n(n-1))/2 ;       n = no. of elements

for i,j in zip(a[0],a[1]):
    num_indexes.append((i,j))

# print(len(num_indexes))
# print(num_indexes)


sum = 0
while len(num_indexes)>=1:
    lenght = len(num_indexes)
    i = 1
    while i<lenght:
        #find dist b/w num_indexes[0] and num_indexes[i]
        row_count = 0
        col_count = 0
        for k in rows:
            if (k>num_indexes[0][0] and k<num_indexes[i][0]) or (k<num_indexes[0][0] and k>num_indexes[i][0]):
                row_count+=1
        for p in cols:
            if (p>num_indexes[0][1] and p<num_indexes[i][1]) or (p<num_indexes[0][1] and p>num_indexes[i][1]):
                col_count+=1
        
        vert = (abs(num_indexes[0][0]-num_indexes[i][0])-row_count) + row_count*1000000
        hor =  (abs(num_indexes[0][1]-num_indexes[i][1])-col_count) + col_count*1000000
        dist = vert + hor
        # print('Stars =',num_indexes[0],num_indexes[i],'Dist =',dist)

        sum += dist
        i+=1
    num_indexes.pop(0)

print(num_indexes)
print(sum)
