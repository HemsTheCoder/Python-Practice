# Here using conditional statement, loop,function we will create a game know as "Rock Paper Sissor".
import random

def won(comp,player):
    if comp==player:
       print("Match is draw both have chosen same option.")
    elif comp=='r':
        if player=='p':
           print("************************Player Won*************************")
           print(f"Computer chose '{comp}' and player chose '{player}' , so Paper covered the Rock and computer lost....")
        else:
           print("************************Computer Won*************************")
           print(f"Computer chose '{comp}' and player chose '{player}' , so rock distroyed the sissor and player lost....")
    elif comp=='p':
        if player=='s':
           print("************************Player Won*************************")
           print(f"Computer chose '{comp}' and player chose '{player}' , so sissor cuts the paper and computer lost....")
        else:
            print("************************Computer Won*************************")
            print(f"Computer chose '{comp}' and player chose '{player}' ,so Paper covered the Rock and player lost....")
    elif comp=='s':
        if player=='r':
            print("************************Player Won*************************")
            print(f"Computer chose '{comp}' and player chose '{player}' , so rock distroyed the sissor and computer lost....")
        else:
            print("************************Computer Won*************************")
            print(f"Computer chose '{comp}' and player chose '{player}' , so sissor cuts the paper and computer lost....")
ranum=random.randint(1,3)
comp=0
print("computer chosen the option..")
player=input("Player turn: Select your option (r)rock ,(p) paper,(s) sissor:")

if ranum==1:
    comp='s'
elif ranum==2:
    comp='p'
elif ranum==3:
    comp='r'

won(comp,player)
