
import re

f= open('day2_input.txt','r')

sum = 0
for i in f: 
    # red
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    red = re.findall(r'[0-9]{1,2}\sred',i)
    red = ' '.join(red)
    red = re.findall(r'[0-9]{1,2}',red)
    intlistred = [ int(i) for i in red ]
    red_max = max(intlistred)
    if red_max > 12:
        continue
    
    # green
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    green = re.findall(r'[0-9]{1,2}\sgreen',i)
    green = ' '.join(green)
    green = re.findall(r'[0-9]{1,2}',green)
    intlistgreen = [ int(i) for i in green ]
    green_max = max(intlistgreen)
    if green_max > 13:
        continue

    # blue
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    blue = re.findall(r'[0-9]{1,2}\sblue',i)
    blue = ' '.join(blue)
    blue = re.findall(r'[0-9]{1,2}',blue)
    intlistblue = [ int(i) for i in blue ]
    blue_max = max(intlistblue)
    if blue_max > 14:
        continue

    game_id = re.findall(r'Game\s[0-9]{1,3}',i)
    game_id = ' '.join(game_id)
    game_id = re.findall(r'[0-9]{1,3}',game_id)
    game_id = [ int(i) for i in game_id ]
    game_id = game_id[0]
    sum += game_id
    
print(sum)

f.close()