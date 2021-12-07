from collections import Counter

with open('Day7/testInput.txt', 'r') as file:
# with open('Day7/input.txt', 'r') as file:
    lines = file.read().splitlines()

crab_list = [int(i) for i in lines[0].split(',')]
counter = Counter([i for i in crab_list])
h_max = max(crab_list)
h_min = min(crab_list)

fuel_list = []
for h in range(h_min, h_max):
    used_fuel = 0
    for crab_h, count in counter.items():
        used_fuel += abs((crab_h - h)*count)
    fuel_list.append(used_fuel)

print(min(fuel_list))