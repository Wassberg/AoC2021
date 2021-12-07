# with open('Day6/testInput.txt', 'r') as file:
with open('Day6/input.txt', 'r') as file:
    lines = file.read().splitlines()

fish_list = [int(i) for i in lines[0].split(',')]

max_days = 80
for i in range(0, max_days):
    index = 0
    for fish in list(fish_list):
        if fish == 0:
            fish_list.append(8)
            fish_list[index] = 6
        else:
            fish_list[index] -= 1
        index += 1

print(len(fish_list))