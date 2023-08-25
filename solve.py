import sys

def character_counts(line):
	char_counts = { 
		"0" : 0,
		"1" : 0,
		"." : 0,
	}
	for char in line:
		char_counts[char] += 1
	return char_counts

def matrix_empty_count(matrix):
	return sum(line.count(".") for line in matrix)

def replace_empty(line, el):
	for i in range(len(line)):
		if line[i] == '.':
			line[i] = el

def fill_line(line):
	char_counts = character_counts(line)
	if char_counts["."] == 0:
		return line	
	half_line_len = len(line) // 2
	if char_counts["0"] == half_line_len:
		replace_empty(line, "1")
	if char_counts["1"] == half_line_len:
		replace_empty(line, "0")

def empty_between_same(line):
	for i in range(1, len(line)-1):
		if line[i] == ".":
			if line[i-1] == "0" and line[i+1] == "0":
				line[i] = "1"
			if line[i-1] == "1" and line[i+1] == "1":
				line[i] = "0"

def sides_double(line):
	for i in range(len(line)):
		if line[i] == '.':
			if i > 1 and line[i-1] != '.' and line[i-1] == line[i-2]:
				line[i] = '0' if line[i-1] == '1' else '1'
			if i < (len(line) - 2) and line[i+1] != '.' and line[i+1] == line[i+2]:
				line[i] = '0' if line[i+1] == '1' else '1'

def possible_combinations(line):
	# TODO : replace specific cases with generic solution
	if line == list("0...0."):
		line[5] = '1'
	elif line == list("0..1.0"):
		line[1] = '1'
		line[2] = '0'
		line[4] = '1'
	elif line == list("1.0..1"):
		line[1] = '0'
		line[3] = '1'
		line[4] = '0'

class ColumnList:
	def __init__(self, matrix, column_index):
		self.matrix = matrix
		self.column_index = column_index

	def __getitem__(self, index):
		return self.matrix[index][self.column_index]

	def __setitem__(self, index, value):
		self.matrix[index][self.column_index] = value

	def __len__(self):
		return len(self.matrix)
       
def apply_rules(line):
	sides_double(line)
	empty_between_same(line)
	fill_line(line)
	possible_combinations(line)
		
if __name__ == "__main__":
	path = sys.argv[1] if len(sys.argv) >= 2 else './puzzles/6x6_puzzle_easy_1.txt'
	matrix = [list(line.strip()) for line in open(path).readlines()]
	
	print("Original binary puzzle :")
	for row in matrix:
		print("".join(row))
	
	step = 0
	previous_empty_count = matrix_empty_count(matrix)
	
	while True:
		for row in matrix:
			apply_rules(row)
		
		for i in range(len(matrix)):
			column = ColumnList(matrix, i)
			apply_rules(column)
		
		step = step + 1
				
		print("After " + str(step) + " step(s) :")
		for row in matrix:
			print("".join(row))
		
		empty_count = matrix_empty_count(matrix)
		if empty_count == 0 or empty_count == previous_empty_count:
			break
		previous_empty_count = empty_count
