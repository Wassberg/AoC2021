with open('Day8/testInput.txt', 'r') as file:
# with open('Day8/input.txt', 'r') as file:
    lines = file.read().splitlines()

def decode_number(num_string, decrypt_map):
    check = set(num_string) & set(decrypt_map[4]) # Check shared segments with 4
    if len(check) == 4: return 9 
    check = set(num_string) & set(decrypt_map[8]) # Check shared segments with 8
    if len(check) == 6:
        x = set(num_string) & set(decrypt_map[1]) # Check shared segments with 1
        if len(x) == 1: return 6
    elif len(check) == 5:
        x = set(num_string) & set(decrypt_map[1]) # Check shared segments with 1
        if len(x) == 1: 
            y = set(num_string) & set(decrypt_map[4]) # Check shared segments with 4
            if len(y) == 3: return 5
            elif len(y) == 2: return 2
        x = set(num_string) & set(decrypt_map[1]) # Check shared segments with 1
        if len(x) == 2: return 3
    return 0

# Split up signal patterns and output numbers 
signal_patterns = []
output_nums = []
for line in lines:
    split = line.split('|')
    signal_patterns.append(split[0].strip().split(' '))
    output_nums.append(split[1].strip().split(' '))

index = 0
decoded_numbers = []
for pattern in signal_patterns:
    num_map = {}
    # Loop through pattern to find 'easy numbers' and add to decoding map
    for val in pattern:
        val = "".join(sorted(val))
        if len(val) == 2: num_map[1] = val
        elif len(val) == 3: num_map[7] = val
        elif len(val) == 4: num_map[4] = val
        elif len(val) == 7: num_map[8] = val

    # Loop through pattern to decode 'non-easy numbers' and add to decoding map
    for val in pattern:
        val = "".join(sorted(val))
        if len(val) == 5 or len(val) == 6: num_map[decode_number(val, num_map)] = val
    
    decoded_number = 0

    # Loop through output numbers to decode it based on the decoding map
    for val in output_nums[index]:
        val = "".join(sorted(val))
        decoded_val = list(num_map.keys())[list(num_map.values()).index(val)]
        decoded_number = decoded_number*10 + decoded_val

    decoded_numbers.append(decoded_number)
    index += 1

print(sum(decoded_numbers))