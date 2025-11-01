import datetime
# pull the current date and time
current_time = datetime.datetime.now()
# print the month, day, and year in 00/00/00 format
print(current_time.strftime("%m/%d/%y"))
# print the month, day, and year in January 1, 2019 format
print(current_time.strftime("%B %e, %Y"))
# add the current time onto the date
print(current_time.strftime("%B %e, %Y %l:%M:%S %p"))

