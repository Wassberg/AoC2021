f = open("Day1/testInput.txt", "r")
# f = open("Day1/input.txt", "r")
lines = f.read().splitlines()

depths = [int(i) for i in lines]
i = 0
increases = 0
prev_depth_sum = None
for depth in depths[:-2]:
    depth_sum = depths[i] + depths[i+1] + depths[i+2]
    if(prev_depth_sum != None and depth_sum > prev_depth_sum):
        increases += 1
    i += 1
    prev_depth_sum = depth_sum
print(increases)
