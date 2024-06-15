from datetime import datetime

date_str = input()
data_obj = datetime.strptime(date_str, '%d-%b-%Y')
print(data_obj)


from datetime import datetime

date_str = input()
str_in = "%d %b %Y"
data_obj = datetime.strptime(date_str, str_in)
print(data_obj)