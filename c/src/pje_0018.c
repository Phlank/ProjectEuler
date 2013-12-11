#include <stdio.h>

int main() {
	FILE* f = fopen("../../txt/pje_0018_pyramid.txt", "r");
	int MAX = 15;
	int pyramid[MAX][MAX], i = 0, j = 0;
	for (i = 0; i < MAX; i++) {
		for (j = 0; j <= i; j++) {
			fscanf(f, "%d", &pyramid[i][j]);
		}
	}
	for (i = MAX-2; i >= 0; i--) {
		for (j = 0; j <= i; j++) {
			if (pyramid[i+1][j] > pyramid[i+1][j+1])
				pyramid[i][j] += pyramid[i+1][j];
			else
				pyramid[i][j] += pyramid[i+1][j+1];
		}
	}
	printf("%d\n", pyramid[0][0]);
	return 0;
}