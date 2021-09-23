import datetime, pytz

tz_old = "Correct pytz timezone name, say, Europe/London"
tz_new = "example: America/Toronto"

# Convert them into PyTZ timezone objects.
tz_old = pytz.timezone(tz_old)
tz_new = pytz.timezone(tz_new)

# Set the timestamp you want.
ts = datetime.datetime(2021, 1, 1, 0, 0, 0)

# Localize the timestamp to the old timestamp and then convert to the new one.
print("from {}\n  to {}".format(tz_old.localize(ts), tz_old.localize(ts).astimezone(tz_new)))
