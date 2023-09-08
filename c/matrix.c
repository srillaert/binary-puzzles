typedef struct Matrix {
	char* matrix_array;
	size_t width;
} Matrix;

typedef struct Line {
	char* base_address;
	int multiplier;
	size_t width;
} Line;

typedef struct LineCount {
	int unknown_count;
	int zero_count;
	int one_count;
} LineCount;

Matrix matrix_create(char* matrix_array) {
	size_t matrix_len = strlen(matrix_array);
	size_t width = (size_t)sqrt((double)matrix_len);
	Matrix matrix = { matrix_array, width };
	return matrix;
}

void matrix_print(Matrix matrix, FILE *stream) {
	for(int i=0; i<matrix.width; i++) {
		for(int j=0; j<matrix.width; j++) {
			fputc(matrix.matrix_array[i*matrix.width+j], stream);
		}
		fputc('\n', stream);
	}
}

char line_get(Line line, int index) {
	return line.base_address[index * line.multiplier];
}

void line_set(Line line, int index, char ch) {
	line.base_address[index * line.multiplier] = ch;
}
