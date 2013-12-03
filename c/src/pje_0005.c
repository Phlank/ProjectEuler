#include <stdio.h>
#include <stdbool.h>

int power(int a, int b) {
	long long total = 1;
	int x;
	for (x = 0; x < b; x++)
		total *= a;
	return total;
}

bool isPrime(int i) {
	if (i < 2)
		return false;
	if (i == 2)
		return true;
	bool primality = true;
	int x;
	for (x = 2; x < i && primality; x++) {
		if (i%x == 0)
			primality = false;
	}
	return primality;
}

int main() {
	int i;
	long long multiple = 1;
	for (i = 2; i <= 20; i++) {
		if (isPrime(i)) {
			int m;
			int n;
			for (n = 1; power(i, n) < 20; n++)
				m = n;
			multiple *= power(i, m);
		}
	}
	printf("%lld\n", multiple);
	return 0;
}
