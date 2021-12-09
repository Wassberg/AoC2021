with open('Day9/testInput.txt', 'r') as file:
# with open('Day9/input.txt', 'r') as file:
    lines = file.read().splitlines()

def is_low_point(map, i, j):
    if i > 0:
        if map[i][j] >= map[i-1][j]: return False
    if j > 0:
        if map[i][j] >= map[i][j-1]: return False
    if i < len(map)-1:
        if map[i][j] >= map[i+1][j]: return False
    if j < len(map[i])-1:
        if map[i][j] >= map[i][j+1]: return False
    return True

p_map = []
for line in lines: 
    p_map.append(list(map(int, list(line))))

low_points = []
for i in range(len(p_map)):
    for j in range(len(p_map[i])):
        if is_low_point(p_map, i, j):
          low_points.append(p_map[i][j])  

print(sum(low_points) + len(low_points))