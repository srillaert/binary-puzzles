#include "assert.c"
#include "techniques.c"

void matrix_create_test() {
	char puzzle[] = "..0.";

	Matrix matrix = matrix_create(puzzle);

	assert_void_p((void*)puzzle, (void*)matrix.matrix_array);
	assert_size_t(2, matrix.width);
}

void line_get_test_column() {
	char puzzle[] = "..0.";

	Line first_column = { puzzle, 2, 2 };

	assert_char('.', line_get(first_column, 0));
	assert_char('0', line_get(first_column, 1));
}

void line_get_test_row() {
	char puzzle[] = "..0.";

	Line second_row = { puzzle + 2, 1, 2 };

	assert_char('0', line_get(second_row, 0));
	assert_char('.', line_get(second_row, 1));
}

void apply_count_technique_test() {
	char actual[] = ".1";
	Line line = { actual, 1, 2 };

	apply_count_technique(line);

	assert_str("01", actual);
}

int main(void) {
	matrix_create_test(); 

	line_get_test_column();
	line_get_test_row();

	apply_count_technique_test();

	return 0;
}
