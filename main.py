import datetime
# pull the current date and time
current_time = datetime.datetime.now()
# print the month, day, and year in 00/00/00 format
print(current_time.strftime("%m/%d/%y"))
# print the month, day, and year in 00/00/0000 format
print(current_time.strftime("%m/%d/%Y"))
# add the current time onto the date
print(current_time.strftime("%m/%d/%Y %I:%M:%S %p"))
