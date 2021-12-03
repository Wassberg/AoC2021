with open('Day3/testInput.txt', 'r') as file:
# with open('Day3/input.txt', 'r') as file:
    lines = file.read().splitlines()

def get_arr(lines):
    arr = []
    for i in range(len(lines[0])):
        col = ""
        for line in lines:
            col += line[i]
        arr.append(col)
    return arr

def get_numbers(num_list, num, col):
    new_list = []
    for number in num_list:
        if(number[col] == num):
            new_list.append(number)
    return new_list 

arr = get_arr(lines)
oxygen_gr_arr = co2_sr_arr = arr
oxygen_gr_nums = co2_sr_nums = lines
oxygen_gr = co2_sr = ''

col_index = 0
while(len(oxygen_gr_nums) > 1):
    ones = oxygen_gr_arr[col_index].count('1')
    zeroes = oxygen_gr_arr[col_index].count('0')
    toKeep = '1' if ones >= zeroes else '0'
    oxygen_gr_nums = get_numbers(oxygen_gr_nums, toKeep, col_index)
    oxygen_gr_arr = get_arr(oxygen_gr_nums)
    col_index += 1
oxygen_gr = oxygen_gr_nums[0]

col_index = 0
while(len(co2_sr_nums) > 1):
    ones = co2_sr_arr[col_index].count('1')
    zeroes = co2_sr_arr[col_index].count('0')
    toKeep = '1' if ones < zeroes else '0'
    co2_sr_nums = get_numbers(co2_sr_nums, toKeep, col_index)
    co2_sr_arr = get_arr(co2_sr_nums)
    col_index += 1
co2_sr = co2_sr_nums[0]

print(int(oxygen_gr,2) * int(co2_sr,2))