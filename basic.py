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
