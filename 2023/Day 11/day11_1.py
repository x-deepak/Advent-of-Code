
import numpy as np

with open('day11_input.txt','r+') as f:
    data= f.read()
    f.seek(0)
    new_lines = 0
    numbers = 1
    
    for ind,i in enumerate(data):

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



copy_arr = np.array(space)

c=0
while True:
    i = copy_arr[c]
    if set(i) == { 0 }  :
        copy_arr= np.insert(copy_arr,c,i,axis=0)
        c+=1
    c+=1
    if c>=len(copy_arr):
        break



copy_arr = copy_arr.transpose()

c=0
while True:
    i = copy_arr[c]
    if set(i) == { 0 }  :
        copy_arr= np.insert(copy_arr,c,i,axis=0)
        c+=1
    c+=1
    if c>=len(copy_arr):
        break


copy_arr = copy_arr.transpose()



a = np.where(copy_arr==7)



num_indexes = []             #  no. of unique pairs ==  (n(n-1))/2 ;       n = no. of elements

for i,j in zip(a[0],a[1]):
    num_indexes.append((i,j))

# print(num_indexes)



sum = 0
while len(num_indexes)>=1:
    lenght = len(num_indexes)
    i = 1
    while i<lenght:
        #find dist b/w num_indexes[0] and num_indexes[i]
        dist = abs(num_indexes[0][0]-num_indexes[i][0]) + abs(num_indexes[0][1]-num_indexes[i][1])
        sum += dist
        i+=1
    num_indexes.pop(0)

print(num_indexes)
print(sum)
