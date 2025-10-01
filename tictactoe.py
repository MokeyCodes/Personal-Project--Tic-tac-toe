#
board = [1, 2, 3, 
         4, 5, 6, 
         7, 8, 9, ]
turn = True

def board_Display():
    print(f"{board[0]}  |  {board[1]}  |  {board[2]}")
    print(f"{board[3]}  |  {board[4]}  |  {board[5]}")
    print(f"{board[6]}  |  {board[7]}  |  {board[8]}")

def turn_Picked(num, too):
    if too == True:
        try:
            index = board.index(num)
        except:
            print("Number not found, choose again.")
            board_Display()
            turn_For(too)
        if board[index] != "X" and board[index] != "O":
            board[index] = "X"
            board_Display()
            if check_Rows() == True:
                exit()
            elif check_Columns() == True:
                exit()
            elif check_Diagonal() == True:
                exit()
            elif check_Tie() == True:
                exit()
            else:
                too = not too
                turn_For(too)
    if too == False:
        try:
            index = board.index(num)
        except:
            print("Number not found, choose again.")
            board_Display()
            turn_For(too)
        if board[index] != "X" and board[index] != "O":
            board[index] = "O"
            board_Display()
            if check_Rows() == True:
                exit()
            elif check_Columns() == True:
                exit()
            elif check_Diagonal() == True:
                exit()
            elif check_Tie() == True:
                exit()
            
            else:
                too = not too
                turn_For(too)


    


def turn_For(t):
    if t == True:
        table_Input = int(input("\nX's turn, choose a number to replace with X.\n"))
        turn_Picked(table_Input,t)
    if t == False:
        table_Input = int(input("\nO's turn, choose a number to replace with O.\n"))
        turn_Picked(table_Input,t)
    

def check_Rows():
    if board[0] == board[1] == board[2]:
        print(board[0] + " has won.")
        return True
    
    elif board[3] == board[4] == board[5]:
        print(board[3] + " has won.")
        return True
    
    elif board[6] == board[7] == board[8]:
        print(board[6] + " has won.")
        return True
    else:
        return False

def check_Columns():
    if board[0] == board[3] == board[6]:
        print(board[0] + " has won.")
        return True
    
    elif board[1] == board[4] == board[7]:
        print(board[1] + " has won.")
        return True
    
    elif board[2] == board[5] == board[8]:
        print(board[2] + " has won.")
        return True
    else:
        return False
    
def check_Diagonal():
    if board[0] == board[4] == board[8]:
        print(board[0] + " has won.")
        return True
    
    elif board[6] == board[4] == board[2]:
        print(board[6] + " has won.")
        return True
    
    else:
        return False

def check_Tie():
    if check_Rows() == check_Columns() == check_Diagonal() == False and check_For_Integers() == False:
        print("It is a tie.")
        return True


def check_For_Integers():
    for num in board:
        if type(num) is int:
            return True
    return False


board_Display()
turn_For(turn)



# board
# display board
# play game
# ensure move is valid
# check win
    # check rows, columns, diagonals
# check tie
# flip players