# with open('Day8/testInput.txt', 'r') as file:
with open('Day8/input.txt', 'r') as file:
    lines = file.read().splitlines()

output_nums = [line.split('|')[1].strip() for line in lines]

easy_digits = 0
for nums in output_nums:
    for num in nums.split(' '):
        if len(num) == 2 or len(num) == 3 or len(num) == 4 or len(num) == 7:
            easy_digits += 1

print(easy_digits)