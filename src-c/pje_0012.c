#include <stdio.h>
#include <math.h>

//Returns the number of divisors of a given integer.
int numDivisors(int n) {
	int numberOfDivisors = 1;
	int temp = 0;
	while (n%2 == 0) {
		n = n/2;
		temp++;
	}
	numberOfDivisors *= temp+1;
	int k;
	for (k = 3; k < sqrt(n); k += 2) {
		temp = 0;
		while(n%k == 0) {
			n = n/k;
			temp++;
		}
		numberOfDivisors *= temp+1;
		if(n == 1)
			break;
	}
	if(n != 1)
		numberOfDivisors *= 2;
	return numberOfDivisors;
}

int main() {
	long long triangleNumber = 1;
	long n = 1;
	while (numDivisors(triangleNumber) < 500) {
		n++;
		triangleNumber += n;
	}
	printf("%lld\n", triangleNumber);
	return 0;
}