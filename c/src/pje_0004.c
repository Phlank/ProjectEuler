#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isPalindrome(long n) {
	long temp = n;
	long reverse = 0;
	while (temp != 0) {
		reverse = reverse*10+temp%10;
		temp /= 10;
	}
	if (n == reverse)
		return true;
	else
		return false;
}


int main() {
	int a, b;
	long c;
	long highest = 0;
	for (a = 100; a < 1000; a++) {
		for (b = 100; b < a; b++) {
			c = a*b;
			if (highest < c) {
				if (isPalindrome(c) == true)
					highest = c;
			}
		}
	}
	printf("%ld\n", highest);
	return 0;
}
