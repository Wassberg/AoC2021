with open("Day2/testInput.txt", "r") as file:
# with open("Day2/input.txt", "r") as file:
    lines = file.read().splitlines()

p_horizontal = 0
p_vertical = 0

for line in lines:
    direction, value = line.split(" ")
    if(direction == 'forward'): p_horizontal += int(value)
    if(direction == 'down'): p_vertical += int(value)
    if(direction == 'up'): p_vertical -= int(value)


print(p_horizontal * p_vertical)