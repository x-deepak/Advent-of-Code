import re

f= open('day2_input.txt','r')

line = f.readline()
print(line)
# line = 'Game 100: 7 blue, 6 green, 31 red; 3 red, 5 green, 1 blue; 1 red, 5 green, 8 blue; 3 red, 1 green, 5 blue'
# print(line)

result = re.findall(r'[0-9]{1,2}\sred',line)
result = ' '.join(result)
result = re.findall(r'[0-9]{1,2}',result)
intresult = [ int(i) for i in result ]

print(result)
print(intresult)
print(max(intresult))

game_id = re.findall(r'Game\s[0-9]{1,3}',line)
game_id = ' '.join(game_id)
game_id = re.findall(r'[0-9]{1,3}',game_id)
game_id = [ int(i) for i in game_id ]
game_id = game_id[0]
print(game_id)