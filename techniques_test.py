from techniques import *

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


