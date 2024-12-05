from datetime import datetime
import pytz

timezone = pytz.timezone('Etc/GMT-6')
current_time = datetime.now(timezone)

print("Time:", current_time.strftime("%I:%M:%S %p"))
print("Date:", current_time.strftime("%d"))
print("Month:",current_time.strftime("%m"))
print("Year:", current_time.strftime("%Y"))
