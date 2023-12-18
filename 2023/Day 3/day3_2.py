import re

f= open('day3_input.txt','r')

lines = f.readlines()
# line_count = len(lines)
# print(lines)

flag = False
sum = 0
for i in range(0,140):
    # if i==3:
        # break
        # to check sym. beside num
            
    for m in re.finditer(r'[\d]{1,3}[\*]{1}[\d]{1,3}',lines[i].strip()):
        two_num_list = lines[i][m.start(0):m.end(0)].split('*')
        # print(two_num_list, 'middlle')
        gear_ratio = int(two_num_list[0]) * int(two_num_list[1])
        sum += gear_ratio
        # print(gear_ratio, 'mid')

    for m in re.finditer(r'[\*]',lines[i].strip()) :
        top_flag = False
        mid_flag = False
        bot_flag = False     
        if i-1>=0:

            top = [(m.start(0), m.end(0)) for m in re.finditer(r'[\d]{1,4}',lines[i-1][m.start(0)-1:m.end(0)+1])]
            # print(top , 'top')
            if len(top) ==2:
                top_whole = [(m.start(0), m.end(0)) for m in re.finditer(r'[\d]{1,4}',lines[i-1][m.start(0)-3:m.end(0)+3])]
                # print(top_whole, 'top_whole')
                part_num1 = lines[i-1][m.start(0)-3:m.end(0)+3][top_whole[0][0]:top_whole[0][1]]
                part_num2 = lines[i-1][m.start(0)-3:m.end(0)+3][top_whole[1][0]:top_whole[1][1]]
                # print(part_num1,part_num2, 'top_whole')
                gear_ratio = int(part_num1) * int(part_num2)
                sum += gear_ratio
                continue
            if len(top)==1:
                # left num
                if top[0]==(0,1) or top[0]==(0,2):
                    top_left = [(m.start(0), m.end(0)) for m in re.finditer(r'[\d]{1,4}',lines[i-1][m.start(0)-3:m.end(0)])]
                    # print(top_left, 'top_left')
                    part_num = lines[i-1][m.start(0)-3:m.end(0)][top_left[-1][0]:top_left[-1][1]]
                    # print(part_num, 'top_left')
                # right num
                elif top[0]==(2,3) or top[0]==(1,3):
                    top_right = [(m.start(0), m.end(0)) for m in re.finditer(r'[\d]{1,4}',lines[i-1][m.start(0):m.end(0)+3])]
                    # print(top_right, 'top_right')
                    part_num = lines[i-1][m.start(0):m.end(0)+3][top_right[0][0]:top_right[0][1]]
                    # print(part_num, 'top_right')
                elif top[0]==(0,3):
                    top_mid = [(m.start(0), m.end(0)) for m in re.finditer(r'[\d]{1,4}',lines[i-1][m.start(0)-1:m.end(0)+1])]
                    # print(top_mid,'top_mid')
                    part_num = lines[i-1][m.start(0)-1:m.end(0)+1][top_mid[0][0]:top_mid[0][1]]
                    # print(part_num, 'top_mid')
                a = int(part_num)
                top_flag=True

        # mid -->        N*.  and .*N
        if True:
            top = [(m.start(0), m.end(0)) for m in re.finditer(r'[\d]{1,4}',lines[i][m.start(0)-1:m.end(0)+1])]
            if len(top)==1:
                # print(top, 'mid', lines[i][m.start(0)-1:m.end(0)+1][top[0][0]:top[0][1]])
                #left -->  N*.
                if top[0]==(0,1):
                    left = [(m.start(0), m.end(0)) for m in re.finditer(r'[\d]{1,4}',lines[i][m.start(0)-3:m.end(0)])]
                    # print(top_mid,'top_mid')
                    part_num = lines[i][m.start(0)-3:m.end(0)][left[0][0]:left[0][1]]
                    print(part_num, 'mid left')
                #right -->  .*N
                if top[0]==(2,3):
                    right = [(m.start(0), m.end(0)) for m in re.finditer(r'[\d]{1,4}',lines[i][m.start(0):m.end(0)+3])]
                    # print(top_mid,'top_mid')
                    part_num = lines[i][m.start(0):m.end(0)+3][right[0][0]:right[0][1]]
                    print(part_num, 'mid right')
                b = int(part_num)
                mid_flag=True

        if i+1<len(lines):

            top = [(m.start(0), m.end(0)) for m in re.finditer(r'[\d]{1,4}',lines[i+1][m.start(0)-1:m.end(0)+1])]
            # print(top , 'top')
            if len(top) ==2:
                top_whole = [(m.start(0), m.end(0)) for m in re.finditer(r'[\d]{1,4}',lines[i+1][m.start(0)-3:m.end(0)+3])]
                # print(top_whole, 'bot_whole')
                part_num1 = lines[i+1][m.start(0)-3:m.end(0)+3][top_whole[0][0]:top_whole[0][1]]
                part_num2 = lines[i+1][m.start(0)-3:m.end(0)+3][top_whole[1][0]:top_whole[1][1]]
                # print(part_num1,part_num2, 'bot_whole')
                gear_ratio = int(part_num1) * int(part_num2)
                sum += gear_ratio
                continue
            if len(top)==1:
                # left num
                if top[0]==(0,1) or top[0]==(0,2):
                    top_left = [(m.start(0), m.end(0)) for m in re.finditer(r'[\d]{1,4}',lines[i+1][m.start(0)-3:m.end(0)])]
                    # print(top_left, 'bot_left')
                    part_num = lines[i+1][m.start(0)-3:m.end(0)][top_left[-1][0]:top_left[-1][1]]
                    # print(part_num, 'bot_left')
                # right num
                elif top[0]==(2,3) or top[0]==(1,3):
                    top_right = [(m.start(0), m.end(0)) for m in re.finditer(r'[\d]{1,4}',lines[i+1][m.start(0):m.end(0)+3])]
                    # print(top_right, 'bot_right')
                    part_num = lines[i+1][m.start(0):m.end(0)+3][top_right[0][0]:top_right[0][1]]
                    # print(part_num, 'bot_right')
                elif top[0]==(0,3):
                    top_mid = [(m.start(0), m.end(0)) for m in re.finditer(r'[\d]{1,4}',lines[i+1][m.start(0)-1:m.end(0)+1])]
                    # print(top_mid,'bot_mid')
                    part_num = lines[i+1][m.start(0)-1:m.end(0)+1][top_mid[0][0]:top_mid[0][1]]
                    # print(part_num, 'bot_mid')
                c = int(part_num)
                bot_flag=True
        
        if top_flag==True and mid_flag==True:
            sum += a*b
        elif top_flag==True and bot_flag==True:
            sum += a*c
        elif bot_flag==True and mid_flag==True:
            sum += b*c
        


print(sum)


