with open("Day1/testInput.txt", "r") as file:
# with open("Day1/input.txt", "r") as file:
    lines = file.read().splitlines()

depths = [int(i) for i in lines]
increases = 0
current_depth = depths[0]
for depth in depths[1:]:
    if(depth > current_depth): 
        increases += 1
    current_depth = depth

print(increases)