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