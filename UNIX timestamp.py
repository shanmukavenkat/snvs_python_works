import datetime
zero = datetime.datetime(1970,1,1)
d = int(input())
seconds = datetime.timedelta(seconds=d)
result_time = zero+seconds
dt_format = "%Y-%m-%d %H:%M:%S"
print(result_time.strftime(dt_format))

