from datetime import datetime, timedelta
date_A,date_B = input().split()
monday = 0
months = range(1,13)
for year in range(int(date_A),int(date_B)+1):
    for month in months:
        if datetime(year,month,1).strftime("%A") == "Monday":
            monday += 1
print(monday)