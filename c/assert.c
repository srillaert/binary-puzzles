#include<stdio.h>

void assert_char(char expected, char actual) {
	if (actual == expected) {
		printf("Passed.\n");
	} else {
		printf("Failed. Expected '%c' but got '%c'.\n", expected, actual);
	}
}

void assert_void_p(void* expected, void* actual) {
	if (actual == expected) {
		printf("Passed.\n");
	} else {
		printf("Failed. Expected '%p' but got '%p'.\n", expected, actual);
	}
}

void assert_size_t(size_t expected, size_t actual) {
	if (actual == expected) {
		printf("Passed.\n");
	} else {
		printf("Failed. Expected '%zu' but got '%zu'.\n", expected, actual);
	}
}

