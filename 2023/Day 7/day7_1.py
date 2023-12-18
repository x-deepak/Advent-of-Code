import re



with open('day7_input.txt') as f:
    input = f.read()

card_types = [[],[],[],[],[],[],[]]

#card type finder -- >
for i,j in re.findall('(\d*\w*) (\d+)',input):
    card_bid = [i,j]
    c = re.findall(r'(?:([\w\d])(?=.*\1))',i)
    length = len(c)
    if length == 4:
        card_types[6].append(card_bid)
    elif length == 3:
        if c[0]==c[1] and c[2]==c[1]:
            card_types[5].append(card_bid)
        else:
            card_types[4].append(card_bid)
    elif length==2:
        if c[0]==c[1]:
            card_types[3].append(card_bid)
        else:
            card_types[2].append(card_bid)
    elif length==1:
        card_types[1].append(card_bid)
    else:
        card_types[0].append(card_bid)


power_dict = { 'A':'C', 'K':'B', 'Q':'A', 'J':'9', 'T':'8', '9':'7', '8':'6', '7':'5', '6':'4', '5':'3', '4':'2', '3':'1', '2':'0'}
def power(card):
    return power_dict[card]


# card = '88223'
# card = list(map(power,card))
# card  = ''.join(card)
# card = int(card, 16)

# print(card_types)

for i in card_types:
    for k in range(len(i)-1):
        n = 0
        while n+1<len(i):
            card1 = list(map(power,i[n][0]))
            card1  = ''.join(card1)
            card1 = int(card1, 16)
            card2 = list(map(power,i[n+1][0]))
            card2  = ''.join(card2)
            card2 = int(card2, 16)
            if card1>card2:
                i[n],i[n+1] = i[n+1],i[n]
            n+=1

pwr = 1
sum = 0
for i in card_types:
    for j in i:
        sum += int(j[1])*pwr
        pwr +=1

print(sum)