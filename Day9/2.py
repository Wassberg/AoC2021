with open('Day9/testInput.txt', 'r') as file:
# with open('Day9/input.txt', 'r') as file:
    lines = file.read().splitlines()

def is_low_point(p_map, i, j):
    if i > 0:
        if p_map[i][j] >= p_map[i-1][j]: return False
    if j > 0:
        if p_map[i][j] >= p_map[i][j-1]: return False
    if i < len(p_map)-1:
        if p_map[i][j] >= p_map[i+1][j]: return False
    if j < len(p_map[i])-1:
        if p_map[i][j] >= p_map[i][j+1]: return False
    return True

def get_basin_size(p_map, i, j, basin_p = set()):
    basin_pos = set()
    if i > 0:
        if p_map[i-1][j] != 9: basin_pos.add(str(i-1)+','+str(j))
    if j > 0:
        if p_map[i][j-1] != 9: basin_pos.add(str(i)+','+str(j-1))
    if i < len(p_map)-1:
        if p_map[i+1][j] != 9: basin_pos.add(str(i+1)+','+str(j))
    if j < len(p_map[i])-1:
        if p_map[i][j+1] != 9: basin_pos.add(str(i)+','+str(j+1))

    set_diff = basin_pos - basin_p
    basin_p = set.union(basin_pos, basin_p)
    for coord in set_diff:
        x,y = coord.split(',')
        basin_p = set.union(basin_p, get_basin_size(p_map, int(x), int(y), basin_p))
    return basin_p

p_map = []
for line in lines: 
    p_map.append(list(map(int, list(line))))

low_points = []
basins = []
for i in range(len(p_map)):
    for j in range(len(p_map[i])):
        if is_low_point(p_map, i, j):
          low_points.append(p_map[i][j])  
          basins.append(get_basin_size(p_map, i, j, {str(i)+','+str(j)}))

basins.sort(key=len, reverse=True)
product = 1
for basin in basins[0:3]:
    product *= len(basin)
print(product)