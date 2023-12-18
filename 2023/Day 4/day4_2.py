import re


# game_id = re.findall(r'[0-9]{1,3}',game_id)

f= open('day4_input.txt','r')

line_list = f.readlines()


def match_count(i):

    split_str = line_list[i-1].split('|')
    nums_i_have = re.findall(r'\d{1,3}',split_str[0][8:])
    winning_nums = re.findall(r'\d{1,3}',split_str[1])
    match=0
    for j in nums_i_have:
        if j in winning_nums:
            match +=1
    return match
# print(match_count(1))


def cards_won(i):
    global card_count
    card_count+=1
    won_cards=match_count(i)
    for j in range(1,won_cards+1):
        cards_won(i+j)
    return card_count


cards=0
for i in range(1,213+1):
    card_count=0
    c = cards_won(i)

    # print(c,match_count(i))
    cards += c

print(cards)

