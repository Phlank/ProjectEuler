#include <stdio.h>

int main() {
	FILE* f = fopen("../txt/pje_0013_nums.txt", "r");
	int c, nums[100][50], j, k;
	for (j = 0; j < 100; j++) {
		/* There is a return character at the end
		of each line, so we have to add one to the
		bounds for the second loop to read in the
		entire file */
		for (k = 0; k < 51; k++) {
			c = fgetc(f);
			if (c != 10 && c != 13) {\
				nums[j][k] = c-48;
			}
		}
	}
	fclose(f);
	int carry = 0;
	int sum[50];
	for (k = 49; k >= 0; k--) {
		int column = carry;
		for (j = 0; j < 100; j++) {
			column += nums[j][k];
		}
		//Finds the amount to carry over and the amount to save
		carry = column/10;
		int remaining = column%10;
		if (k != 0)
			sum[k] = remaining;
		else
			sum[k] = column;
	}
	//Find the number of digits in the first column
	int length = 0;
	int temp = sum[0];
	while (temp/10 > 0) {
		length++;
		temp /= 10;
	}
	for (k = 0; k < 10-length; k++) {
		printf("%d", sum[k]);
	}
	printf("\n");
}