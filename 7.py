#Tic Tac Toe game vs CPU
#Plays on Python 2.7!!!!!!!

import random

board = range(0,10)


def printBoard():     #game grid

    print board[1], '|', board[2], '|',board[3]
    print '----------'
    print board[4], '|', board[5], '|',board[6]
    print '----------'
    print board[7], '|', board[8], '|',board[9]

printBoard()

win=0


def check(sign):     #elegxei oles tis periptweis an nikise exse kapoios i vghke isopalia
    if board[1] == sign and board[2] == sign and board[3] == sign:
        win=1
        return True
    if board[4] == sign and board[5] == sign and board[6] == sign:
        win=1
        return True
    if board[7] == sign and board[8] == sign and board[9] == sign:
        win=1
        return True
    if board[1] == sign and board[4] == sign and board[7] == sign:
        win=1
        return True
    if board[2] == sign and board[5] == sign and board[8] == sign:
        win=1
        return True
    if board[3] == sign and board[6] == sign and board[9] == sign:
        win=1
        return True
    if board[1] == sign and board[5] == sign and board[9] == sign:
        win=1
        return True
    if board[3] == sign and board[5] == sign and board[7] == sign:
        win=1
        return True
    if  board[1] == 1 or board[2] == 2 or board[3]==3 or board[4] ==   4 or board[5]==5 or board[6]==6 or board[7]==7 or board[8]==8 or board[9] == 9 :
        return False
    else:

        print ("It's a Tie")
        tie=1

    quit()

print ("Hello player 1! Let's play some Tic Tac Toe")


def round1():            #paizei o player1
    box=int(input('Plese enter a number from [1,9] to place X :  '))
    if board[box]!= "O" and board[box]!="X":  #elegos an to koiuti einai adeio
        board[box]="X"
        printBoard()
        sign="X"


    else :
        print ("This spot is taken! Try another one!")
        round1()
        sign="X"
    if check(sign)== True: #elegxos an nikise exase i prepei na synexistei to paixnidi
        print ("YOU WON THE GAME")
        win==1
        quit()
        return True;
    else:
        return False;

def round2():               #paizei o ypologistis
    if win!=1:
        print ("Now it's computer's turn!")
        random.seed()
        cpu= random.randint(1,9)
        while board[cpu]== "O" or board[cpu]=="X":   #elegos an to koiuti einai adeio
            random.seed()
            cpu=random.randint(1,9)
        if board[cpu]!="O" and board[cpu]!="X":
                board[cpu]="O"
                printBoard()
                #global sign
                note="O"

        if check(note)== True:    #elegxos an nikise exase i prepei na synexistei to paixnidi
            print ("CPU WON THE GAME")
            win==1
            quit()
            return True;
        else:
            return False;


while win==0:
    round1()
    round2()
