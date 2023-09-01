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
