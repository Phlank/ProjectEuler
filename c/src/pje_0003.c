#include <stdio.h>

int main() {
	long long number = 600851475143;
	long long i = 3;
	while (i < number) {
		if (number%i == 0)
			number /= i;
		else
			i += 2;
	}
	printf("%lld\n", i);
	return 0;
}
