#the dictionary board
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }


#board display in console 
def board(board):
    print(board['7']+'|'+ board['8'] + '|'+board['9'])
    print("-----")
    print(board['4']+'|'+ board['5'] + '|'+board['6'])
    print("-----")
    print(board['1']+'|'+ board['2'] + '|'+board['3'])

def game():
   
    turn='x'
    count=0
    for i in range(10):
        board(theBoard)
        print("its your turn"+ turn +"insert the number")
        move=input()
        if theBoard[move]=='':
            theBoard[move]=turn
            count +=1
        else:
            continue 
        if count>=5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] !=' ':
                board(theBoard)
                print("\nGame Over\n")
                print('******'+turn+'won ******')
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] !=' ':
                board(theBoard)
                print("\nGame Over\n")
                print('******'+turn+'won ******')
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] !=' ':
                board(theBoard)
                print("\nGame Over\n")
                print('******'+turn+'won ******')
                break
            elif theBoard['7'] == theBoard['4'] == theBoard['1'] !=' ':
                board(theBoard)
                print("\nGame Over\n")
                print('******'+turn+'won ******')
                break
            elif theBoard['8'] == theBoard['5'] == theBoard['2'] !=' ':
                board(theBoard)
                print("\nGame Over\n")
                print('******'+turn+'won ******')
                break
            elif theBoard['9'] == theBoard['6'] == theBoard['3'] !=' ':
                board(theBoard)
                print("\nGame Over\n")
                print('******'+turn+'won ******')
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] !=' ':
                board(theBoard)
                print("\nGame Over\n")
                print('******'+turn+'won ******')
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] !=' ':
                board(theBoard)
                print("\nGame Over\n")
                print('******'+turn+'won ******')
                break
        if count == 9:
            board(theBoard)
            print("********the game is tie ***********")
        if turn=='x':
                turn='0'
        else:
                turn='x'

            
            
           
game()
