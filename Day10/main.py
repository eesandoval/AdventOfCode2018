from itertools import *
import re


position_x, position_y, vector_x, vector_y = [], [], [], []
line_count = 0


def read_input(filename):
	global position_x
	global position_y
	global vector_x
	global vector_y 
	global line_count
	with open(filename) as file:
		lines = file.readlines()
	for line in lines:
		position_line = line[line.index('<') + 1:line.index('>')]
		line_v = line[line.index('velocity'):]
		vector_line = line_v[line_v.index('<') + 1:line_v.index('>')]
		position_x.append(int(position_line.split(',')[0]))
		position_y.append(int(position_line.split(',')[1]))
		vector_x.append(int(vector_line.split(',')[0]))
		vector_y.append(int(vector_line.split(',')[1]))
	line_count = len(position_x)


def pre_process():
	global position_x
	global position_y
	global vector_x
	global vector_y
	global line_count
	min_x, min_y = min(position_x), min(position_y)
	w = max(position_x) - min_x + 1
	h = max(position_y) - min_y + 1
	if h > 10:
		return False
	t = [['.'] * w for _ in range(h)]
	for i in range(line_count):
		t[position_y[i] - min_y][position_x[i] - min_x] = '#'
	for l in t:
		print(''.join(l))
	print()
	return True


def first_second_part():
	for t in count(1):
		for i in range(line_count):
			position_x[i] += vector_x[i]
			position_y[i] += vector_y[i]
		if pre_process():
			return t 

read_input("input")
print(first_second_part())
