"""
To-Do list:
1. Trying a possible configuration/Sudoku solver
2. Build a GUI
"""
import tool_collection


class Sudoku_grid:
    def __init__(self):
        while True:
            self.columns = tool_collection.get_input('How many lines/columns does the Sudoku have? ', int)
            if check_column_number(self.columns):
                break
            print('A sudoku must have n**2 lines/columns.. ')

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

    def make_changes(self):
        line = tool_collection.get_input('Please enter the line.. ', int) - 1
        column = tool_collection.get_input('Please enter the column.. ', int) - 1
        number = tool_collection.get_input('Please enter the number to replace '
                                           '{self.grid[line][column]} at ({line + 1}, {column + 1}) with.. ', int)
        if 1 <= line <= column_number and 1 <= column <= column_number and check_box_number(number):
            self.grid[line][column] = number
        else:
            return False


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
                    solved_grid = sudoku_solver(solve_list, column_number)
                    if not solved_grid:
                        continue
                    else:
                        return solved_grid
                elif illegal and possible_number == column_number:
                    solve_list[line][column] = 0
                    return None
                else:
                    continue

    return solve_list


def print_grid(grid):
    for i in grid:
        print(i)


def check_for_zero(grid):
    for line in grid:
        for column in line:
            if column == 0:
                return True
    return False


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
    return False


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


def ask_for_changes():
    changes = str(input('Do you want to make changes?[Y/n]')).lower()
    if 'y' in changes:
        return True
    elif 'n' in changes:
        return False
    else:
        pass


if __name__ == '__main__':
    while True:
        sudoku_grid = Sudoku_grid()
        print_grid(sudoku_grid.grid)
        print('')
        print('')
        change = bool(ask_for_changes())
        if change:
            sudoku_grid.make_changes()
        elif change is False:
            pass
        else:
            break
        if check_illegal_grid(sudoku_grid.grid, sudoku_grid.columns):
            print('The sudoku is illegal\n')
            if ask_for_changes():
                sudoku_grid.make_changes()
            else:
                break
        solved_sudoku = sudoku_solver(sudoku_grid.grid, sudoku_grid.columns)
        print_grid(solved_sudoku)
        if check_illegal_grid(sudoku_grid.grid, sudoku_grid.columns):
            print('An error occurred.. ')
        else:
            print('\nSolved!\n')
        break
