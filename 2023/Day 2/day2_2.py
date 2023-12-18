
import re

f= open('day2_input.txt','r')

power = 0
for i in f: 
    # red
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    red = re.findall(r'[0-9]{1,2}\sred',i)
    red = ' '.join(red)
    red = re.findall(r'[0-9]{1,2}',red)
    intlistred = [ int(i) for i in red ]
    red_max = max(intlistred)
    
    
    # green
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    green = re.findall(r'[0-9]{1,2}\sgreen',i)
    green = ' '.join(green)
    green = re.findall(r'[0-9]{1,2}',green)
    intlistgreen = [ int(i) for i in green ]
    green_max = max(intlistgreen)


    # blue
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    blue = re.findall(r'[0-9]{1,2}\sblue',i)
    blue = ' '.join(blue)
    blue = re.findall(r'[0-9]{1,2}',blue)
    intlistblue = [ int(i) for i in blue ]
    blue_max = max(intlistblue)

    print(red_max,green_max,blue_max)
    power += red_max * green_max * blue_max

    
print(power)

f.close()