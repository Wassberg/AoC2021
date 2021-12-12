with open('Day12/testInput.txt', 'r') as file:
# with open('Day12/input.txt', 'r') as file:
    lines = file.read().splitlines()

cave_connections = {}

def find_paths(cave, small_caves_visited, extra_cave, path, paths, connections):
    small_caves_visited = small_caves_visited.copy()
    path = path.copy()
    path.append(cave)
    if cave == 'end':
        paths.append(path)
        return path
    if cave in small_caves_visited and not extra_cave is None: return path
    elif cave.islower():
        if cave in small_caves_visited and extra_cave is None:
            extra_cave = cave    
        small_caves_visited.append(cave)
    for con in connections.get(cave, []):
        if con == 'start' or (con in small_caves_visited and not extra_cave is None):
            continue
        else:
            find_paths(con, small_caves_visited, extra_cave, path, paths, connections)
    return paths
    
# Create cave map
for connection in lines:
    c_from, c_to = connection.split('-')
    con = cave_connections.get(c_from, [])
    if not con:
        cave_connections[c_from] = [c_to]
    elif not c_to in con:
        con.append(c_to)
    con = cave_connections.get(c_to, [])
    if not con:
        cave_connections[c_to] = [c_from]
    elif not c_from in con:
        con.append(c_from)

paths = []
for con in cave_connections.get("start", []):
        paths.extend(find_paths(con, [], None, ['start'],  [], cave_connections))

print(len(paths))