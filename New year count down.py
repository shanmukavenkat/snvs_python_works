from datetime import datetime,timedelta

given_date1_time = input()

start_year = datetime.strptime(given_date1_time, "%b %d %Y %I:%M %p")

end_year = (start_year.year )+ 1

end_date = datetime(year = end_year, month = 1, day = 1)

differ = end_date - start_year

total_seconds = differ.total_seconds()

hours = int(total_seconds//3600)

minutes = int((total_seconds-(hours*3600))//60)

print("{} hours {} minutes".format(hours,minutes))