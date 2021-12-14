with open('Day14/testInput.txt', 'r') as file:
# with open('Day14/input.txt', 'r') as file:
    lines = file.read().splitlines()

template = lines[0]
insertions = {}
empty_count = {}
for line in lines[2:]:
    a,b = line.split(' -> ')
    insertions[a] = a[0] + b + a[1]
    empty_count[a] = 0

steps = 10
inserts = empty_count.copy()
for insertion in insertions.keys(): # Count pairs from template
    count = len(template.replace(insertion, insertions[insertion])) - len(template)
    inserts[insertion] = count

for step in range(steps): # Count new pairs from previous pairs + insertions
    n_inserts = empty_count.copy()
    for i_key, i_value in inserts.items():
        if i_value > 0:
            n_inserts[insertions[i_key][:-1]] += i_value
            n_inserts[insertions[i_key][-2:]] += i_value
    inserts = n_inserts

letter_count = {}
for k,v in inserts.items(): # Count letters from all pairs
    for char in k:
        count = letter_count.get(char, 0)
        if count > 0: 
            letter_count[char] += v
        else:
            letter_count[char] = v

for char, v in letter_count.items(): # Remove intersecting letter count
    letter_count[char] = v//2 + v%2 

print(max(letter_count.values()) - min(letter_count.values()))