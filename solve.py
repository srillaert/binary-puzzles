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

def maximum_two(line):
	previous = ""
	for char in line:
		count = count + 1 if char == previous else 1
		if count > 2:
			return False
		previous = char
	return True
	
def is_solved_line(line, size):		
	# each row and column contains as many zeroes as ones		
	counts = character_counts(line)
	if counts["0"] != size // 2 or counts["1"] != size // 2:
		return False
	
	if not maximum_two(line):
		return False
		
	return True
	
def is_solved_puzzle(matrix):
	size = len(matrix)
	if any(len(row) != size for row in matrix):
		return False # not a valid puzzle
	
	if not all(is_solved_line(line, size) for line in matrix):
		return False
		
	# each row in unique
	for i in range(len(matrix)):
		for j in range(i+1, len(matrix)):
			if matrix[i] == matrix[j]:
				return False
	
	columns = [ColumnList(matrix, i) for i in range(len(matrix))]
	if not all(is_solved_line(column, size) for column in columns):
		return False
	# each column is unique
	for i in range(len(columns)):
		for j in range(i+1, len(columns)):
			if columns[i] == columns[j]:
				return False	

	return True

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
				
def generate_permutations(current, n, m, result):
    if n == 0 and m == 0:
        result.append(current)
        return
    
    if n > 0:
        generate_permutations(current + '0', n - 1, m, result)
    
    if m > 0:
        generate_permutations(current + '1', n, m - 1, result)

def get_permutations(n, m):
    permutations = []
    generate_permutations('', n, m, permutations)
    return permutations
    
def merge_row_with_permutation(row, permutation):
    result = []
    permutation_index = 0

    for char in row:
        if char == '.':
            if permutation_index < len(permutation):
                result.append(permutation[permutation_index])
                permutation_index += 1
            else:
                # If no more characters in permutation, keep the '.' as is
                result.append('.')
        else:
            result.append(char)

    return result
    
def possible_combinations(line, not_allowed_lines = []):
	counts = character_counts(line)
	permutations = get_permutations((len(line) // 2) - counts["0"], (len(line) // 2) - counts["1"])
	lines_to_test = [merge_row_with_permutation(line, permutation) for permutation in permutations]
	valid_lines = [line for line in lines_to_test if maximum_two(line) and line not in not_allowed_lines]	
	for i in range(len(line)):
		if line[i] == '.':
			first_valid_line = valid_lines[0]
			if all(valid_line[i] == first_valid_line[i] for valid_line in valid_lines):
				line[i] = first_valid_line[i]

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

def apply_techniques(line, other_lines):
	sides_double(line)
	empty_between_same(line)
	fill_line(line)
	possible_combinations(line, other_lines)

class Puzzle:
	def __init__(self, matrix):
		self.rows = matrix
		self.columns = [ColumnList(matrix, i) for i in range(len(matrix))]
	
	def apply_techniques(self):
		for row in self.rows:
			other_rows = [other_row for other_row in self.rows if other_row != row]
			apply_techniques(row, other_rows)
		
		for column in self.columns:
			other_columns = [list(other_column) for other_column in self.columns if other_column != column]
			apply_techniques(column, other_columns)      
	
def solve_puzzle(path):
	matrix = [list(line.strip()) for line in open(path).readlines()]
	
	print("Original binary puzzle :")
	for row in matrix:
		print("".join(row))
	
	step = 0
	previous_empty_count = matrix_empty_count(matrix)
	puzzle = Puzzle(matrix)
	
	while True:
		puzzle.apply_techniques()
		
		step = step + 1
				
		print("After " + str(step) + " step(s) :")
		for row in puzzle.rows:
			print("".join(row))
		
		empty_count = matrix_empty_count(matrix)
		if empty_count == 0 or empty_count == previous_empty_count:
			break
		previous_empty_count = empty_count
	return matrix
		
if __name__ == "__main__":
	path = sys.argv[1] if len(sys.argv) >= 2 else './puzzles/6x6_puzzle_easy_1.txt'
	solve_puzzle(path)
