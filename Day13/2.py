with open('Day13/testInput.txt', 'r') as file:
# with open('Day13/input.txt', 'r') as file:
    lines = file.read().splitlines()

dots = []
folds = []
for line in lines:
    if ',' in line:
        x, y = line.split(',')
        dots.append({'x':int(x), 'y':int(y)})
    elif '=' in line:
        p, c = line.split(' ')[2].split('=')
        folds.append({'p':p, 'c':int(c)})

for fold in folds:  
    fold_p = fold['p']
    fold_c = fold['c']
    for dot in dots:
        if fold_p == 'x' and dot['x'] > fold_c:
            dot['x'] = fold_c - (dot['x'] - fold_c)
        elif fold_p == 'y' and dot['y'] > fold_c:
            dot['y'] = fold_c - (dot['y'] - fold_c)
    dots = [dict(t) for t in {tuple(d.items()) for d in dots}]
    
x_max = y_max = 0
for dot in dots:
    if dot['x'] > x_max: x_max = dot['x']
    if dot['y'] > y_max: y_max = dot['y']

for y in range(y_max + 1):
    line = "".ljust(x_max)
    for dot in dots:
        if dot['y'] == y: line = line[:dot['x']] + '█' + line[dot['x'] + 1:]
    print(line)