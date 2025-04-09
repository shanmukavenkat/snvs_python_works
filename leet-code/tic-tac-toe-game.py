A = []
for i in range(3):
    a = input().split()
    A.append(a)

if ((A[0][0] == "O" and A[0][1] == "O" and A[0][2] == "O") or (A[1][0] == "O" and A[1][1] == "O" and A[1][2] == "O") or
    (A[2][0] == "O" and A[2][1] == "O" and A[2][2] == "O") or (A[0][0] == "O" and A[1][0] == "O" and A[2][0] == "O") or
    (A[0][1] == "O" and A[1][1] == "O" and A[2][1] == "O") or (A[0][2] == "O" and A[1][2] == "O" and A[2][2] == "O") or
    (A[0][0] == "O" and A[1][1] == "O" and A[2][2] == "O") or (A[0][2] == "O" and A[1][1] == "O" and A[2][2] == "O")):
    print("Abhinav Wins")
elif ((A[0][0] == "X" and A[0][1] == "X" and A[0][2] == "X") or (A[1][0] == "X" and A[1][1] == "X" and A[1][2] == "X")or
    (A[2][0] == "X" and A[2][1] == "X" and A[2][2] == "X") or (A[0][0] == "X" and A[1][0] == "X" and A[2][0] == "X") or
    (A[0][1] == "X" and A[1][1] == "X" and A[2][1] == "X") or (A[0][2] == "X" and A[1][2] == "X" and A[2][2] == "X") or
    (A[0][0] == "X" and A[1][1] == "X" and A[2][2] == "X") or (A[0][2] == "X" and A[1][1] == "X" and A[2][2] == "X")):
    print("Anjali Wins")
else:
    print("Tie")
