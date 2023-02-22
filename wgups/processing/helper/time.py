from datetime import datetime, timedelta


# Time complexity: O(1)
# Space complexity: O(1)

# Convert a string to a datetime.time object and return.
def str_to_time(time):
    return datetime.strptime(time, '%I:%M %p').time()


# Time complexity: O(1)
# Space complexity: O(1)

# Convert a datetime.time object to a string and return.
def time_to_str(time):
    return time.strftime('%I:%M %p')


# Time complexity: O(1)
# Space complexity: O(1)

# Convert distance traveled to minutes traveled and return.
def miles_to_minutes(mph, miles):
    return miles/(mph/60)


# Time complexity: O(1)
# Space complexity: O(1)

# Convert distance traveled to arrival time and return.
def get_time(mph, miles, time):
    minutes = miles_to_minutes(mph, miles)
    init_date = datetime(100, 1, 1, time.hour, time.minute, time.second)
    init_date = init_date + timedelta(minutes=minutes)
    return init_date.time()


# Time complexity: O(1)
# Space complexity: O(1)

# Add the number of minutes to the time and return the new time.
def add_minutes(minutes, time):
    init_date = datetime(100, 1, 1, time.hour, time.minute, time.second)
    init_date = init_date + timedelta(minutes=minutes)
    return init_date.time()


# Time complexity: O(1)
# Space complexity: O(1)

# Determine what the difference in minutes is between two separate times and return.
def time_difference(time1, time2):
    init_date1 = datetime(100, 1, 1, time1.hour, time1.minute, time1.second)
    init_date2 = datetime(100, 1, 1, time2.hour, time2.minute, time2.second)
    time_delta = abs(init_date1 - init_date2)
    return time_delta.total_seconds()/60
