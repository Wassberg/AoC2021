with open('Day4/testInput.txt', 'r') as file:
# with open('Day4/input.txt', 'r') as file:
    lines = file.read().splitlines()

def get_number_list(string):
    return [int(num) for num in string.split(',')]

def generate_board_solutions(board_arr, board_size):
    solutions = []
    index = 0
    for index in range(board_size):
        solutions.append(board_arr[index*board_size:index*board_size+board_size])
        solutions.append(board_arr[index::board_size])
        index += 1
    return solutions

def check_bingo_board(board, nums):
    for solution in board:
        if all(num in nums for num in solution):
            return True
    return False
    
bingo_board_size = 5
bingo_nums = get_number_list(lines[0])
bingo_boards = [] 

board = ''
for line in lines[2:]:
    if(line == ''):
        bingo_boards.append(get_number_list(board.rstrip(',')))
        board = ''
        continue
    board += ','.join(line.split()) + ','
bingo_boards.append(get_number_list(board.rstrip(',')))

bingo_board_solutions = []
for bingo_board in bingo_boards:
    bingo_board_solutions.append(generate_board_solutions(bingo_board, bingo_board_size))

taken_nums = bingo_nums[0:bingo_board_size-1]
winning_board = []
for num in bingo_nums[bingo_board_size-1:]:
    taken_nums.append(num)
    board_index = 0
    for board in bingo_board_solutions:
        if(check_bingo_board(board, taken_nums)):
            winning_board = bingo_boards[board_index]
            break
        board_index += 1
    if(winning_board): break

unmarked_numbers = [num for num in winning_board if num not in taken_nums]

print(sum(unmarked_numbers)*taken_nums[-1])