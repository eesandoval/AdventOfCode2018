def read_input(filename):
    with open(filename) as file:
        lines = file.readlines()
    return int(lines[0])


def find_power_level(x, y, grid_serial_number):
	rack_id = x + 10
	result = rack_id
	result *= y
	result += grid_serial_number
	result *= rack_id 
	if (result < 100):
		return -5 
	return int(str(result)[-3]) - 5


def create_grid(grid_serial_number):
	grid = [[0 for _ in range(300)] for _ in range(300)]
	for y in range(0, len(grid)):
		for x in range(0, len(grid[y])):
			grid[y][x] = find_power_level(x, y, grid_serial_number) 
	return grid


def find_max(grid_serial_number, grid, size):
	max_power_level = 0
	max_x = 0
	max_y = 0
	for y in range(0, len(grid) - size - 1):
		for x in range(0, len(grid[y]) - size - 1):
			power_level = 0
			for s in range(size):
				power_level += sum(grid[y+s][x:x+size])
			if power_level > max_power_level:
				max_power_level = power_level
				max_x = x 
				max_y = y
	return (max_x, max_y, max_power_level)


def first_part(grid_serial_number, grid):
	result_triple = find_max(grid_serial_number, grid, 3)
	return (result_triple[0], result_triple[1])


def second_part(grid_serial_number, grid):
	max_result_triple = (0, 0, 0)
	max_result_size = 0
	not_bigger_flag = 0
	for size in range(1, 300):
		result_triple = find_max(grid_serial_number, grid, size)
		if result_triple[2] >= max_result_triple[2]:
			max_result_triple = result_triple
			max_result_size = size
		else:
			not_bigger_flag += 1
		if not_bigger_flag > 4:
			break
	return (max_result_triple[0], max_result_triple[1], max_result_size)


lst = read_input("input")
g = create_grid(lst)
print(first_part(lst, g)) 
print(second_part(lst, g))
