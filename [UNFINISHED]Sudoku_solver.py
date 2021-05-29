"""
To-Do list:
1. Trying a possible configuration/Sudoku solver
2. Build a GUI
"""
import tool_collection


class Sudoku_grid:
    def __init__(self):
        while True:
            self.columns = tool_collection.get_input('How many lines/columns does the Sudoku have?', int)
            if check_column_number(self.columns):
                break
            print('A sudoku must have n**2 lines/columns.. ')

        #    def initialize_grid(self):

        def check_box_number(box_number, column_number):  # checks whether the number is allowed
            if 0 <= box_number <= column_number:
                return True
            return False

        grid = []
        for lines in range(self.columns):
            line = []
            for columns in range(self.columns):
                while True:
                    number = tool_collection.get_input(f'Please enter the number ({lines + 1}, {columns + 1})'
                                                       f'; 0 = empty ', int)
                    if check_box_number(number, self.columns):
                        line.append(number)
                        break
                    else:
                        print('This is no valid input')
                        continue

            if grid:
                grid.append(line)  # adding a list for every line to 'grid'
            else:
                grid = [line]
        self.grid = grid


def sudoku_solver(input_grid, column_number):
    block_size = int(pow(column_number, 1 / 2))

    solve_list = []
    for lines in input_grid:
        line = []
        for columns in lines:
            line.append(columns)
        if solve_list:
            solve_list.append(line)
        else:
            solve_list = [line]

    for line in range(column_number):
        for column in range(column_number):
            if solve_list[line][column] != 0:
                continue
            for possible_number in range(1, column_number + 1):
                solve_list[line][column] = possible_number
                # illegal by line, column, or block
                illegal = check_illegal_list(solve_list[line]) or \
                          check_illegal_list(convert_column_to_list(solve_list, column, column_number)) or \
                          check_illegal_list(
                              convert_block_to_list(solve_list, assign_to_block(line, column, block_size),
                                                    column_number))
                if not illegal:
                    if possible_number == do_not_try[line][column]:
                        continue
                    else:
                        if do_not_try[line][column]:
                            do_not_try[line][column].append(line)
                        else:
                            do_not_try[line][column] = [possible_number]
                    break
                elif possible_number == 9 and illegal:
                    sudoku_solver(input_grid, column_number)
                else:
                    continue

    return solve_list


def print_grid(grid):
    for i in grid:
        print(i)


def check_column_number(column_number):
    num_root = pow(column_number, 1 / 2)
    if int(num_root) == num_root:
        return True
    return False


def check_illegal_list(input_line):
    def check_list_for_duplicates(dup_list):
        for element in dup_list:
            if dup_list.count(element) > 1 and element != 0:
                return True

    if check_list_for_duplicates(input_line):
        return True


def convert_column_to_list(input_grid, column, column_number):
    converted_list = []
    for line in range(column_number):
        converted_list.append(input_grid[line][column])
    return converted_list


def convert_block_to_list(input_grid, block, column_number):
    block_size = int(pow(column_number, 1 / 2))
    block_line = (block // block_size) * block_size
    block_column = (block % block_size) * block_size
    converted_list = []
    for line in range(block_size):
        for column in range(block_size):
            converted_list.append(input_grid[block_line + line][block_column + column])
    return converted_list


def assign_to_block(line, column, block_size):
    block_line = line // block_size
    block_column = column // block_size
    block = block_line * block_size + block_column
    return block


def check_illegal_grid(input_grid, column_number):
    for line in input_grid:
        return check_illegal_list(line)

    for column in range(column_number):
        for number in convert_column_to_list(input_grid, column, column_number):
            return check_illegal_list(number)

    for block in range(column_number):
        for number in convert_block_to_list(input_grid, block, column_number):
            return check_illegal_list(number)

    return False


if __name__ == '__main__':

    sudoku_grid = Sudoku_grid()
    print_grid(sudoku_grid.grid)
    print('')
    print('')
    if check_illegal_grid(sudoku_grid.grid, sudoku_grid.columns):
        print('The sudoku is illegal')
    do_not_try = []
    solved_sudoku = sudoku_solver(sudoku_grid.grid, sudoku_grid.columns)
    print_grid(solved_sudoku)
    if check_illegal_grid(sudoku_grid.grid, sudoku_grid.columns):
        print('An error occurred.. ')
