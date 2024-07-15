import calendar

a = int(input("Enter the year: "))
b = int(input("Enter the month:"))

for i in range(1,b):
    new_s = calendar.month(a,i)
    print("\n")
    print(new_s)


