import re

f= open('day3_input.txt','r')

lines = f.readlines()
# line_count = len(lines)
# print(lines)

# print(lines[0].strip())
sum = 0
for i in range(0,140):
    # if i==3:
        # break
    # ind = [(m.start(0), m.end(0)) for m in re.finditer(r'[0-9]{1,4}',lines[i].strip())]
    # print(ind,len(ind))
    for m in re.finditer(r'[0-9]{1,4}',lines[i].strip()) : 
        # to check sym. above num
        # start = m.start(0)
        # end = m.end(0)
        if i-1>=0:
            if m.start(0) == 0:
                top = re.search(r'[^.\d]', lines[i-1][m.start(0):m.end(0)+1])
            elif m.end(0) == 140:
                top = re.search(r'[^.\d]', lines[i-1][m.start(0)-1:m.end(0)])
            else:
                top = re.search(r'[^.\d]', lines[i-1][m.start(0)-1:m.end(0)+1])
            if top is not None:
                part_num = lines[i][m.start(0):m.end(0)]
                # print(part_num , 'top')
                sum += int(part_num)
                continue
        # to check sym. below num
        if i+1<len(lines):
            if m.start(0) == 0:
                bot = re.search(r'[^.\d]', lines[i+1][m.start(0):m.end(0)+1])
            elif m.end(0) == 140:
                bot = re.search(r'[^.\d]', lines[i+1][m.start(0)-1:m.end(0)])
            else:
                bot = re.search(r'[^.\d]', lines[i+1][m.start(0)-1:m.end(0)+1])
            if bot is not None:
                part_num = lines[i][m.start(0):m.end(0)]
                # print(part_num, 'bot')
                sum += int(part_num)
                continue   
        # to check sym. beside num
        if m.start(0) == 0:
                mid =  re.search(r'[^.\d]', lines[i][m.start(0):m.end(0)+1])
        elif m.end(0) == 140:
                mid =  re.search(r'[^.\d]', lines[i][m.start(0)-1:m.end(0)])
        else:
                mid =  re.search(r'[^.\d]', lines[i][m.start(0)-1:m.end(0)+1])               
        if mid is not None:
            part_num = lines[i][m.start(0):m.end(0)]
            # print(part_num, 'mid')
            sum += int(part_num)
            continue


print(sum)
    # print(lines[i].strip())
    # print(ind)


# ind = [(m.start(0), m.end(0)) for m in re.finditer(r'[0-9]{1,4}',j)]

# mid_checker = [(m.start(0), m.end(0)) for m in re.finditer(r'[^.\d]{1}[\d]{1,4}|[\d]{1,4}[^.\d]{1}',j)]     

