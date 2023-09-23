import sys
from techniques import *

def apply_techniques(line, other_lines):
	sides_double(line)
	empty_between_same(line)
	fill_line(line)
	possible_combinations(line, other_lines)
	
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
			
def matrix_empty_count(matrix):
	return sum(line.count(".") for line in matrix)

max_steps = 14 * 14 # Every step an element needs to be found, otherwise we are stuck. The biggest puzzles on binarypuzzle.com have 14 * 14 elements.
	
def solve_puzzle(path):
	matrix = [list(line.strip()) for line in open(path).readlines()]
	
	print("Original binary puzzle :")
	for row in matrix:
		print("".join(row))
	
	step = 0
	previous_empty_count = matrix_empty_count(matrix)
	puzzle = Puzzle(matrix)
	
	while step < max_steps:
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
	if len(sys.argv) <= 1:
		print("Usage: " + sys.argv[0] + " FILE [MAX_STEPS]");
		exit(0)
	path = sys.argv[1]
	if len(sys.argv) >= 3:
		max_steps = int(sys.argv[2]) 	
	solve_puzzle(path)
