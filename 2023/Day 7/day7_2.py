import re



with open('day7_input.txt') as f:
    input = f.read()

card_types = [[],[],[],[],[],[],[]]

#card type finder -- >
for i,j in re.findall('(\d*\w*) (\d+)',input):
    card_bid = [i,j]
    c = re.findall(r'(?:([\w\d])(?=.*\1))',i)    # finds duplicates ;  AAAAA= 4 duplicates
    length = len(c)
    joker=  re.findall(r'[J]',i)
    joker_len = len(joker)
    if length == 4:        # AAAAA
        card_types[6].append(card_bid)
    elif length == 3:        # AAAA1
        if joker_len==0:
            if c[0]==c[1] and c[2]==c[1]:
                card_types[5].append(card_bid)
            else:
                card_types[4].append(card_bid)
        else:
            if joker_len>0:
                card_types[6].append(card_bid)
    elif length==2:
        if joker_len==0:
            if c[0]==c[1]:
                card_types[3].append(card_bid)
            else:
                card_types[2].append(card_bid)
        else:
            if joker_len==1 and c[0]==c[1]:
                card_types[5].append(card_bid)
            elif joker_len==1 and c[0]!=c[1]:
                card_types[4].append(card_bid)
            # elif joker_len==2 or joker_len==3:
            else:
                card_types[5].append(card_bid)
    elif length==1:
        if joker_len==0:        
            card_types[1].append(card_bid)
        else:
            card_types[3].append(card_bid)
    else:
        if joker_len==0:
            card_types[0].append(card_bid)
        else:
            card_types[1].append(card_bid)


power_dict = { 'A':'C', 'K':'B', 'Q':'A','T':'9', '9':'8', '8':'7', '7':'6', '6':'5', '5':'4', '4':'3', '3':'2', '2':'1','J':'0'}
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