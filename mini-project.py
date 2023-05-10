board = [' ' for i in range(9)]

def bord():
    print("-------------------")
    print("| ",board[0]," | ",board[1]," | ",board[2]," | ")
    print("-------------------")
    print("| ",board[3]," | ",board[4]," | ",board[5]," | ")
    print("-------------------")
    print("| ",board[6]," | ",board[7]," | ",board[8]," | ")
    print("-------------------")

def check():
    if board[0] == board[1] == board[2] != ' ' or board[3] == board[4] == board[5] != ' ' or board[6] == board[7] == board[8] != ' ' or board[0] == board[3] == board[6] != ' ' or board[1] == board[4] == board[7] != ' ' or board[2] == board[5] == board[8] != ' ' or board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        print("player",player,"wins!")
    else:
        if ' ' not in board:
            print("its a tie")
player = "X"
bord()         

for i in range(9):
    inputvalue = False
    while not inputvalue:
        a = input("enter the square no")
        x = a.isdigit()
        b = int(a)-1
        if b < 0 or b > 8 or x == False :
            print("Wrong input. should be numbers between 1 to 9")
        elif ' ' != board[b]:
            print("this square has already full")
        else:
            board[b] = player
            inputvalue = True
        bord()
        check()
    if player == "X":
        player = "O"
    else:
        player = "X" 
