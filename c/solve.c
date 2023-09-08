#include<stdio.h>
#include<stdlib.h>

int main(int argc, char* argv[]) {
	char* path = argc < 2 ? "../puzzles/6x6_puzzle_easy_1.txt" : argv[1];

	FILE* stream = fopen(path, "r");
	if (stream == NULL) {
		printf("%s: cannot open '%s' for reading\n", argv[0], path);
		return 1;
	}
	printf("opened '%s'\n", path);
	
	int width = 0;
	char c = fgetc(stream);
	while (c != '\n' && c != EOF) {
		width++;
		c = fgetc(stream);
	}
	printf("Puzzle is %d width\n", width);
	
	int puzzle_array_size = width * width;
	char* puzzle_array = malloc(sizeof(char) * puzzle_array_size);
	
	rewind(stream);
	int i=0;
	while((c = fgetc(stream)) != EOF) {
		if(c == '.' || c == '0' || c == '1') {
			puzzle_array[i++] = c;
		}
		if(i > puzzle_array_size) {
			printf("More elements that the expected %dx%d array\n", width, width);
			return 1;
		}
	}
	if (i < puzzle_array_size) {
			printf("Only found %d elements, that is less than the expected %dx%d array\n", i, width, width);
			return 1;
	}

	fclose(stream);

	return 0;
}
