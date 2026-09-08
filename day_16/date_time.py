from datetime import datetime


# Day 16: Date and Time

# Exercises

# 1. Use the datetime module to retrieve today's year, month, and day, the current
# hour and minute, and the Unix timestamp.
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(now)
print(day)
print(month)
print(year)
print(hour)
print(minute)
print(timestamp)


# 2. Turn the current date and time into a string with the format below:
# "%m/%d/%Y, %H:%M:%S"
time_one = now.strftime('%m/%d/%Y, %H:%M:%S')
print(time_one)

# 3. Parse the string '5 December, 2019' into a datetime object.
date_string = '5 December, 2019'
date_object = datetime.strptime(date_string, '%d %B, %Y')
print(date_object)

# 4. Find how much time remains from now until January 1 of next year.
new_year = datetime(year=now.year + 1, month=1, day=1)
time_left = new_year - now
print('Time left for new year: ',time_left)

# 5. Find the elapsed time from January 1, 1970 to the present.
t1 = datetime(year = 1970, month = 1, day = 1, hour = 0, minute = 0, second = 0)
t2 = now
diff = t2 - t1
print('The elapsed time is: ',diff)

# 6. Describe practical uses for the datetime module. Consider analyzing data over
# time, recording when application events happen, and dating blog entries.
# We can use datetime to timestamp log entries and logins, work with code-change timestamps, and calculate how much time has passed since those events.
