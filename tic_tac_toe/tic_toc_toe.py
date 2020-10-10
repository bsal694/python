#!/usr/bin/env python3

#at first the code tells that game is still going 
import os 
game_is_still_going=True



#no one is winner 
winner = None 


#Default player 
currentPlayer="x"


#this is a sample board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#access keys from board(list)
def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")





#Main program 
def playGame():
    #display board
    displayBoard()

    
    
    #Only operate the loop if it is true 
    while game_is_still_going:
        



        handleTurn(currentPlayer)

        check_if_game_over()


        flip_player()
    if winner == 'x' or winner == 'o':
        
        print(winner + ' is the winner')
        os.system('spd-say "game over"')
    elif winner == None:
        print('tie')






def handleTurn(player):

    print(player+' turn')
    position=raw_input("enter the number between 1-9: ")
    valid=False

    #if value is false then it run 
    while not valid:

        #character except 1-9 then as the input from player 
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position=raw_input("Enter the number between 1-9")
        
        
        #positining the x or o in board
        position=int(position)-1


        #check if there is a space for the player or already fille
        if board[position]=='-':
            valid=True 
        else:
            print('you cant go there go again')
    
    
    
    
    board[position] =player
    displayBoard()

def check_if_game_over():
    check_win()
    check_tie()



def flip_player():
    global currentPlayer
    if currentPlayer=='x':
        currentPlayer='o'
    else:
        currentPlayer='x'
    return




def check_win():

    global winner
    row_winner=check_row()
    columns_winner=check_columns()
    diagonal_winner=check_diagonal()
    if row_winner:
        winner=row_winner
    elif columns_winner:
        winner=columns_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None 
    pass





def check_row():
    global game_is_still_going
    row1= board[0] == board[1] == board[2] !='-'
    row2= board[3] == board[4] == board[5] !='-'
    row3= board[6] == board[7] == board[8] !='-'
    if row1 or row2 or row3:
        game_is_still_going = False
    if row1:
        return board[0]
    elif row2:
        return board[1]
    elif row3:
        return board[2]
    return
    



def check_columns():
    global game_is_still_going
    col1= board[0] == board[3] == board[6] 
    col2= board[1] == board[4] == board[7] !='-'
    col3= board[2] == board[5] == board[8] !='-'
    if col1 or col2 or col3:
        game_is_still_going=False
    if col1:
        return board[0]
    elif col2:
        return board[3]
    elif col3:
        return board[6]
    return
    
def check_diagonal():
    global game_is_still_going
    dig1= board[0] == board[4] == board[8] !='-'
    dig2= board[2] == board[4] == board[6] !='-'
    if dig1 or dig2:
        game_is_still_going=False
    if dig1:
        return board[0]
    elif dig2:
        return board[2]
    return


def check_tie():
    global game_is_still_going

    if "-" not in board:
        game_is_still_going=False
        return None 


playGame()







