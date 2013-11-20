#include <stdio.h>
#include <stdlib.h>

int main(int argv, char* argc) {
	int o = 0;
	int i;
	for (i = 3; i < 1000; i++) {
		if (i%3 == 0)
			o += i;
		else if (i%5 == 0)
			o += i;
	}
	printf("%d\n", o);
	return 0;
}
