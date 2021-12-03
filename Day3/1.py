with open('Day3/testInput.txt', 'r') as file:
# with open('Day3/input.txt', 'r') as file:
    lines = file.read().splitlines()

arr = []
gamma_str = ''
epsilon_str = ''

for i in range(len(lines[0])):
    col = ''
    for line in lines:
        col += line[i]
    arr.append(col)

for col in arr:
    ones = col.count('1')
    zeroes = col.count('0')
    gamma_str += '1' if ones > zeroes else '0'
    epsilon_str += '0' if ones > zeroes else '1'

consumption = int(gamma_str,2)*int(epsilon_str,2)
print(consumption)