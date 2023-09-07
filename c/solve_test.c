#include<math.h>
#include<string.h>
#include "assert.c"
#include "matrix.c"
#include "techniques.c"
#include "matrix_test.c"
#include "techniques_test.c"

int main(void) {
	matrix_create_test(); 

	line_get_test_column();
	line_get_test_row();

	apply_count_technique_test();

	return 0;
}
