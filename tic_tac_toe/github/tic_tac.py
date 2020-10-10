#global variable 

currentPlayer='X'
game_is_still_going=True 
winner=None 


board=['-' ,'-' ,'-',
       '-' ,'-' ,'-',
       '-' ,'-' ,'-']
def displayBoard():
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print("\n")


def game():
    


    displayBoard()


    #if the value of game is still going is true the loop work
    while game_is_still_going:



        Playerhandle(currentPlayer)


        check_if_game_over()


        flip_player()
    
    
    
    if winner == 'X' or winner == 'O':
        print(winner+"  :won the game")
    elif winner == None:
        
        print("tie")





def Playerhandle(player):
    print(player+' turn')
    position=raw_input("enter the number between 1-9: ")

    valid=False 
#character except 1-9 then as the input from player 
    while not valid:

        while position not in ["1","2","3","4","5","6","7","8",'9']:
            position=raw_input("Enter the number between 1-9")
            
            
            #positining the x or o in board
        position=int(position)-1


        #check if there is a space for the player or already fille
        if board[position]=='-':
            valid=True
        else:
            print("go again")
        
    board[position] =player
    displayBoard()




def check_if_game_over():
    check_win()
    check_tie()





def check_win():
    global winner
    row_winner=check_row()
    column_winner=check_column()
    diagonal_winner=check_diagonal()

    if row_winner:
        winner=row_winner

    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None
    



def check_row():
    global game_is_still_going
    row1=board[6] == board[7] == board[8] != '-'
    row2=board[5] == board[4] == board[5] !='-'
    row3=board[0] == board[1] == board[2] !='-'

    if row1 or row2 or row3:
        game_is_still_going=False
    if row1:
        return board[6]
    if row2:
        return board[5]
    if row3:
        return board[0]
    return

def check_column():
    global game_is_still_going
    col1=board[6] == board[3] == board[0] != '-'
    col2=board[7] == board[4] == board[1] !='-'
    col3=board[8] == board[5] == board[2] !='-'

    if col1 or col2 or col3:
        game_is_still_going=False
    if col1:
        return board[6]
    if col2:
        return board[7]
    if col3:
        return board[8]
    return
   

def check_diagonal():
    global game_is_still_going
    diag1=board[6] == board[4] == board[2] != '-'
    diag2=board[8] == board[4] == board[0] !='-'

    if diag1 or diag2:
        game_is_still_going=False
    if diag1:
        return board[6]
    if diag2:
        return board[8]
    return


 
def check_tie():
    global game_is_still_going
    if '-' not in board:
        game_is_still_going=False
        return None




def flip_player():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer='X'
    







game()