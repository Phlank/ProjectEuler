#include <stdio.h>

int main() {
	FILE* f;
	f = fopen("../txt/pje_0008_n.txt", "r");
	long highest = 0;
	int c;
	int nums[5] = {0, 0, 0, 0, 0};
	while ((c = fgetc(f)) != EOF) {
		c -= 48;
		nums[0] = nums[1];
		nums[1] = nums[2];
		nums[2] = nums[3];
		nums[3] = nums[4];
		nums[4] = c;
		if (highest < nums[0]*nums[1]*nums[2]*nums[3]*nums[4]) 
			highest = nums[0]*nums[1]*nums[2]*nums[3]*nums[4];
	}
	fclose(f);
	printf("%ld\n", highest);
	return 0;
}
