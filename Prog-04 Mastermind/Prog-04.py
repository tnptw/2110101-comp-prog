# Prog-04: Mastermind Game

import random
import math

WINNING_MSG = "Congratulations! You won the game."
LOSING_MSG = "Sorry! You just lost it."

code = ''.join(random.sample('ABCDEF', 4))

print('Please guess the puzzle code using')
print('the four distinct code characters from [A to F]:')

#---------------------------------------------------

P = 0; V = 0; X = 0
decode = input('Turn #1 : ')
if decode[0] == code[0] :
    P += 1
elif decode[0] in code :
    V += 1
else :
    X += 1
if decode[1] == code[1] :
    P += 1
elif decode[1] in code :
    V += 1
else :
    X += 1
if decode[2] == code[2] :
    P += 1
elif decode[2] in code :
    V += 1
else :
    X += 1
if decode[3] == code[3] :
    P += 1
elif decode[3] in code :
    V += 1
else :
    X += 1
if P == 4 :
    print(WINNING_MSG)
if P != 4 :
    print('     '+'     '+'P='+str(P)+','+'V='+str(V)+','+'X='+str(X))
    P = 0; V = 0; X = 0
    decode = input('Turn #2 : ')
    if decode[0] == code[0] :
        P += 1
    elif decode[0] in code :
        V += 1
    else :
        X += 1
    if decode[1] == code[1] :
        P += 1
    elif decode[1] in code :
        V += 1
    else :
        X += 1
    if decode[2] == code[2] :
        P += 1
    elif decode[2] in code :
        V += 1
    else :
        X += 1
    if decode[3] == code[3] :
        P += 1
    elif decode[3] in code :
        V += 1
    else :
        X += 1
    if P == 4 :
        print(WINNING_MSG)
    if P != 4 :
        print('     '+'     '+'P='+str(P)+','+'V='+str(V)+','+'X='+str(X))
        P = 0; V = 0; X = 0
        decode = input('Turn #3 : ')
        if decode[0] == code[0] :
            P += 1
        elif decode[0] in code :
            V += 1
        else :
            X += 1
        if decode[1] == code[1] :
            P += 1
        elif decode[1] in code :
            V += 1
        else :
            X += 1
        if decode[2] == code[2] :
            P += 1
        elif decode[2] in code :
            V += 1
        else :
            X += 1
        if decode[3] == code[3] :
            P += 1
        elif decode[3] in code :
            V += 1
        else :
            X += 1
        if P == 4 :
            print(WINNING_MSG)
        if P != 4 :
            print('     '+'     '+'P='+str(P)+','+'V='+str(V)+','+'X='+str(X))
            P = 0; V = 0; X = 0
            decode = input('Turn #4 : ')
            if decode[0] == code[0] :
                P += 1
            elif decode[0] in code :
                V += 1
            else :
                X += 1
            if decode[1] == code[1] :
                P += 1
            elif decode[1] in code :
                V += 1
            else :
                X += 1
            if decode[2] == code[2] :
                P += 1
            elif decode[2] in code :
                V += 1
            else :
                X += 1
            if decode[3] == code[3] :
                P += 1
            elif decode[3] in code :
                V += 1
            else :
                X += 1
            if P == 4 :
                print(WINNING_MSG)
            if P != 4 :
                print('     '+'     '+'P='+str(P)+','+'V='+str(V)+','+'X='+str(X))
                print(LOSING_MSG)
                print('The answer is ', code)
                print('Please try again...')