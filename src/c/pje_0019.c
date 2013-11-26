#include <stdio.h>

int main() {
	int dayOfWeek = 3, dayOfMonth = 1, month = 1, year = 1901, firstSundays = 0;
	int monthDays[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	int monthDaysLeap[12] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	while (dayOfMonth != 1 || month != 1 || year != 2001) {
		dayOfWeek++;
		if (dayOfWeek > 7)
			dayOfWeek = 1;
		dayOfMonth++;
		if (year%4 == 0 && (year%100 != 0 || year%400 == 0)) {
			if (dayOfMonth > monthDaysLeap[month-1]) {
				dayOfMonth = 1;
				month++;
				if (month > 12) {
					month = 1;
					year++;
				}
			}
		}
		else {
			if (dayOfMonth > monthDays[month-1]) {
				dayOfMonth = 1;
				month++;
				if (month > 12) {
					month = 1;
					year++;
				}
			}
		}
		if (dayOfWeek == 1 && dayOfMonth == 1)
			firstSundays++;
	}
	printf("%d\n", firstSundays);
	return 0;
}