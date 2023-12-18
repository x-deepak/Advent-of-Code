import re


# str =  "eightseventhree7lfqpnclxnnineninemgkjtqksrdone"

# pattern = "one|two|three|four|five|six|seven|eight|nine|zero|oneight|threeight|fiveight|nineight|twone|zerone|sevenine|eightwo|eighthree|[0-9]+"

# matches = re.findall(pattern, str) 
 
# print(matches) 
pattern ="one|two|three|four|five|six|seven|eight|nine|zero|[0-9]"
pattern_rev="orez|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno|[0-9]"


def strtodigit(n):
    if n=='one':
        return '1'
    if n=='two':
        return '2'
    if n=='three':
        return '3'
    if n=='four':
        return '4'
    if n=='five':
        return '5'
    if n=='six':
        return '6'
    if n=='seven':
        return '7'
    if n=='eight':
        return '8'
    if n=='nine':
        return '9'
    if n=='zero':
        return '0'
    else:
        return n

def strtodigitrev(n):
    n=n[::-1]
    if n=='one':
        return '1'
    if n=='two':
        return '2'
    if n=='three':
        return '3'
    if n=='four':
        return '4'
    if n=='five':
        return '5'
    if n=='six':
        return '6'
    if n=='seven':
        return '7'
    if n=='eight':
        return '8'
    if n=='nine':
        return '9'
    if n=='zero':
        return '0'
    else:
        return n
# result = list(map(strtodigit, matches))

# print(result)


f= open('day1_input.txt','r')

j=0

sum=0
for i in f: 
    m= re.search(pattern, i)
    first = m.group(0) if m else ""
    n = re.search(pattern_rev, i[::-1])
    last = n.group(0) if n else ""

    # print(last)
    first_num= strtodigit(first)
    last_num = strtodigitrev(last)
    twodigits = first_num+last_num
    sum+= int(twodigits)
    # print(last_num)

    # j+=1
    # if j==10:
    #     break

print(sum)