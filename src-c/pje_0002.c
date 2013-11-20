#include <stdio.h>
#include <stdlib.h>

int main(int argv, char* argc) {
	int a, b, c, output;
	static const int MAX = 4000000;
	a = 1;
	b = 2;
	c = 3;
	output = 2;
	while (c < MAX) {
		c = a+b;
		if (c%2 == 0)
			output += c;
		a = b;
		b = c;
	}
	printf("%d\n", output);
	return 0;
}
