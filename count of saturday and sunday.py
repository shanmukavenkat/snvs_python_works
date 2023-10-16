from datetime import datetime, timedelta

given_date1 = input()
given_date2 = input()

start_date = datetime.strptime(given_date1, "%d %b %Y")
end_date = datetime.strptime(given_date2, "%d %b %Y")

date_diff = abs(end_date - start_date)  # Use abs() to get the absolute difference

total_days = date_diff.days

saturdays = 0
sundays = 0

for i in range(total_days + 1):
    delta = timedelta(days=i)
    n = start_date + delta
    nF = n.strftime("%A")

    if nF == "Saturday":
        saturdays += 1
    elif nF == "Sunday":
        sundays += 1

print("Saturdays: {}".format(saturdays))
print("Sundays: {}".format(sundays))
