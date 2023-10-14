a = input()
b = a.lower()
k = ""
for i in range(len(a)):
    if b[i] == "a":
        k += "z"
    elif b[i] == " ":
        k += " "
    elif b[i] == "b":
        k += "y"
    elif b[i] == "c":
        k += "x"
    elif b[i] == "d":
        k += "w"
    elif b[i] == "e":
        k += "v"
    elif b[i] == "f":
        k += "u"
    elif b[i] == "g":
        k += "t"
    elif b[i] == "h":
        k += "s"
    elif b[i] == "i":
        k += "r"
    elif b[i] == "j":
        k += "q"
    elif b[i] == "k":
        k += "p"
    elif b[i] == "l":
        k += "o"
    elif b[i] == "m":
        k += "n"
    elif b[i] == "z":
        k += "a"
    elif b[i] == "y":
        k += "b"
    elif b[i] == "x":
        k += "c"
    elif b[i] == "w":
        k += "d"
    elif b[i] == "v":
        k += "e"
    elif b[i] == "u":
        k += "f"
    elif b[i] == "t":
        k += "g"
    elif b[i] == "s":
        k += "h"
    elif b[i] == "r":
        k += "i"
    elif b[i] == "q":
        k += "j"
    elif b[i] == "p":
        k += "k"
    elif b[i] == "o":
        k += "l"
    elif b[i] == "n":
        k += "m"
print(k)

