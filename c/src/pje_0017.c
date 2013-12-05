#include <stdio.h>

int main(void) {
	int letters = 0, c;
	FILE* f = fopen("../../txt/pje_0017_nums.txt", "r");
	while (fgetc(f) != EOF)
		letters++;
	printf("%d\n", letters);
}
