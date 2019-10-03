from math import floor
board=[[' ' for i in range(3)] for j in range(3)]
round=0
def check():
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i]: 
            print(board[0][i]+' is the winner')
            quit()
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]: 
            print(board[i][0]+' is the winner')
            quit()
    if board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0]:
        print(board[1][1]+' is the winner')
        quit()
def draw():
    for i,j in enumerate(board):
        print(j,end= ' ')
        if (i+1)%3: print()
    print()
def move(a,b):
    global board,round
    if board[a][b]!=' ':
        print("Position Occupied")
        return
    board[a][b]= 'X' if round%2 else 'O'
    round+=1
def turn():
    print("Turn " + str(floor(round/2) + 1) + "\n Player " + str(round%2 + 1),end="\n")
    a=int(input("  Enter column for " + ("X " if round%2 else "O ")))
    b=int(input("  Enter row for " + ("X " if round%2 else "O ")))
    move(a,b)
    draw()
    if round/2>=3:
        check()
print("LET THE GAMES BEGIN ")
while True:
    if round>=9: 
        print('tie')
        quit()
    turn()