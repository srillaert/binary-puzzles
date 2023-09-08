#include<stdio.h>
#include<string.h>

int failed = 0;
int passed = 0;

void assert_char(char expected, char actual) {
	if (actual == expected) {
		passed++;
		printf("Passed.\n");
	} else {
		failed++;
		printf("Failed. Expected '%c' but got '%c'.\n", expected, actual);
	}
}

void assert_void_p(void* expected, void* actual) {
	if (actual == expected) {
		passed++;
		printf("Passed.\n");
	} else {
		failed++;
		printf("Failed. Expected '%p' but got '%p'.\n", expected, actual);
	}
}

void assert_size_t(size_t expected, size_t actual) {
	if (actual == expected) {
		passed++;
		printf("Passed.\n");
	} else {
		failed++;
		printf("Failed. Expected '%zu' but got '%zu'.\n", expected, actual);
	}
}

void assert_str(char* expected, char* actual) {
	if (!strcmp(actual, expected)) {
		passed++;
		printf("Passed.\n");
	} else {
		failed++;
		printf("Failed. Expected '%s' but got '%s'.\n", expected, actual);
	}
}

void print_test_summary() {
	if (failed != 0) {
		printf("%d failed, ", failed);
	}
	printf("%d passed\n", passed);
}
