#Program to make Tic Tac Toe on human v/s computer(easy), human v/s computer(impossible), human v/s human, computer v/s computer mode
#this program works on a 3x3 dataframe with 1 to 9 integers print on it sequentially to mark the move by user and computer
#easy mode of program works with computer's input randomly
#impossible mode of program works with conmputer's fixed input by cases
#human v/s human mode of program works with user's input
#computer v/s computer mode of program works with computer's input randomly (no interaction of user)

import pandas as pd
import random as r
import sys
from tabulate import tabulate
import time

#defining 3 functions which will help checking the winner for easy mode by checking each row, column and the diagonals for both players(user and computer)
#for example if O-O-O comes across a diagonal fn2() will check this and give win to the computer
#all fn1,fn2,fn3 are used for human v/s computer, human v/s human, computer v/s computer
#fn1 is used for checking the rows, columns and the diagonals for user upto 4 moves
def fn1():
    if x.loc[1,1] == 'X':
        if x.loc[1,2] == 'X':
            if x.loc[1,3] == 'X':
                if n==1:
                    print('You won')
                    sys.exit()
                if n==3:
                    print('Player-X won')
                    sys.exit()
                if n==4:
                    print('Computer-X won')
                    sys.exit()
        if x.loc[2,2] == 'X':
            if x.loc[3,3] == 'X':   
                if n==1:
                    print('You won')
                    sys.exit()
                if n==3:
                    print('Player-X won')
                    sys.exit()
                if n==4:
                    print('Computer-X won')
                    sys.exit()
        if x.loc[2,1] == 'X':
            if x.loc[3,1] == 'X':
                if n==1:
                    print('You won')
                    sys.exit()
                if n==3:
                    print('Player-X won')
                    sys.exit()
                if n==4:
                    print('Computer-X won')
                    sys.exit()

    if x.loc[2,2] == 'X':
        if x.loc[1,2] == 'X':
            if x.loc[3,2] == 'X':
                if n==1:
                    print('You won')
                    sys.exit()
                if n==3:
                    print('Player-X won')
                    sys.exit()
                if n==4:
                    print('Computer-X won')
                    sys.exit()
        if x.loc[2,1] == 'X':
            if x.loc[2,3] == 'X':
                if n==1:
                    print('You won')
                    sys.exit()
                if n==3:
                    print('Player-X won')
                    sys.exit()
                if n==4:
                    print('Computer-X won')
                    sys.exit()
        if x.loc[1,3] == 'X':
            if x.loc[3,1] == 'X':
                if n==1:
                    print('You won')
                    sys.exit()
                if n==3:
                    print('Player-X won')
                    sys.exit()
                if n==4:
                    print('Computer-X won')
                    sys.exit()

    if x.loc[3,3] == 'X':
        if x.loc[1,3] == 'X':
            if x.loc[2,3] == 'X':
                if n==1:
                    print('You won')
                    sys.exit()
                if n==3:
                    print('Player-X won')
                    sys.exit()
                if n==4:
                    print('Computer-X won')
                    sys.exit()
        if x.loc[3,1] == 'X':
            if x.loc[3,2] == 'X':
                if n==1:
                    print('You won')
                    sys.exit()
                if n==3:
                    print('Player-X won')
                    sys.exit()
                if n==4:
                    print('Computer-X won')
                    sys.exit()



#fn2 is used for checking the rows, columns and the diagonals for computer upto all its moves
def fn2():
    if x.loc[1,1] == 'O':
        if x.loc[1,2] == 'O':
            if x.loc[1,3] == 'O':
                if n==1:
                    print('You lost')
                    sys.exit()
                if n==3:
                    print('Player-O won')
                    sys.exit()
                if n==4:
                    print('Computer-O won')
                    sys.exit()
        if x.loc[2,2] == 'O':
            if x.loc[3,3] == 'O':
                if n==1:
                    print('You lost')
                    sys.exit()
                if n==3:
                    print('Player-O won')
                    sys.exit()
                if n==4:
                    print('Computer-O won')
                    sys.exit()
        if x.loc[2,1] == 'O':
            if x.loc[3,1] == 'O':
                if n==1:
                    print('You lost')
                    sys.exit()
                if n==3:
                    print('Player-O won')
                    sys.exit()
                if n==4:
                    print('Computer-O won')
                    sys.exit()

    if x.loc[2,2] == 'O':
        if x.loc[1,2] == 'O':
            if x.loc[3,2] == 'O':
                if n==1:
                    print('You lost')
                    sys.exit()
                if n==3:
                    print('Player-O won')
                    sys.exit()
                if n==4:
                    print('Computer-O won')
                    sys.exit()
        if x.loc[2,1] == 'O':
            if x.loc[2,3] == 'O':
                if n==1:
                    print('You lost')
                    sys.exit()
                if n==3:
                    print('Player-O won')
                    sys.exit()
                if n==4:
                    print('Computer-O won')
                    sys.exit()
        if x.loc[1,3] == 'O':
            if x.loc[3,1] == 'O':
                if n==1:
                    print('You lost')
                    sys.exit()
                if n==3:
                    print('Player-O won')
                    sys.exit()
                if n==4:
                    print('Computer-O won')
                    sys.exit()

    if x.loc[3,3] == 'O':
        if x.loc[1,3] == 'O':
            if x.loc[2,3] == 'O':
                if n==1:
                    print('You lost')
                    sys.exit()
                if n==3:
                    print('Player-O won')
                    sys.exit()
                if n==4:
                    print('Computer-O won')
                    sys.exit()
        if x.loc[3,1] == 'O':
            if x.loc[3,2] == 'O':
                if n==1:
                    print('You lost')
                    sys.exit()
                if n==3:
                    print('Player-O won')
                    sys.exit()
                if n==4:
                    print('Computer-O won')
                    sys.exit()


#fn3 is used for checking the rows, columns and the diagonals for user for its last move since even draw can happen             
def fn3():
    count = 0
    if x.loc[1,1] == 'X':
        if x.loc[1,2] == 'X':
            if x.loc[1,3] == 'X':
                if n==1:
                    print('You win')
                    sys.exit()
                if n==3:
                    print('Player-X won')
                    sys.exit()
                if n==4:
                    print('Computer-X won')
                    sys.exit()
                
    if x.loc[1,1] == 'X':    
        if x.loc[2,2] == 'X':
            if x.loc[3,3] == 'X':
                if n==1:
                    print('You win')
                    sys.exit()
                if n==3:
                    print('Player-X won')
                    sys.exit()
                if n==4:
                    print('Computer-X won')
                    sys.exit()
                
    if x.loc[1,1] == 'X':        
        if x.loc[2,1] == 'X':
            if x.loc[3,1] == 'X':
                if n==1:
                    print('You win')
                    sys.exit()
                if n==3:
                    print('Player-X won')
                    sys.exit()
                if n==4:
                    print('Computer-X won')
                    sys.exit()
                
            
    if x.loc[2,2] == 'X':
        if x.loc[1,2] == 'X':
            if x.loc[3,2] == 'X':
                if n==1:
                    print('You win')
                    sys.exit()
                if n==3:
                    print('Player-X won')
                    sys.exit()
                if n==4:
                    print('Computer-X won')
                    sys.exit()
                
    if x.loc[2,2] == 'X':        
        if x.loc[2,1] == 'X':
            if x.loc[2,3] == 'X':
                if n==1:
                    print('You win')
                    sys.exit()
                if n==3:
                    print('Player-X won')
                    sys.exit()
                if n==4:
                    print('Computer-X won')
                    sys.exit()
                
    if x.loc[2,2] == 'X':        
        if x.loc[1,3] == 'X':
            if x.loc[3,1] == 'X':
                if n==1:
                    print('You win')
                    sys.exit()
                if n==3:
                    print('Player-X won')
                    sys.exit()
                if n==4:
                    print('Computer-X won')
                    sys.exit()
                
            
    if x.loc[3,3] == 'X':
        if x.loc[1,3] == 'X':
            if x.loc[2,3] == 'X':
                if n==1:
                    print('You win')
                    sys.exit()
                if n==3:
                    print('Player-X won')
                    sys.exit()
                if n==4:
                    print('Computer-X won')
                    sys.exit()
                
    if x.loc[3,3] == 'X':       
        if x.loc[3,1] == 'X':
            if x.loc[3,2] == 'X':
                if n==1:
                    print('You win')
                    sys.exit()
                if n==3:
                    print('Player-X won')
                    sys.exit()
                if n==4:
                    print('Computer-X won')
                    sys.exit()
    
    if count == 0:
        print('Game Draw')
    
    sys.exit()

#main code
#selection for mode
print('(1) Human v/s Computer(Easy)')
print('(2) Human v/s Computer(Impossible)')
print('(3) Human v/s Human')
print('(4) Computer v/s Computer')

n=0
while n not in [1,2,3,4]:
    n = int(input('Enter difficulty level: '))

#creation of dataframe with indexing of both column and row as [1,2,3]
if n==1:
    a={1:1,2:2,3:3}
    b={1:4,2:5,3:6}
    c={1:7,2:8,3:9}
    x=pd.DataFrame([a,b,c],index=[1,2,3])
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    w=[1,2,3,4,5,6,7,8,9]

    a=0
    while a not in w:
        print('')
        a=int(input("Mark 'X': "))

#user's chance-1, input is given by the user and the input is marked as a 'X' on the dataframe
    if a in w:
        if a == 1:
            x.loc[1,1] = 'X'
        if a == 2:
            x.loc[1,2] = 'X'
        if a == 3:
            x.loc[1,3] = 'X'
        if a == 4:
            x.loc[2,1] = 'X'
        if a == 5:
            x.loc[2,2] = 'X'
        if a == 6:
            x.loc[2,3] = 'X'
        if a == 7:
            x.loc[3,1] = 'X'
        if a == 8:
            x.loc[3,2] = 'X'
        if a == 9:
            x.loc[3,3] = 'X'
        w.remove(a)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)



#randomly choosing random integer between 1 and 9 and using it as input of computer
    c=r.randint(1,9)
    while c not in w:
        c=r.randint(1,9)
        

#computer's chance-1, input is given by the computer randomly and the input is marked as a 'O' on the dataframe
    if c in w:
        if c == 1:
            x.loc[1,1] = 'O'
        if c == 2:
            x.loc[1,2] = 'O'
        if c == 3:
            x.loc[1,3] = 'O'
        if c == 4:
            x.loc[2,1] = 'O'
        if c == 5:
            x.loc[2,2] = 'O'
        if c == 6:
            x.loc[2,3] = 'O'
        if c == 7:
            x.loc[3,1] = 'O'
        if c == 8:
            x.loc[3,2] = 'O'
        if c == 9:
            x.loc[3,3] = 'O'
        w.remove(c)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)

#user's chance-2
    a=0
    while a not in w:
        print('')
        a=int(input("Mark 'X': "))

    if a in w:
        if a == 1:
            x.loc[1,1] = 'X'
        if a == 2:
            x.loc[1,2] = 'X'
        if a == 3:
            x.loc[1,3] = 'X'
        if a == 4:
            x.loc[2,1] = 'X'
        if a == 5:
            x.loc[2,2] = 'X'
        if a == 6:
            x.loc[2,3] = 'X'
        if a == 7:
            x.loc[3,1] = 'X'
        if a == 8:
            x.loc[3,2] = 'X'
        if a == 9:
            x.loc[3,3] = 'X'
        w.remove(a)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)

#computer's chance-2
    c=r.randint(1,9)
    while c not in w:
        c=r.randint(1,9)
        


    if c in w:
        if c == 1:
            x.loc[1,1] = 'O'
        if c == 2:
            x.loc[1,2] = 'O'
        if c == 3:
            x.loc[1,3] = 'O'
        if c == 4:
            x.loc[2,1] = 'O'
        if c == 5:
            x.loc[2,2] = 'O'
        if c == 6:
            x.loc[2,3] = 'O'
        if c == 7:
            x.loc[3,1] = 'O'
        if c == 8:
            x.loc[3,2] = 'O'
        if c == 9:
            x.loc[3,3] = 'O'
        w.remove(c)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)

#user's chance-3
    a=0
    while a not in w:
        print('')
        a=int(input("Mark 'X': "))

    if a in w:
        if a == 1:
            x.loc[1,1] = 'X'
        if a == 2:
            x.loc[1,2] = 'X'
        if a == 3:
            x.loc[1,3] = 'X'
        if a == 4:
            x.loc[2,1] = 'X'
        if a == 5:
            x.loc[2,2] = 'X'
        if a == 6:
            x.loc[2,3] = 'X'
        if a == 7:
            x.loc[3,1] = 'X'
        if a == 8:
            x.loc[3,2] = 'X'
        if a == 9:
            x.loc[3,3] = 'X'
        w.remove(a)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)

    fn1()

#computer's chance-3
    c=r.randint(1,9)
    while c not in w:
        c=r.randint(1,9)
        


    if c in w:
        if c == 1:
            x.loc[1,1] = 'O'
        if c == 2:
            x.loc[1,2] = 'O'
        if c == 3:
            x.loc[1,3] = 'O'
        if c == 4:
            x.loc[2,1] = 'O'
        if c == 5:
            x.loc[2,2] = 'O'
        if c == 6:
            x.loc[2,3] = 'O'
        if c == 7:
            x.loc[3,1] = 'O'
        if c == 8:
            x.loc[3,2] = 'O'
        if c == 9:
            x.loc[3,3] = 'O'
        w.remove(c)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)

    fn2()

#user's chance-4
    a=0
    while a not in w:
        print('')
        a=int(input("Mark 'X': "))

    if a in w:
        if a == 1:
            x.loc[1,1] = 'X'
        if a == 2:
            x.loc[1,2] = 'X'
        if a == 3:
            x.loc[1,3] = 'X'
        if a == 4:
            x.loc[2,1] = 'X'
        if a == 5:
            x.loc[2,2] = 'X'
        if a == 6:
            x.loc[2,3] = 'X'
        if a == 7:
            x.loc[3,1] = 'X'
        if a == 8:
            x.loc[3,2] = 'X'
        if a == 9:
            x.loc[3,3] = 'X'
        w.remove(a)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)

    fn1()

#computer's chance-4
    c=r.randint(1,9)
    while c not in w:
        c=r.randint(1,9)
        

    if c in w:
        if c == 1:
            x.loc[1,1] = 'O'
        if c == 2:
            x.loc[1,2] = 'O'
        if c == 3:
            x.loc[1,3] = 'O'
        if c == 4:
            x.loc[2,1] = 'O'
        if c == 5:
            x.loc[2,2] = 'O'
        if c == 6:
            x.loc[2,3] = 'O'
        if c == 7:
            x.loc[3,1] = 'O'
        if c == 8:
            x.loc[3,2] = 'O'
        if c == 9:
            x.loc[3,3] = 'O'
        w.remove(c)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)

    fn2()

#user's 5th and last move
    a=0
    while a not in w:
        print('')
        a=int(input("Mark 'X': "))

    if a in w:
        if a == 1:
            x.loc[1,1] = 'X'
        if a == 2:
            x.loc[1,2] = 'X'
        if a == 3:
            x.loc[1,3] = 'X'
        if a == 4:
            x.loc[2,1] = 'X'
        if a == 5:
            x.loc[2,2] = 'X'
        if a == 6:
            x.loc[2,3] = 'X'
        if a == 7:
            x.loc[3,1] = 'X'
        if a == 8:
            x.loc[3,2] = 'X'
        if a == 9:
            x.loc[3,3] = 'X'
        w.remove(a)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)

    fn3()

#easy mode completed
#-----------------------------#
#-----------------------------#
#-----------------------------#
#-----------------------------#

#impossible mode
#there is no case of winning by the user
#if the user puts first move on the center then there is 100% chance of tie unless user plays a wrong move
#if the user puts first move anywhere else then there is 100% chance of win of computer

#defining a dataframe with initially a fixed move by computer(this fixes the game to be won by computer or a tie)
if n==2:
    j=r.randint(1,2)
    a={1:1,2:2,3:3}
    b={1:4,2:5,3:6}
    c={1:'X',2:8,3:9}
    x=pd.DataFrame([a,b,c],index=[1,2,3])
    if j == 1:
        print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    if j == 2:
        print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    w=[1,2,3,4,5,6,8,9]


    a=0
    while a not in w:
        print('')
        a=int(input("Mark 'O': "))

    if a in w:
        if a == 1:
            x.loc[1,1] = 'O'
        if a == 2:
            x.loc[1,2] = 'O'
        if a == 3:
            x.loc[1,3] = 'O'
        if a == 4:
            x.loc[2,1] = 'O'
        if a == 5:
            x.loc[2,2] = 'O'
        if a == 6:
            x.loc[2,3] = 'O'
        if a == 8:
            x.loc[3,2] = 'O'
        if a == 9:
            x.loc[3,3] = 'O'
        w.remove(a)
    if j == 1:
        print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    if j == 2:
        print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)

#Since there are 8 remaining boxes to fill, user has 8 choices for first move, and each first move makes a different case

    #case-1 [1,1] is marked by the user
    #100% win by computer
    #computer put its mark on the corners which allows it to make the winning move everytime 
    if x.loc[1,1]=='O':
        x.loc[3,3]='X'
        w.remove(9)
        if j == 1:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        if j == 2:
            print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        print('Remaining: ',w)


        a=0
        while a not in w:
            print('')
            a=int(input("Mark 'O': "))

        if a in w:
            if a == 1:
                x.loc[1,1] = 'O'
            if a == 2:
                x.loc[1,2] = 'O'
            if a == 3:
                x.loc[1,3] = 'O'
            if a == 4:
                x.loc[2,1] = 'O'
            if a == 5:
                x.loc[2,2] = 'O'
            if a == 6:
                x.loc[2,3] = 'O'
            if a == 8:
                x.loc[3,2] = 'O'
            if a == 9:
                x.loc[3,3] = 'O'
            w.remove(a)
        if j == 1:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        if j == 2:
            print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        print('Remaining: ',w)


        if x.loc[3,2] == 8:
            x.loc[3,2]='X'
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('You lost')
            sys.exit()
        else:
            x.loc[1,3] = 'X'
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('Remaining: ',w)
            

            a=0
            while a not in w:
                print('')
                a=int(input("Mark 'O': "))

            if a in w:
                if a == 1:
                    x.loc[1,1] = 'O'
                if a == 2:
                    x.loc[1,2] = 'O'
                if a == 3:
                    x.loc[1,3] = 'O'
                if a == 4:
                    x.loc[2,1] = 'O'
                if a == 5:
                    x.loc[2,2] = 'O'
                if a == 6:
                    x.loc[2,3] = 'O'
                if a == 8:
                    x.loc[3,2] = 'O'
                if a == 9:
                    x.loc[3,3] = 'O'
                w.remove(a)
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('Remaining: ',w)

            if x.loc[2,3] == 6:
                x.loc[2,3] = 'X'
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('You lost')
                sys.exit()
            else:
                x.loc[2,2] = 'X'
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('You lost')
                sys.exit()



    #case-2 [3,3] marked by user
    #100% win by computer
    #the mechanism is same as case-1
    if x.loc[3,3]=='O':
        x.loc[1,1]='X'
        w.remove(1)
        if j == 1:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        if j == 2:
            print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        print('Remaining: ',w)


        a=0
        while a not in w:
            print('')
            a=int(input("Mark 'O': "))

        if a in w:
            if a == 1:
                x.loc[1,1] = 'O'
            if a == 2:
                x.loc[1,2] = 'O'
            if a == 3:
                x.loc[1,3] = 'O'
            if a == 4:
                x.loc[2,1] = 'O'
            if a == 5:
                x.loc[2,2] = 'O'
            if a == 6:
                x.loc[2,3] = 'O'
            if a == 8:
                x.loc[3,2] = 'O'
            if a == 9:
                x.loc[3,3] = 'O'
            w.remove(a)
        if j == 1:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        if j == 2:
            print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        print('Remaining: ',w)

        if x.loc[2,1] == 4:
            x.loc[2,1]='X'
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('You lost')
            sys.exit()
        else:
            x.loc[1,3] = 'X'
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('Remaining: ',w)
            a=0
            while a not in w:
                print('')
                a=int(input("Mark 'O': "))

            if a in w:
                if a == 1:
                    x.loc[1,1] = 'O'
                if a == 2:
                    x.loc[1,2] = 'O'
                if a == 3:
                    x.loc[1,3] = 'O'
                if a == 4:
                    x.loc[2,1] = 'O'
                if a == 5:
                    x.loc[2,2] = 'O'
                if a == 6:
                    x.loc[2,3] = 'O'
                if a == 8:
                    x.loc[3,2] = 'O'
                if a == 9:
                    x.loc[3,3] = 'O'
                w.remove(a)
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('Remaining: ',w)

            if x.loc[1,2] == 2:
                x.loc[1,2] = 'X'
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('You lost')
                sys.exit()
            else:
                x.loc[2,2] = 'X'
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('You lost')
                sys.exit()


    #case-3 [2,1] marked by user
    #100% win by computer
    if x.loc[2,1]=='O':
        x.loc[3,3]='X'
        w.remove(9)
        if j == 1:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        if j == 2:
            print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        print('Remaining: ',w)


        a=0
        while a not in w:
            print('')
            a=int(input("Mark 'O': "))

        if a in w:
            if a == 1:
                x.loc[1,1] = 'O'
            if a == 2:
                x.loc[1,2] = 'O'
            if a == 3:
                x.loc[1,3] = 'O'
            if a == 4:
                x.loc[2,1] = 'O'
            if a == 5:
                x.loc[2,2] = 'O'
            if a == 6:
                x.loc[2,3] = 'O'
            if a == 8:
                x.loc[3,2] = 'O'
            if a == 9:
                x.loc[3,3] = 'O'
            w.remove(a)
        if j == 1:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        if j == 2:
            print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        print('Remaining: ',w)

        if x.loc[3,2] == 8:
            x.loc[3,2]='X'
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('You lost')
            sys.exit()
        else:
            x.loc[1,3] = 'X'
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('Remaining: ',w)
            
            a=0
            while a not in w:
                print('')
                a=int(input("Mark 'O': "))

            if a in w:
                if a == 1:
                    x.loc[1,1] = 'O'
                if a == 2:
                    x.loc[1,2] = 'O'
                if a == 3:
                    x.loc[1,3] = 'O'
                if a == 4:
                    x.loc[2,1] = 'O'
                if a == 5:
                    x.loc[2,2] = 'O'
                if a == 6:
                    x.loc[2,3] = 'O'
                if a == 8:
                    x.loc[3,2] = 'O'
                if a == 9:
                    x.loc[3,3] = 'O'
                w.remove(a)
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('Remaining: ',w)

            if x.loc[2,3] == 6:
                x.loc[2,3] = 'X'
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('You lost')
                sys.exit()
            else:
                x.loc[2,2] = 'X'
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('You lost')
                sys.exit()


    #case-4 [3,2] marked by user
    #100% win by computer
    if x.loc[3,2]=='O':
        x.loc[1,1]='X'
        w.remove(1)
        if j == 1:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        if j == 2:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        print('Remaining: ',w)


        a=0
        while a not in w:
            print('')
            a=int(input("Mark 'O': "))

        if a in w:
            if a == 1:
                x.loc[1,1] = 'O'
            if a == 2:
                x.loc[1,2] = 'O'
            if a == 3:
                x.loc[1,3] = 'O'
            if a == 4:
                x.loc[2,1] = 'O'
            if a == 5:
                x.loc[2,2] = 'O'
            if a == 6:
                x.loc[2,3] = 'O'
            if a == 8:
                x.loc[3,2] = 'O'
            if a == 9:
                x.loc[3,3] = 'O'
            w.remove(a)
        if j == 1:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        if j == 2:
            print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        print('Remaining: ',w)

        if x.loc[2,1] == 4:
            x.loc[2,1]='X'
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('You lost')
            sys.exit()
        else:
            x.loc[1,3] = 'X'
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('Remaining: ',w)
            
            a=0
            while a not in w:
                print('')
                a=int(input("Mark 'O': "))

            if a in w:
                if a == 1:
                    x.loc[1,1] = 'O'
                if a == 2:
                    x.loc[1,2] = 'O'
                if a == 3:
                    x.loc[1,3] = 'O'
                if a == 4:
                    x.loc[2,1] = 'O'
                if a == 5:
                    x.loc[2,2] = 'O'
                if a == 6:
                    x.loc[2,3] = 'O'
                if a == 8:
                    x.loc[3,2] = 'O'
                if a == 9:
                    x.loc[3,3] = 'O'
                w.remove(a)
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('Remaining: ',w)

            if x.loc[1,2] == 2:
                x.loc[1,2] = 'X'
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('You lost')
                sys.exit()
            else:
                x.loc[2,2] = 'X'
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('You lost')
                sys.exit()


    #case-5 [1,3] marked by user
    #100% win by computer
    if x.loc[1,3]=='O':
        x.loc[1,1]='X'
        w.remove(1)
        if j == 1:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        if j == 2:
            print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        print('Remaining: ',w)


        a=0
        while a not in w:
            print('')
            a=int(input("Mark 'O': "))

        if a in w:
            if a == 1:
                x.loc[1,1] = 'O'
            if a == 2:
                x.loc[1,2] = 'O'
            if a == 3:
                x.loc[1,3] = 'O'
            if a == 4:
                x.loc[2,1] = 'O'
            if a == 5:
                x.loc[2,2] = 'O'
            if a == 6:
                x.loc[2,3] = 'O'
            if a == 8:
                x.loc[3,2] = 'O'
            if a == 9:
                x.loc[3,3] = 'O'
            w.remove(a)
        if j == 1:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        if j == 2:
            print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        print('Remaining: ',w)

        if x.loc[2,1] == 4:
            x.loc[2,1]='X'
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('You lost')
            sys.exit()
        else:
            x.loc[3,3] = 'X'
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('Remaining: ',w)
            
            a=0
            while a not in w:
                print('')
                a=int(input("Mark 'O': "))

            if a in w:
                if a == 1:
                    x.loc[1,1] = 'O'
                if a == 2:
                    x.loc[1,2] = 'O'
                if a == 3:
                    x.loc[1,3] = 'O'
                if a == 4:
                    x.loc[2,1] = 'O'
                if a == 5:
                    x.loc[2,2] = 'O'
                if a == 6:
                    x.loc[2,3] = 'O'
                if a == 8:
                    x.loc[3,2] = 'O'
                if a == 9:
                    x.loc[3,3] = 'O'
                w.remove(a)
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('Remaining: ',w)

            if x.loc[3,2] == 8:
                x.loc[3,2] = 'X'
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('You lost')
                sys.exit()
            else:
                x.loc[2,2] = 'X'
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('You lost')
                sys.exit()




    #case-6 [1,2] marked by user
    #100% win by computer
    if x.loc[1,2]=='O':
        x.loc[3,3]='X'
        w.remove(9)
        if j == 1:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        if j == 2:
            print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        print('Remaining: ',w)


        a=0
        while a not in w:
            print('')
            a=int(input("Mark 'O': "))

        if a in w:
            if a == 1:
                x.loc[1,1] = 'O'
            if a == 2:
                x.loc[1,2] = 'O'
            if a == 3:
                x.loc[1,3] = 'O'
            if a == 4:
                x.loc[2,1] = 'O'
            if a == 5:
                x.loc[2,2] = 'O'
            if a == 6:
                x.loc[2,3] = 'O'
            if a == 8:
                x.loc[3,2] = 'O'
            if a == 9:
                x.loc[3,3] = 'O'
            w.remove(a)
        if j == 1:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        if j == 2:
            print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        print('Remaining: ',w)

        if x.loc[3,2] == 8:
            x.loc[3,2]='X'
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('You lost')
            sys.exit()
        else:
            x.loc[2,2] = 'X'
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('Remaining: ',w)
            
            a=0
            while a not in w:
                print('')
                a=int(input("Mark 'O': "))

            if a in w:
                if a == 1:
                    x.loc[1,1] = 'O'
                if a == 2:
                    x.loc[1,2] = 'O'
                if a == 3:
                    x.loc[1,3] = 'O'
                if a == 4:
                    x.loc[2,1] = 'O'
                if a == 5:
                    x.loc[2,2] = 'O'
                if a == 6:
                    x.loc[2,3] = 'O'
                if a == 8:
                    x.loc[3,2] = 'O'
                if a == 9:
                    x.loc[3,3] = 'O'
                w.remove(a)
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('Remaining: ',w)

            if x.loc[1,1] == 1:
                x.loc[1,1] = 'X'
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('You lost')
                sys.exit()
            else:
                x.loc[1,3] = 'X'
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('You lost')
                sys.exit()




    #case-7 [2,3] marked by computer
    #100% win by computer
    if x.loc[2,3]=='O':
        x.loc[1,1]='X'
        w.remove(1)
        if j == 1:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        if j == 2:
            print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        print('Remaining: ',w)


        a=0
        while a not in w:
            print('')
            a=int(input("Mark 'O': "))

        if a in w:
            if a == 1:
                x.loc[1,1] = 'O'
            if a == 2:
                x.loc[1,2] = 'O'
            if a == 3:
                x.loc[1,3] = 'O'
            if a == 4:
                x.loc[2,1] = 'O'
            if a == 5:
                x.loc[2,2] = 'O'
            if a == 6:
                x.loc[2,3] = 'O'
            if a == 8:
                x.loc[3,2] = 'O'
            if a == 9:
                x.loc[3,3] = 'O'
            w.remove(a)
        if j == 1:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        if j == 2:
            print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        print('Remaining: ',w)

        if x.loc[2,1] == 4:
            x.loc[2,1]='X'
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('You lost')
            sys.exit()
        else:
            x.loc[2,2] = 'X'
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('Remaining: ',w)
            
            a=0
            while a not in w:
                print('')
                a=int(input("Mark 'O': "))

            if a in w:
                if a == 1:
                    x.loc[1,1] = 'O'
                if a == 2:
                    x.loc[1,2] = 'O'
                if a == 3:
                    x.loc[1,3] = 'O'
                if a == 4:
                    x.loc[2,1] = 'O'
                if a == 5:
                    x.loc[2,2] = 'O'
                if a == 6:
                    x.loc[2,3] = 'O'
                if a == 8:
                    x.loc[3,2] = 'O'
                if a == 9:
                    x.loc[3,3] = 'O'
                w.remove(a)
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('Remaining: ',w)

            if x.loc[3,1] == 1:
                x.loc[3,1] = 'X'
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('You lost')
                sys.exit()
            else:
                x.loc[1,3] = 'X'
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('You lost')
                sys.exit()



    #case-8 [2,2] marked by user
    #can be tied by user if played accordingly
    if x.loc[2,2]=='O':
        x.loc[1,1]='X'
        w.remove(1)
        if j == 1:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        if j == 2:
            print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        print('Remaining: ',w)


        a=0
        while a not in w:
            print('')
            a=int(input("Mark 'O': "))

        if a in w:
            if a == 1:
                x.loc[1,1] = 'O'
            if a == 2:
                x.loc[1,2] = 'O'
            if a == 3:
                x.loc[1,3] = 'O'
            if a == 4:
                x.loc[2,1] = 'O'
            if a == 5:
                x.loc[2,2] = 'O'
            if a == 6:
                x.loc[2,3] = 'O'
            if a == 8:
                x.loc[3,2] = 'O'
            if a == 9:
                x.loc[3,3] = 'O'
            w.remove(a)
        if j == 1:
            print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        if j == 2:
            print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
        print('Remaining: ',w)

        if x.loc[2,1] == 4:
            x.loc[2,1]='X'
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('You lost')
            sys.exit()
        else:
            x.loc[2,3] = 'X'
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('Remaining: ',w)
            
            a=0
            while a not in w:
                print('')
                a=int(input("Mark 'O': "))

            if a in w:
                if a == 1:
                    x.loc[1,1] = 'O'
                if a == 2:
                    x.loc[1,2] = 'O'
                if a == 3:
                    x.loc[1,3] = 'O'
                if a == 4:
                    x.loc[2,1] = 'O'
                if a == 5:
                    x.loc[2,2] = 'O'
                if a == 6:
                    x.loc[2,3] = 'O'
                if a == 8:
                    x.loc[3,2] = 'O'
                if a == 9:
                    x.loc[3,3] = 'O'
                w.remove(a)
            if j == 1:
                print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            if j == 2:
                print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
            print('Remaining: ',w)

            if x.loc[1,2] == 'O':
                x.loc[3,2]='X'
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('Game Draw')
            if x.loc[3,2] == 'O':
                x.loc[1,2]='X'
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('Game Draw')
            else:
                if j == 1:
                    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                if j == 2:
                    print(tabulate(x.T.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
                print('Game Draw')

#impossible mode completed

#------------------------------#
#------------------------------#
#------------------------------#

#human v/s human mode

if n==3:
    #creation of dataframe with indexing of both column and row as [1,2,3]
    a={1:1,2:2,3:3}
    b={1:4,2:5,3:6}
    c={1:7,2:8,3:9}
    x=pd.DataFrame([a,b,c],index=[1,2,3])
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    w=[1,2,3,4,5,6,7,8,9]
    

#--------------------------------------#
#plyera.b means player-a's bth chance

#player1.1
    a=0
    while a not in w:
        print('')
        a=int(input("Mark 'X': "))

    if a in w:
        if a == 1:
            x.loc[1,1] = 'X'
        if a == 2:
            x.loc[1,2] = 'X'
        if a == 3:
            x.loc[1,3] = 'X'
        if a == 4:
            x.loc[2,1] = 'X'
        if a == 5:
            x.loc[2,2] = 'X'
        if a == 6:
            x.loc[2,3] = 'X'
        if a == 7:
            x.loc[3,1] = 'X'
        if a == 8:
            x.loc[3,2] = 'X'
        if a == 9:
            x.loc[3,3] = 'X'
        w.remove(a)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    

#player2.1    
    c=0
    while c not in w:
        print('')
        c=int(input("Mark 'O': "))

    if c in w:
        if c == 1:
            x.loc[1,1] = 'O'
        if c == 2:
            x.loc[1,2] = 'O'
        if c == 3:
            x.loc[1,3] = 'O'
        if c == 4:
            x.loc[2,1] = 'O'
        if c == 5:
            x.loc[2,2] = 'O'
        if c == 6:
            x.loc[2,3] = 'O'
        if c == 7:
            x.loc[3,1] = 'O'
        if c == 8:
            x.loc[3,2] = 'O'
        if c == 9:
            x.loc[3,3] = 'O'
        w.remove(c)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    

#player1.2
    a=0
    while a not in w:
        print('')
        a=int(input("Mark 'X': "))

    if a in w:
        if a == 1:
            x.loc[1,1] = 'X'
        if a == 2:
            x.loc[1,2] = 'X'
        if a == 3:
            x.loc[1,3] = 'X'
        if a == 4:
            x.loc[2,1] = 'X'
        if a == 5:
            x.loc[2,2] = 'X'
        if a == 6:
            x.loc[2,3] = 'X'
        if a == 7:
            x.loc[3,1] = 'X'
        if a == 8:
            x.loc[3,2] = 'X'
        if a == 9:
            x.loc[3,3] = 'X'
        w.remove(a)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    

#player2.2
    c=0
    while c not in w:
        print('')
        c=int(input("Mark 'O': "))

    if c in w:
        if c == 1:
            x.loc[1,1] = 'O'
        if c == 2:
            x.loc[1,2] = 'O'
        if c == 3:
            x.loc[1,3] = 'O'
        if c == 4:
            x.loc[2,1] = 'O'
        if c == 5:
            x.loc[2,2] = 'O'
        if c == 6:
            x.loc[2,3] = 'O'
        if c == 7:
            x.loc[3,1] = 'O'
        if c == 8:
            x.loc[3,2] = 'O'
        if c == 9:
            x.loc[3,3] = 'O'
        w.remove(c)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    

#player1.3
    a=0
    while a not in w:
        print('')
        a=int(input("Mark 'X': "))

    if a in w:
        if a == 1:
            x.loc[1,1] = 'X'
        if a == 2:
            x.loc[1,2] = 'X'
        if a == 3:
            x.loc[1,3] = 'X'
        if a == 4:
            x.loc[2,1] = 'X'
        if a == 5:
            x.loc[2,2] = 'X'
        if a == 6:
            x.loc[2,3] = 'X'
        if a == 7:
            x.loc[3,1] = 'X'
        if a == 8:
            x.loc[3,2] = 'X'
        if a == 9:
            x.loc[3,3] = 'X'
        w.remove(a)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    fn1()
    

#player2.3
    c=0
    while c not in w:
        print('')
        c=int(input("Mark 'O': "))

    if c in w:
        if c == 1:
            x.loc[1,1] = 'O'
        if c == 2:
            x.loc[1,2] = 'O'
        if c == 3:
            x.loc[1,3] = 'O'
        if c == 4:
            x.loc[2,1] = 'O'
        if c == 5:
            x.loc[2,2] = 'O'
        if c == 6:
            x.loc[2,3] = 'O'
        if c == 7:
            x.loc[3,1] = 'O'
        if c == 8:
            x.loc[3,2] = 'O'
        if c == 9:
            x.loc[3,3] = 'O'
        w.remove(c)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    fn2()
    

#player1.4
    a=0
    while a not in w:
        print('')
        a=int(input("Mark 'X': "))

    if a in w:
        if a == 1:
            x.loc[1,1] = 'X'
        if a == 2:
            x.loc[1,2] = 'X'
        if a == 3:
            x.loc[1,3] = 'X'
        if a == 4:
            x.loc[2,1] = 'X'
        if a == 5:
            x.loc[2,2] = 'X'
        if a == 6:
            x.loc[2,3] = 'X'
        if a == 7:
            x.loc[3,1] = 'X'
        if a == 8:
            x.loc[3,2] = 'X'
        if a == 9:
            x.loc[3,3] = 'X'
        w.remove(a)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    fn1()
    

#playerp2.4
    c=0
    while c not in w:
        print('')
        c=int(input("Mark 'O': "))

    if c in w:
        if c == 1:
            x.loc[1,1] = 'O'
        if c == 2:
            x.loc[1,2] = 'O'
        if c == 3:
            x.loc[1,3] = 'O'
        if c == 4:
            x.loc[2,1] = 'O'
        if c == 5:
            x.loc[2,2] = 'O'
        if c == 6:
            x.loc[2,3] = 'O'
        if c == 7:
            x.loc[3,1] = 'O'
        if c == 8:
            x.loc[3,2] = 'O'
        if c == 9:
            x.loc[3,3] = 'O'
        w.remove(c)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    fn2()
    

#player1.5
    a=0
    while a not in w:
        print('')
        a=int(input("Mark 'X': "))

    if a in w:
        if a == 1:
            x.loc[1,1] = 'X'
        if a == 2:
            x.loc[1,2] = 'X'
        if a == 3:
            x.loc[1,3] = 'X'
        if a == 4:
            x.loc[2,1] = 'X'
        if a == 5:
            x.loc[2,2] = 'X'
        if a == 6:
            x.loc[2,3] = 'X'
        if a == 7:
            x.loc[3,1] = 'X'
        if a == 8:
            x.loc[3,2] = 'X'
        if a == 9:
            x.loc[3,3] = 'X'
        w.remove(a)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    fn3()

#human v/s human mode completed
#-------------------#
#-------------------#
#-------------------#

#computer v/s computer mode
if n==4:
    #creation of dataframe with indexing of both column and row as [1,2,3]
    a={1:1,2:2,3:3}
    b={1:4,2:5,3:6}
    c={1:7,2:8,3:9}
    x=pd.DataFrame([a,b,c],index=[1,2,3])
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('')
    w=[1,2,3,4,5,6,7,8,9]
    time.sleep(1.5)

#--------------------------------------#
#compa.b means computer a's bth chance
#time delay is added 2.5 second after every move so the moves can be observed

#comp1.1
    print('Computer-X')
    a=r.randint(1,9)
    while a not in w:
        a=r.randint(1,9)

    if a in w:
        if a == 1:
            x.loc[1,1] = 'X'
        if a == 2:
            x.loc[1,2] = 'X'
        if a == 3:
            x.loc[1,3] = 'X'
        if a == 4:
            x.loc[2,1] = 'X'
        if a == 5:
            x.loc[2,2] = 'X'
        if a == 6:
            x.loc[2,3] = 'X'
        if a == 7:
            x.loc[3,1] = 'X'
        if a == 8:
            x.loc[3,2] = 'X'
        if a == 9:
            x.loc[3,3] = 'X'
        w.remove(a)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    print('')
    time.sleep(2.5)

#comp2.1    
    print('Computer-O')
    c=r.randint(1,9)
    while c not in w:
        c=r.randint(1,9)

    if c in w:
        if c == 1:
            x.loc[1,1] = 'O'
        if c == 2:
            x.loc[1,2] = 'O'
        if c == 3:
            x.loc[1,3] = 'O'
        if c == 4:
            x.loc[2,1] = 'O'
        if c == 5:
            x.loc[2,2] = 'O'
        if c == 6:
            x.loc[2,3] = 'O'
        if c == 7:
            x.loc[3,1] = 'O'
        if c == 8:
            x.loc[3,2] = 'O'
        if c == 9:
            x.loc[3,3] = 'O'
        w.remove(c)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    print('')
    time.sleep(2.5)

#comp1.2
    print('Computer-X')
    a=r.randint(1,9)
    while a not in w:
        a=r.randint(1,9)

    if a in w:
        if a == 1:
            x.loc[1,1] = 'X'
        if a == 2:
            x.loc[1,2] = 'X'
        if a == 3:
            x.loc[1,3] = 'X'
        if a == 4:
            x.loc[2,1] = 'X'
        if a == 5:
            x.loc[2,2] = 'X'
        if a == 6:
            x.loc[2,3] = 'X'
        if a == 7:
            x.loc[3,1] = 'X'
        if a == 8:
            x.loc[3,2] = 'X'
        if a == 9:
            x.loc[3,3] = 'X'
        w.remove(a)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    print('')
    time.sleep(2.5)

#comp2.2
    print('Computer-O')
    c=r.randint(1,9)
    while c not in w:
        c=r.randint(1,9)

    if c in w:
        if c == 1:
            x.loc[1,1] = 'O'
        if c == 2:
            x.loc[1,2] = 'O'
        if c == 3:
            x.loc[1,3] = 'O'
        if c == 4:
            x.loc[2,1] = 'O'
        if c == 5:
            x.loc[2,2] = 'O'
        if c == 6:
            x.loc[2,3] = 'O'
        if c == 7:
            x.loc[3,1] = 'O'
        if c == 8:
            x.loc[3,2] = 'O'
        if c == 9:
            x.loc[3,3] = 'O'
        w.remove(c)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    print('')
    time.sleep(2.5)

#comp1.3
    print('Computer-X')
    a=r.randint(1,9)
    while a not in w:
        a=r.randint(1,9)

    if a in w:
        if a == 1:
            x.loc[1,1] = 'X'
        if a == 2:
            x.loc[1,2] = 'X'
        if a == 3:
            x.loc[1,3] = 'X'
        if a == 4:
            x.loc[2,1] = 'X'
        if a == 5:
            x.loc[2,2] = 'X'
        if a == 6:
            x.loc[2,3] = 'X'
        if a == 7:
            x.loc[3,1] = 'X'
        if a == 8:
            x.loc[3,2] = 'X'
        if a == 9:
            x.loc[3,3] = 'X'
        w.remove(a)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    print('')
    fn1()
    time.sleep(2.5)

#comp2.3
    print('Computer-O')
    c=r.randint(1,9)
    while c not in w:
        c=r.randint(1,9)

    if c in w:
        if c == 1:
            x.loc[1,1] = 'O'
        if c == 2:
            x.loc[1,2] = 'O'
        if c == 3:
            x.loc[1,3] = 'O'
        if c == 4:
            x.loc[2,1] = 'O'
        if c == 5:
            x.loc[2,2] = 'O'
        if c == 6:
            x.loc[2,3] = 'O'
        if c == 7:
            x.loc[3,1] = 'O'
        if c == 8:
            x.loc[3,2] = 'O'
        if c == 9:
            x.loc[3,3] = 'O'
        w.remove(c)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    print('')
    fn2()
    time.sleep(2.5)

#comp1.4
    print('Computer-X')
    a=r.randint(1,9)
    while a not in w:
        a=r.randint(1,9)

    if a in w:
        if a == 1:
            x.loc[1,1] = 'X'
        if a == 2:
            x.loc[1,2] = 'X'
        if a == 3:
            x.loc[1,3] = 'X'
        if a == 4:
            x.loc[2,1] = 'X'
        if a == 5:
            x.loc[2,2] = 'X'
        if a == 6:
            x.loc[2,3] = 'X'
        if a == 7:
            x.loc[3,1] = 'X'
        if a == 8:
            x.loc[3,2] = 'X'
        if a == 9:
            x.loc[3,3] = 'X'
        w.remove(a)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    print('')
    fn1()
    time.sleep(2.5)

#comp2.4
    print('Computer-O')
    c=r.randint(1,9)
    while c not in w:
        c=r.randint(1,9)

    if c in w:
        if c == 1:
            x.loc[1,1] = 'O'
        if c == 2:
            x.loc[1,2] = 'O'
        if c == 3:
            x.loc[1,3] = 'O'
        if c == 4:
            x.loc[2,1] = 'O'
        if c == 5:
            x.loc[2,2] = 'O'
        if c == 6:
            x.loc[2,3] = 'O'
        if c == 7:
            x.loc[3,1] = 'O'
        if c == 8:
            x.loc[3,2] = 'O'
        if c == 9:
            x.loc[3,3] = 'O'
        w.remove(c)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    print('')
    fn2()
    time.sleep(2.5)

#comp1.5
    print('Computer-X')
    a=r.randint(1,9)
    while a not in w:
        a=r.randint(1,9)

    if a in w:
        if a == 1:
            x.loc[1,1] = 'X'
        if a == 2:
            x.loc[1,2] = 'X'
        if a == 3:
            x.loc[1,3] = 'X'
        if a == 4:
            x.loc[2,1] = 'X'
        if a == 5:
            x.loc[2,2] = 'X'
        if a == 6:
            x.loc[2,3] = 'X'
        if a == 7:
            x.loc[3,1] = 'X'
        if a == 8:
            x.loc[3,2] = 'X'
        if a == 9:
            x.loc[3,3] = 'X'
        w.remove(a)
    print(tabulate(x.rename(columns={1:'Tic',2:'Tac',3:'Toe'}), headers = 'keys', tablefmt = 'fancy_grid', showindex=False, numalign='left'))
    print('Remaining: ',w)
    print('')
    fn3()

#computer v/s computer mode completed

#------------------#
#------------------#
#------------------#