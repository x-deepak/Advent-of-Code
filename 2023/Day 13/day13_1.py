
with open('day13_input.txt') as f:
    segments = f.read().split('\n\n')


def count_rows(i):
    ls_cp = i.copy()
    pop_counter=0
    while len(ls_cp)>=2:
        if len(ls_cp)%2!=0:
            ls_cp.pop(0)
            pop_counter+=1
        l = int(len(ls_cp)/2)
        first = ls_cp[:l]
        second = ls_cp[l:]
        # print('frist= ',first)
        second.reverse()
        # print('sec=',second)
        if first==second:
            return pop_counter+len(first)
        ls_cp.pop(0)
        ls_cp.pop(0)
        pop_counter+=2


    # print('hello')
        

    while len(i)>=2:
        if len(i)%2!=0:
            i.pop(-1)
        l = int(len(i)/2)
        first = i[:l]
        second = i[l:]
        # print('frist= ',first)
        second.reverse()
        # print('sec=',second)
        if first==second:
            return len(first)
        i.pop(-1)
        i.pop(-1)
    return 0
        


def transpose(l1):              #def transpose(l1,l2=[]): --> this error took me 1hr to find
    l2 = []
    for i in range(len(l1[0])):
        # print(i)
        row = ''
        for item in l1[::-1]:

            row+= item[i]
        l2.append(row)
    return l2

# p = transpose(segments[0].split('\n'))

# print(segments[0].split('\n'),'\n',p)



sum = 0

for  pat in segments:
    pattern_list = pat.split('\n')
    rows = count_rows(pattern_list)
    if rows==0:
        pattern_list2 = transpose(pat.split('\n'))
        rows = count_rows(pattern_list2)
        # print(rows)
        sum += rows 
    else:
        # print(rows*100)
        sum += rows*100

    
    
print(sum)
