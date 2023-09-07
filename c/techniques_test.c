void apply_count_technique_test() {
	char actual[] = ".1";
	Line line = { actual, 1, 2 };

	apply_count_technique(line);

	assert_str("01", actual);
}

