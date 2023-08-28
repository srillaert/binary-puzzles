from solve import *
from pathlib import Path

def test_character_counts_all_three_characters():
	result = character_counts(list("011..."))
	assert(result["0"] == 1)
	assert(result["1"] == 2)
	assert(result["."] == 3)

def test_character_counts_only_empty():
	result = character_counts(list(".."))
	assert(result["0"] == 0)
	assert(result["1"] == 0)
	assert(result["."] == 2)

def test_maximum_two():
	assert(maximum_two(list("1100")) == True)
	assert(maximum_two(list("001110")) == False) 

def test_matrix_empty_count():
	matrix = [["0", "."], [".", "0"]]
	assert(matrix_empty_count(matrix) == 2)

def test_permutations():
	permutations = get_permutations(1, 2)
	assert(permutations == ['011', '101', '110'])

def test_merge_row_with_permutation():
	row = list("0..1.0")
	permutation = '011'
	merged_string = merge_row_with_permutation(row, permutation)
	assert(merged_string == list("001110"))
	
def test_fill_line_with_1():
	line = list("0.")
	fill_line(line)
	assert(line == list("01"))

def test_fill_line_with_0():
	line = list(".1")
	fill_line(line)
	assert(line == list("01"))


def test_empty_between_same():
	line = list("0.01.1")
	empty_between_same(line)
	assert(line == list("010101"))


def test_sides_double_left():
	line = list("00....")
	sides_double(line)
	assert(line == list("001..."))

def test_sides_double_right():
	line = list("....11")
	sides_double(line)
	assert(line == list("...011"))

def test_sides_double_middle():
	line = list("..00..")
	sides_double(line)
	assert(line == list(".1001."))

def test_possible_combinations_1():
	line = list("0...0.")
	possible_combinations(line)
	assert(line == list("0...01"))

def test_possible_combinations_2():
	line = list("0..1.0")
	possible_combinations(line)
	assert(line == list("010110"))

def test_possible_combinations_3():
	line = list("1.0..1")
	possible_combinations(line)
	assert(line == list("100101"))

def test_possible_combinations_no_two_rows_same():
	line = list("1..010")
	not_allowed_lines = [
		list("101010"), # this row limits our combinations to 1
		list("001101"),
		list("010011"),
		list("...10."),
		list(".1010.")
	]
	possible_combinations(line, not_allowed_lines)
	assert(line == list("110010"))


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

def test_solve_puzzle():
	directory = Path('./puzzles/')
	for file_path in directory.iterdir():
		if file_path.is_file():
			solution = solve_puzzle(file_path.absolute())
			assert(is_solved_puzzle(solution))
