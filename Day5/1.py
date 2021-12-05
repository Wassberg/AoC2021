with open('Day5/testInput.txt', 'r') as file:
# with open('Day5/input.txt', 'r') as file:
    lines = file.read().splitlines()

def get_coordinations(str):
    coords = str.replace(' -> ', ',').split(',')
    return list(map(int, coords))

# Real ugly, but it works
def add_coords(dict, x1, x2, y1, y2):
    if(x1 == x2):
        y_max = max(y1, y2)
        y_min = min(y1, y2)
        for i in range(y_min, y_max+1):
            if (x1,i) in dict.keys():
                dict[x1,i] += 1
            else:
                dict[x1,i] = 1
    elif(y1 == y2):
        x_max = max(x1, x2)
        x_min = min(x1, x2)
        for i in range(x_min, x_max+1):
            if (i,y1) in dict.keys():
                dict[i,y1] += 1
            else:
                dict[i,y1] = 1
    return dict

coord_dict = {}
for line in lines:
    x1, y1, x2, y2 = get_coordinations(line)
    coord_dict = {**coord_dict,  **add_coords(coord_dict, x1, x2, y1, y2)}

overlaps = 0
for key in coord_dict.keys():
    if coord_dict[key] > 1: overlaps += 1

print(overlaps)