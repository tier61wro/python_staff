'''
#12.05.2020
Complete the function so that it returns the number of seconds that have elapsed between the start and end times given.

Tips:
The start/end times are given as Date (JS/CoffeeScript), DateTime (C#), Time (Nim), datetime(Python) and Time (Ruby) instances.
The start time will always be before the end time.
----
чтобы работать с датами
from datetime import datetime
перевод в юниксовый таймстемп:end.timestamp()
'''

from datetime import datetime

def elapsed_seconds(start, end):
	return int(end.timestamp() - start.timestamp())

start = datetime(2013, 1, 1, 0, 0, 1)
end = datetime(2013, 1, 1, 0, 0, 2)
print(elapsed_seconds(start,end))