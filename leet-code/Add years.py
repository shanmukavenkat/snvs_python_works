from datetime import datetime ,timedelta
g_date ="%b %d %Y"
u_date = input()
a_years = int(input())
delta = timedelta(days=365*a_years)
date_obj = datetime.strptime(u_date, g_date)
print(date_obj+delta)
