with open('Day10/testInput.txt', 'r') as file:
# with open('Day10/input.txt', 'r') as file:
    lines = file.read().splitlines()

c_opens = ['(','[','{','<']
c_closes = {'(':')','[':']','{':'}','<':'>'}
c_points = {')':3,']':57,'}':1197,'>':25137}

c_errors = []
for line in lines:
    c_open = []
    for char in line:
        if char in c_opens:
             c_open.append(char)
        elif char == c_closes[c_open[-1]]:
             c_open.pop()
        else:
            c_errors.append(char)
            break

c_sum = 0
for char in c_errors:
    c_sum += c_points[char]
print(c_sum)