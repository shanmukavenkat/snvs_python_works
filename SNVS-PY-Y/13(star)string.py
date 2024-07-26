## string
## length odd ayite square the length
## else cube it
def ntr(n):
    k = len(n)
    if (k % 2 != 0):
        print(k ** 2)

    else:
        print(k ** 3)
    return " "
n = input()
print(ntr(n))
