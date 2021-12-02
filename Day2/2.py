# f = open("Day2/testInput.txt", "r")
f = open("Day2/input.txt", "r")
lines = f.read().splitlines()

p_horizontal = 0
p_vertical = 0
aim = 0

for line in lines:
    direction, value = line.split(" ")
    if(direction == 'forward'): 
        p_horizontal += int(value)
        p_vertical += int(value)*aim
    if(direction == 'down'): aim += int(value)
    if(direction == 'up'): aim -= int(value)

print(p_horizontal * p_vertical)