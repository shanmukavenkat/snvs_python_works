from datetime import datetime as dt
from datetime import timedelta as td
d_format ="%b %d %Y"
d_1 = input()
d_2 = input()
delta = td(days=0)
date_format = dt.strptime(d_1, d_format)
date_format2 = dt.strptime(d_2, d_format)
diff = date_format2 - date_format
for i in range(diff.days+1):
    print((date_format)+td(days=i))
