with open('Day11/testInput.txt', 'r') as file:
# with open('Day11/input.txt', 'r') as file:
    lines = file.read().splitlines()

def flash(octo, octos):
    if octo["energy"] < 9 or octo["flashed"]: 
        octo["energy"] += 1
        return 0
    octo["flashed"] = True
    octo["energy"] = 0
    flashes = 1
    octo_left_above = octos.get(str(octo["x"]-1)+","+str(octo["y"]-1), None)
    if octo_left_above and not octo_left_above["flashed"]:
        flashes += flash(octo_left_above, octos)
    octo_above = octos.get(str(octo["x"])+","+str(octo["y"]-1), None)
    if octo_above and not octo_above["flashed"]:
        flashes += flash(octo_above, octos)
    octo_right_above = octos.get(str(octo["x"]+1)+","+str(octo["y"]-1), None)
    if octo_right_above and not octo_right_above["flashed"]:
        flashes += flash(octo_right_above, octos)
    octo_left = octos.get(str(octo["x"]-1)+","+str(octo["y"]), None)
    if octo_left and not octo_left["flashed"]:
        flashes += flash(octo_left, octos)
    octo_right = octos.get(str(octo["x"]+1)+","+str(octo["y"]), None)
    if octo_right and not octo_right["flashed"]:
        flashes += flash(octo_right, octos)
    octo_left_below = octos.get(str(octo["x"]-1)+","+str(octo["y"]+1), None)
    if octo_left_below and not octo_left_below["flashed"]:
        flashes += flash(octo_left_below, octos)
    octo_below = octos.get(str(octo["x"])+","+str(octo["y"]+1), None)
    if octo_below and not octo_below["flashed"]:
        flashes += flash(octo_below, octos)
    octo_right_below = octos.get(str(octo["x"]+1)+","+str(octo["y"]+1), None)
    if octo_right_below and not octo_right_below["flashed"]:
        flashes += flash(octo_right_below, octos)
    return flashes

octos = {}
for x, line in enumerate(lines):
    for y, energy in enumerate(line):
        octos[str(x)+','+str(y)] = {"energy":int(energy), "flashed": False, "x": x, "y": y}

all_flash = False
i = 0
while(not all_flash):
    all_flash = True
    for coord, octo in octos.items():
        octo["energy"] += 1

    for coord, octo in octos.items():
        if octo["energy"] > 9 and not octo["flashed"]:
            flash(octo, octos)

    for coord, octo in octos.items():
        if octo["energy"] > 9 and octo["flashed"]:
            octo["energy"] = 0
        elif not octo["flashed"]:
            all_flash = False
        octo["flashed"] = False
    i += 1

print(i)