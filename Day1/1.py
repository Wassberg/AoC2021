f = open("Day1/testInput.txt", "r")
# f = open("Day1/input.txt", "r")
lines = f.read().splitlines()

depths = [int(i) for i in lines]
increases = 0
current_depth = depths[0]
for depth in depths[1:]:
    if(depth > current_depth): 
        increases += 1
    current_depth = depth

print(increases)