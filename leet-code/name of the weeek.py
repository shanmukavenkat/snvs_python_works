from datetime import datetime as dt

d_input = input()
d_format = "%b %d %Y"
d = dt.strptime(d_input, d_format)
date_A = d.strftime("%A")
print(date_A)