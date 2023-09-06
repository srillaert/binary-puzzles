#include "assert.c"
#include<math.h>
#include<stdio.h>
#include<string.h>

typedef struct Matrix {
	char* matrix_array;
	size_t width;
} Matrix;

typedef struct Line {
	char* base_address;
	int multiplier;
	size_t width;
} Line;

Matrix matrix_create(char* matrix_array) {
	size_t matrix_len = strlen(matrix_array);
	size_t width = (size_t)sqrt((double)matrix_len);
	Matrix matrix = { matrix_array, width };
	return matrix;
}

void matrix_create_test() {
	char puzzle[] = "..0.";

	Matrix matrix = matrix_create(puzzle);

	assert_void_p((void*)puzzle, (void*)matrix.matrix_array);
	assert_size_t(2, matrix.width);
}

char line_get(Line line, int index) {
	return *(line.base_address + index * line.multiplier);
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

int main(void) {
	matrix_create_test(); 

	line_get_test_column();
	line_get_test_row();

	return 0;
}
