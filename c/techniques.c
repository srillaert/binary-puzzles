LineCount line_count_characters(Line line) {
	LineCount line_count = { 0, 0, 0 };
	for(int i=0; i<line.width; i++) {
		char ch = line_get(line, i);
		switch(ch) {
			case '.':
				line_count.unknown_count++;
				break;
			case '0':
				line_count.zero_count++;
				break;
			case '1':
				line_count.one_count++;
				break;
		}
	}
	return line_count;
}

void apply_count_technique(Line line) {
	LineCount line_count = line_count_characters(line);
	if (line_count.unknown_count > 0) {
		char fill_char = '\0';
		if (line_count.zero_count == line.width / 2) fill_char = '1';
		if (line_count.one_count == line.width / 2) fill_char = '0';
		if (fill_char != '\0') {
			for(int i = 0; i<line.width; i++) {
				char ch = line_get(line, i);
				if (ch == '.') {
					line_set(line, i, fill_char);
				} 
			}
		}
	}
}
