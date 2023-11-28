import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Get the date and time one year from now
one_year_from_now = current_datetime + datetime.timedelta(days=365)

# Format the datetime objects as strings
current_datetime_str = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
one_year_from_now_str = one_year_from_now.strftime('%Y-%m-%d %H:%M:%S')

print("Current Date and Time:", current_datetime_str)
print("Date and Time One Year from Now:", one_year_from_now_str)
