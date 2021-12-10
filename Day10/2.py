import statistics

with open('Day10/testInput.txt', 'r') as file:
# with open('Day10/input.txt', 'r') as file:
    lines = file.read().splitlines()

c_opens = ['(','[','{','<']
c_closes = {'(':')','[':']','{':'}','<':'>'}
c_points = {')':1,']':2,'}':3,'>':4}

lines_to_remove = []
index = 0
for line in list(lines):
    c_open = []
    for char in line:
        if char in c_opens: 
            c_open.append(char)
        elif char == c_closes[c_open[-1]]: 
            c_open.pop()
        else:
            lines_to_remove.append(index)
            break
    index += 1

for line_num in sorted(lines_to_remove, reverse=True):
    del(lines[line_num])

c_closings = []
for line in lines:
    c_open = []
    c_close = []
    for char in line:
        if char in c_opens: 
            c_open.append(char)
        elif char == c_closes[c_open[-1]]:  
            c_open.pop()
    for char in reversed(c_open):
        c_close.append(c_closes[char])
    c_closings.append(c_close)
        
totals = []
for closing in c_closings:
    line_total = 0
    for char in closing:
        line_total = line_total*5 + c_points[char]
    totals.append(line_total)

print(statistics.median(totals))