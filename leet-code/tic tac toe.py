a = input().split()
b = input().split()
c = input().split()

input_list = [a, b, c]
givenitems = "OX"
winner = False
for i in givenitems:
    for j in range(3):
        if a[j] == i and b[j] == i and c[j] == i:
            winner = True
            winner_item = i
        elif a[0] == i and b[1] == i and c[2] ==i:
            winner = True
            winner_item = i
        elif a[2] ==i and b[1] == i and c[0] == i:
            winner = True
            winner_item = i
    for inputs in input_list:
        if inputs == [i,i,i]:
            winner = True
            winner_item = i
if winner:
    if winner_item == "O":
        print("Abhinav Wins")
    else:
        print("Anjali Wins")
else:
    print("Tie")


