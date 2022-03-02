#PORTFOLIO PROJECT 3
# Tic Tac Tow game

print("Instructions to play:"
      "\nPlayer-1 is given the symbol of 'X'"
      "\nPlayer-2 is given the symbol of 'O'"
      "\nType the row,column to place your symbol eg: '1,1' , '1,2' \n")

li=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def print_list(li):
    print(
        '- - - - - '
        f'\n{li[0][0]} | {li[0][1]} | {li[0][2]}'
        f'\n{li[1][0]} | {li[1][1]} | {li[1][2]}'
        f'\n{li[2][0]} | {li[2][1]} | {li[2][2]}'
        '\n- - - - -'
    )

def check_place(i,j):
    if li[i][j]=='X' or li[i][j]=='O':
        return False
    else:
        return True

game_not_over = True

def check_win():
    global game_not_over
    for n in range(3):
        if li[0][n] == li[1][n] ==li[2][n] and li[0][n]!=' ':
            print(f"Winner is {li[0][n]}")
            game_not_over = False
            break
        elif li[n][0]==li[n][1]==li[n][2] and li[n][0]!=' ':
            print(f'Winner is {li[n][0]}')
            game_not_over = False
            break
        elif li[0][0]==li[1][1]==li[2][2] or li[0][2]==li[1][1]==li[2][0] and li[1][1]!=" ":
            print(f'Winner is {li[1][1]}')
            game_not_over = False
            break
        else:
            continue

n=1

while game_not_over :
    if n%2!=0:
        p = input("Player-1: Enter the row,column to place 'X': ")
        i,j=map(int,p.split(","))
        i = int(i) - 1
        j = int(j) - 1
        li[i][j]="X"

    else:
        p = input("Player-2: Enter the row,column to place 'O': ")
        i,j = map(int, p.split(","))
        i = int(i) - 1
        j = int(j) - 1
        li[i][j] = "O"

    n+=1
    print_list(li)
    check_win()
