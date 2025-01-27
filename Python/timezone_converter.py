from datetime import datetime
import pytz

def convert_time(time_str, from_tz_str, to_tz_str):
    from_tz = pytz.timezone(from_tz_str)
    to_tz = pytz.timezone(to_tz_str)
    
    # Parse the time string into a datetime object
    naive_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    
    # Localize the naive datetime object to the from_tz
    localized_time = from_tz.localize(naive_time)
    
    # Convert the localized time to the target time zone
    converted_time = localized_time.astimezone(to_tz)
    
    return converted_time

# Example usage
time_to_convert = "2023-10-15 12:00:00"
from_timezone = "America/New_York"
to_timezone = "Europe/London"

converted_time = convert_time(time_to_convert, from_timezone, to_timezone)
print(f"Original time: {time_to_convert} in {from_timezone}")
print(f"Converted time: {converted_time.strftime('%Y-%m-%d %H:%M:%S')} in {to_timezone}")
