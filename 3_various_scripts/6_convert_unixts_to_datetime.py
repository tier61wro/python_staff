from datetime import datetime
ts = int('1565693882')

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
#print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S'))
