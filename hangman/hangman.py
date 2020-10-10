#!/usr/bin/python3
import random
from word import words
wordchoice=random.choice(words)
worder=wordchoice
word=list(worder)

hidden=[]
for character in word:
    hidden.append('-')
isGameOver=False
attempts=0
max_attempts=4
while not isGameOver:
    hiddenString=' '.join(hidden)
    # display the current board, guessed letters, and attempts remaining
    print(f'the current word is {hiddenString}')

    print("     ------")
    print("     |    |")
    print("     |    " + ("O" if attempts > 0 else ""))
    print("     |    " + ("/\\" if attempts > 1 else ""))
    print("     |    " + ("|" if attempts > 2 else ""))
    print("     |    " + ("/\\" if attempts > 3 else ""))
    print(" --------")
    letterGuessed = input("Please guess a letter: ")


    print('\n\n\n\n')

    if letterGuessed in word:
        # if the player guessed correct, show all matched letters and print message
        for i in range(len(word)):
            character = word[i]
            if character == letterGuessed:
                hidden[i] = word[i]
                word[i] = "_"
        
    else:
        print(f'You had wrong a guessed, Remaining attempt{max_attempts-attempts}')
        attempts+=1
    if all("_" == char for char in word):
        print("""        
 ▄· ▄▌      ▄• ▄▌    ▄▄▌ ▐ ▄▌▪   ▐ ▄             
▐█▪██▌▪     █▪██▌    ██· █▌▐███ •█▌▐█            
▐█▌▐█▪ ▄█▀▄ █▌▐█▌    ██▪▐█▐▐▌▐█·▐█▐▐▌            
 ▐█▀·.▐█▌.▐▌▐█▄█▌    ▐█▌██▐█▌▐█▌██▐█▌            
  ▀ •  ▀█▄▀▪ ▀▀▀      ▀▀▀▀ ▀▪▀▀▀▀▀ █▪                                      
        
        
        """)
        isGameOver = True
    if attempts>4:
        print(""" ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .           ▌ ▐·▄▄▄ .▄▄▄          
▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·    ▪     ▪█·█▌▀▄.▀·▀▄ █·        
▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄     ▄█▀▄ ▐█▐█•▐▀▀▪▄▐▀▀▄         
▐█▄▪▐█▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌    ▐█▌.▐▌ ███ ▐█▄▄▌▐█•█▌        
·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀      ▀█▄▀▪. ▀   ▀▀▀ .▀  ▀        """)
        print(f'The correct answer is: {worder.upper()}')
        isGameOver=True





