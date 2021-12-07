from collections import Counter

# with open('Day6/testInput.txt', 'r') as file:
with open('Day6/input.txt', 'r') as file:
    lines = file.read().splitlines()

fish_list = [int(i) for i in lines[0].split(',')]
counter = Counter([i for i in fish_list])

max_days = 256
for i in range(max_days):
    c = Counter()
    for age, count in counter.items():
        new_age = age -1
        if(new_age < 0):
            c[8] += count
            new_age += 7
        c[new_age] += count
    counter = c

print(sum(counter.values()))