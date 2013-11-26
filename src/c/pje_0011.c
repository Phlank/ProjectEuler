#include <stdio.h>

int main() {
	FILE* f = fopen("../../txt/pje_0011_grid.txt", "r");
	int grid[20][20];
	int i, j;
	long highest = 0;
	for (i = 0; i < 20; i++) {
		for (j = 0; j < 20; j++) {
			fscanf(f, "%d", &grid[i][j]);
		}
	}
	//Horizontal
	for (i = 0; i < 20; i++) {
		for (j = 0; j < 17; j++) {
			long temp = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3];
			if (highest < temp)
				highest = temp;
		}
	}
	//Vertical
	for (i = 0; i < 17; i++) {
		for (j = 0; j < 20; j++) {
			long temp = grid[i][j]*grid[i+1][j]*grid[i+2][j]+grid[i+3][j];
			if (highest < temp)
				highest = temp;
		}
	}
	//Ul-Dr Diagonal
	for (i = 0; i < 17; i++) {
		for (j = 0; j < 17; j++) {
			long temp = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3];
			if (highest < temp)
				highest = temp;
		}
	}
	//Dl-Ur Diagonal
	for (i = 3; i < 20; i++) {
		for (j = 0; j < 17; j++) {
			long temp = grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3];
			if (highest < temp)
				highest = temp;
		}
	}
	printf("%ld\n", highest);
	return 0;
}