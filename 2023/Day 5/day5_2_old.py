import re


f= open('day5_input.txt','r')
line_list = f.readlines()
seeds_list = re.findall(r'\d+',line_list[0])
seeds_list_int= list(map(int, seeds_list))
# print(seeds_list_int)


def map_finder(i,start,stop):
    for j in range(start,stop):
        map_line = re.findall(r'\d+',line_list[j])
        map_line_int = list(map(int,map_line))
        if i>=map_line_int[1] and i<=map_line_int[1]+(map_line_int[2]-1):
            diff = i-map_line_int[1]
            dest_no = map_line_int[0]+diff
            return dest_no
    return i


min_loc = 0
for k,v in enumerate(seeds_list_int):
    if k+1%2==0:
        continue
    for i in range(seeds_list_int[k],seeds_list_int[k+1]):
        soil_no = map_finder(i,3,12)
        fertilizer_no = map_finder(soil_no,14,57)
        water_no = map_finder(fertilizer_no,59,105)
        light_no = map_finder(water_no,107,147)
        temp_no = map_finder(light_no,149,186)
        humidity_no = map_finder(temp_no,188,206)
        location_no = map_finder(humidity_no,208,250)
        if location_no<min_loc:
            min_loc=location_no

print(min_loc)


