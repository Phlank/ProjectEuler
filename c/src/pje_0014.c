#include <stdio.h>

int main() {
	long long longest = 0, n = 0;
	long long i;
	long collatz = 0;
	for (i = 1; i < 1000000; i++) {
		n = i;
		int t = 0;
		while (n != 1) {
			if (n%2 == 0)
				n /= 2;
			else
				n = n*3+1;
			t++;
		}
		if (collatz < t) {
			collatz = t;
			longest = i;
		}
	}
	printf("%lld\n", longest);
	return 0;
}