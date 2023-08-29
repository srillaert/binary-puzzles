from basic import *

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

