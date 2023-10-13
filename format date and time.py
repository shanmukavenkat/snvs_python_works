from datetime import datetime
date_format = "%b %d %Y %I:%M%p"
date_string = input()
date_obj = datetime.strptime(date_string, date_format)
out_put = date_obj.strftime("%d/%m/%Y %H:%M:%S")
print(out_put)