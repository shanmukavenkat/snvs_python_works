
class Month:
    def getMonthName(self, monthNumber):
        if monthNumber == 1:
            print("January")
        elif monthNumber == 2:
            print("February")
        elif monthNumber == 3:
            print("March")
        elif monthNumber == 4:
            print("April")
        elif monthNumber == 5:
            print("May")
        elif monthNumber == 6:
            print("June")
        elif monthNumber == 7:
            print("July")
        elif monthNumber == 8:
            print("August")
        elif monthNumber == 9:
            print("September")
        elif monthNumber == 10:
            print("October")
        elif monthNumber == 11:
            print("November")
        elif monthNumber == 12:
            print("December")
        else:
            print("Invalid input!")
        pass
month = Month()
monthNumber = int(input("Enter month number: "))
month.getMonthName(monthNumber)
