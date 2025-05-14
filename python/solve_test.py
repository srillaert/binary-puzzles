from solve import *
from pathlib import Path

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

def test_column_list_getitem():
	matrix = [[1, 2], [3, 4]]
	
	first_column = ColumnList(matrix, 0)
	assert(first_column[0] == 1)
	assert(first_column[1] == 3)

	second_column = ColumnList(matrix, 1)
	assert(second_column[0] == 2)
	assert(second_column[1] == 4)

def test_column_list_len():
	matrix = [[1], [3]]
	
	first_column = ColumnList(matrix, 0)
	
	assert(len(first_column) == 2)

def test_column_list_len():
	matrix = [[0, 0], [0, 0]]
	
	first_column = ColumnList(matrix, 0)
	first_column[0] = 1
	first_column[1] = 3

	second_column = ColumnList(matrix, 1)
	second_column[0] = 2
	second_column[1] = 4
	
	assert(matrix == [[1, 2], [3, 4]])

def test_matrix_empty_count():
	matrix = [["0", "."], [".", "0"]]
	assert(matrix_empty_count(matrix) == 2)

def test_solve_puzzle():
	directory = Path(__file__).resolve().parent.parent / 'puzzles'
	for file_path in directory.iterdir():
		if file_path.is_file():
			solution = solve_puzzle(file_path.absolute())
			assert(is_solved_puzzle(solution))
