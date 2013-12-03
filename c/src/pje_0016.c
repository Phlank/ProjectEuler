#include <stdio.h>

int main() {
	int SIZE = 400;
	int digits[SIZE];
	int save, carry, i, j;
	for (i = 0; i < SIZE; i++) {
		digits[i] = 0;
	}
	digits[SIZE-1] = 1;
	for (i = 0; i < 1000; i++) {
		carry = 0, save = 0;
		for (j = SIZE-1; j >= 0; j--) {
			int temp = digits[j]*2+carry;
			carry = temp/10;
			save = temp%10;
			digits[j] = save;
		}
	}
	int result = 0;
	for (i = 0; i < SIZE; i++) {
		result += digits[i];
	}
	printf("%d\n", result);
	return 0;
}