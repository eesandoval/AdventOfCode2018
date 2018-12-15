from copy import deepcopy

class Cart:
    def __init__(self, direction):
        self.direction = direction
        self.next_intersection = 0
        if self.direction in ['>', '<']:
            self.on_track = '-'
        else:
            self.on_track = '|'
        self.left = {'v':'>', '>':'^', '^':'<', '<':'v'}
        self.right = {'v':'<', '<':'^', '^':'>', '>':'v'}

    def __repr__(self):
        return '\'' + self.direction + '\''

    def __str__(self):
        return '\'' + self.direction + '\''

    def intersection(self):
        self.next_intersection += 1
        if self.next_intersection > 3:
            self.next_intersection = 1
        if self.next_intersection == 1:
            self.direction = self.left[self.direction]
        elif self.next_intersection == 2:
            self.direction = self.direction
        elif self.next_intersection == 3:
            self.direction = self.right[self.direction]
    
    def __eq__(self, other):
        if self.direction == other:
            return True
        return False

    def replace_track(self, new_track):
        if new_track == '+':
            self.intersection()
        elif new_track == '\\' and self.direction in ['v', '^']:
            self.direction = self.left[self.direction]
        elif new_track == '\\' and self.direction in ['>', '<']:
            self.direction = self.right[self.direction]
        elif new_track == '/' and self.direction in ['v', '^']:
            self.direction = self.right[self.direction] 
        elif new_track == '/' and self.direction in ['>', '<']:
            self.direction = self.left[self.direction]
        old_track = self.on_track
        self.on_track = new_track 
        return old_track


def read_input(filename):
    with open(filename) as file:
        lines = file.readlines()
    result = []
    for line in lines:
        result.append(list(line.rstrip()))
    return result


def first_part(input_list, remove_if_crash=False):
    tick = 0
    current_grid = deepcopy(input_list)
    original = deepcopy(input_list)
    carts = 0
    for row in range(len(original)):
        for col in range(len(original[row])):
            c = original[row][col]
            if c == 'v' or c == '^' or c == '>' or c == '<':
                current_grid[row][col] = Cart(c)
                carts += 1
    new_grid = deepcopy(current_grid)
    while True:
        tick += 1
        print("tick: " + str(tick) + " and carts: " + str(carts))
        if carts <= 1 and remove_if_crash:
            for row in range(0, len(current_grid)):
                for col in range(0, len(current_grid[row])):
                    if current_grid[row][col] in ['v','^','<','>']:
                        return (col, row)
        for row in range(0, len(current_grid)):
            for col in range(0, len(current_grid[row])):
                current_char = current_grid[row][col]
                if current_char == 'v':
                    if new_grid[row+1][col] in ['v','^','<','>']:
                        if remove_if_crash:
                            new_grid[row+1][col] = new_grid[row+1][col].on_track
                            new_grid[row][col] = new_grid[row][col].on_track
                            carts -= 2
                            continue
                        else:
                            return (col,row+1)
                    new_grid[row][col] = current_char.replace_track(new_grid[row+1][col])
                    new_grid[row+1][col] = current_char
                elif current_char == '^':
                    if new_grid[row-1][col] in ['v','^','<','>']:
                        if remove_if_crash:
                            new_grid[row-1][col] = new_grid[row-1][col].on_track
                            new_grid[row][col] = new_grid[row][col].on_track
                            carts -= 2
                            continue
                        else:
                            return (col,row-1)
                    new_grid[row][col] = current_char.replace_track(new_grid[row-1][col])
                    new_grid[row-1][col] = current_char
                elif current_char == '>':
                    if new_grid[row][col+1] in ['v','^','<','>']:
                        if remove_if_crash:
                            new_grid[row][col+1] = new_grid[row][col+1].on_track
                            new_grid[row][col] = new_grid[row][col].on_track
                            carts -= 2
                            continue
                        else:
                            return (col+1,row)
                    new_grid[row][col] = current_char.replace_track(new_grid[row][col+1])
                    new_grid[row][col+1] = current_char
                elif current_char == '<':
                    if new_grid[row][col-1] in ['v','^','<','>']:
                        if remove_if_crash:
                            new_grid[row][col-1] = new_grid[row][col-1].on_track
                            new_grid[row][col] = new_grid[row][col].on_track
                            carts -= 2
                            continue
                        else:
                            return (col-1,row)
                    new_grid[row][col] = current_char.replace_track(new_grid[row][col-1])
                    new_grid[row][col-1] = current_char        
        current_grid = deepcopy(new_grid)


def second_part(input_list):
	return first_part(input_list, True)


lst = read_input("input")
print(first_part(lst))
print(second_part(lst))
