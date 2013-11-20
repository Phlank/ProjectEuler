import time
start_time = time.time()

#main
out = 0
day_of_week = 2									#sunday = 1
day_of_month = 1
days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = 1									#january = 1
year = 1901
while day_of_month < 31 or month < 12 or year < 2000:				#the last day of the period of tests
	day_of_week += 1
	if day_of_week > 7: day_of_week = 1					#going past saturday = sunday
	day_of_month += 1
	if year%4 == 0 and (year%100 != 0 or year%400 == 0):
		if day_of_month > days_of_months_leap[month-1]:
			day_of_month = 1
			month += 1
			if month > 12:						#going past december = january
				month = 1
				year += 1
	else:
		if day_of_month > days_of_months[month-1]:
			day_of_month = 1
			month += 1
			if month > 12:
				month = 1
				year += 1
	if day_of_week == 1 and day_of_month == 1: out += 1

out -= 1

elapsed_time = time.time() - start_time
print "%d found in %ss" % (out, elapsed_time)
