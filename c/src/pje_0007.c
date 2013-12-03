#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int main() {
	long primes[10001];
	primes[0] = 2;
	primes[1] = 3;
	primes[10000] = 0;
	long n = 3;
	int t = 2;
	while (primes[10000] == 0) {
		n += 2;
		int x;
		bool isPrime = true;
		long max = (int) (ceil(sqrt(n)));
		for (x = 0; x < t && primes[x] <= max; x++) {
			if (n%primes[x] == 0)
				isPrime = false;
		}
		if (isPrime) {
			primes[t] = n;
			t++;
		}
	}
	printf("%ld\n", primes[10000]);
	return 0;
}
