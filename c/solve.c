#include<math.h>
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

char line_get(Line line, int index) {
	return *(line.base_address + index * line.multiplier);
}

