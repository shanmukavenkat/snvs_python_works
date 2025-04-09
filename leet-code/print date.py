from datetime import datetime ,timedelta

date_ti = input()
date_obj = datetime.strptime(date_ti, "%d %b %Y")
print(date_obj-timedelta(days=1))
print(date_obj+timedelta(days=0))
print(date_obj+timedelta(days=1))