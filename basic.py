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
