try:
    a, b = input().split()
    a = int(a)
    b = int(b)
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Denominator can't be 0")
except ValueError:
    print("Input should be an integer")