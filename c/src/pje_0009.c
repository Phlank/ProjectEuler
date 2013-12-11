#include <stdio.h>

int main() {
	int a, b, c;
	long long product = 0;
	for (a = 998; a >= 2 && product == 0; a--) {
		for (b = a; b >= 2 && product == 0; b--) {
			for (c = b; c >= 2 && product == 0; c--) {
				if (a+b+c == 1000) {
					if (a > b && a > c) {
						if (b*b+c*c == a*a)
							product = a*b*c;
					}
					else if (b > a && b > c) {
						if (a*a+c*c == b*b)
							product = a*b*c;
					}
					else if (c > a && c > b) {
						if (a*a+b*b == c*c)
							product = a*b*c;
					}
				}
			}
		}
	}
	printf("%lld\n", product);
	return 0;
}
