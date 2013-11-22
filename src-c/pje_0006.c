#include <stdio.h>

int main() {
	long long sumOfSquares = 0;
	long long squareOfSums = 0;
	int i;
	for (i = 1; i <= 100; i++) {
		sumOfSquares += i*i;
		squareOfSums += i;
	}
	squareOfSums *= squareOfSums;
	squareOfSums -= sumOfSquares;
	printf("%lld\n", squareOfSums);
	return 0;
}
