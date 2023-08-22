def character_counts(line):
	char_counts = { 
		"0" : 0,
		"1" : 0,
		"." : 0,
	}
	for char in line:
		char_counts[char] += 1
	return char_counts

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
		
if __name__ == "__main__":	
	matrix = [list(line.strip()) for line in open('6x6_puzzle_easy_1.txt').readlines()]
	
	print("Original binary puzzle :")
	for row in matrix:
		print("".join(row))
	
	for row in matrix:
		apply_rules(row)
	
	for i in range(len(matrix)):
		column = ColumnList(matrix, i)
		apply_rules(column)
			
	print("After one step :")
	for row in matrix:
		print("".join(row))
