class Coordinate:
    def __init__(self, x, y, cid):
        self.x = x
        self.y = y
        self.id = cid


class Grid:
    def __init__(self, max_row, max_col):
        self.board = []
        self.max_row = max_row
        self.max_col = max_col
        for i in range(0, max_row):
            temp_list = []
            for j in range(0, max_col):
                temp_list.append('.')
            self.board.append(temp_list)


def read_input(filename):
    with open(filename) as file:
        result = file.readlines()
    return result


def pre_process(input_list):
    max_row = 0
    max_col = 0
    global grid
    result = []
    for i in range(0, len(input_list)):
        col = int(input_list[i][:input_list[i].index(',')])
        row = int(input_list[i][input_list[i].index(',') + 2:])
        if row > max_row:
            max_row = row
        if col > max_col:
            max_col = col
        result.append(Coordinate(row, col, str(i)))
    grid = Grid(max_row + 2, max_col + 2)
    for coordinate in result:
        grid.board[coordinate.x][coordinate.y] = coordinate.id
    return result


def manhattan_distance(x1, x2, y1, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def first_part(sub_grid, coordinates):
    banned_cords = set()
    for row in range(0, sub_grid.max_row):
        for col in range(0, sub_grid.max_col):
            min_distance = sub_grid.max_row + sub_grid.max_col
            min_coordinate = '.'
            if sub_grid.board[row][col] != '.':
                continue
            for coordinate in coordinates:
                temp_distance = manhattan_distance(coordinate.x, row, coordinate.y, col)
                if temp_distance < min_distance:
                    min_distance = temp_distance
                    min_coordinate = coordinate.id
                elif temp_distance == min_distance:
                    min_coordinate = '.'
            sub_grid.board[row][col] = min_coordinate
    cord_dict = {}
    for row in range(0, sub_grid.max_row):
        for col in range(0, sub_grid.max_col):
            if sub_grid.board[row][col] == '.':
                continue
            if sub_grid.board[row][col].upper() not in cord_dict.keys():
                cord_dict[sub_grid.board[row][col].upper()] = 1
            else:
                cord_dict[sub_grid.board[row][col].upper()] += 1
            if row == 0 or row == sub_grid.max_row - 1 or col == 0 or col == sub_grid.max_col - 1:
                banned_cords.add(sub_grid.board[row][col].upper())
    max_area = 0
    for cord, num in cord_dict.items():
        if cord in banned_cords:
            continue
        max_area = max(max_area, num)
    return max_area


def second_part(sub_grid, coordinates, manhattan_limit=10000):
    result = 0
    for row in range(0, sub_grid.max_row):
        for col in range(0, sub_grid.max_col):
            total_distance = 0
            for coordinate in coordinates:
                total_distance += manhattan_distance(coordinate.x, row, coordinate.y, col)
            if total_distance < manhattan_limit:
                result += 1
    return result


grid = Grid(0, 0)
lst = read_input("input")

cords = pre_process(lst)
print(first_part(grid, cords))

cords = pre_process(lst)
print(second_part(grid, cords))
