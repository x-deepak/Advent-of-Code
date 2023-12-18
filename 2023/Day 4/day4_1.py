import re


# game_id = re.findall(r'[0-9]{1,3}',game_id)

f= open('day4_input.txt','r')

sum = 0
for i in f: 
    split_str = i.strip().split('|')

    nums_i_have = re.findall(r'\d{1,3}',split_str[0][10:])
    winning_nums = re.findall(r'\d{1,3}',split_str[1])
    points = 0
    won_cards=0
    for j in nums_i_have:
        if j in winning_nums:
            won_cards += 1
    if won_cards >= 1:
        points = 1
    for k in range(0,won_cards-1):
        points *= 2
    sum += points

print(sum)
    