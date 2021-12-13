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

fold_p = folds[0]['p']
fold_c = folds[0]['c']
for dot in dots:
    if fold_p == 'x':
        if dot['x'] > fold_c:
            dot['x'] = fold_c - (dot['x'] - fold_c)
    elif fold_p == 'y':
        if dot['y'] > fold_c:
            dot['y'] = fold_c - (dot['y'] - fold_c)

dots = [dict(t) for t in {tuple(d.items()) for d in dots}]
    
print(len(dots))