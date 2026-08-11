#ask user input
#let computer choose the choice
#if user choice equal to computer choice then tie


import random

choices=['r','p','s']
emojis={'r':'🪨','p':'📰','s':'✂️'}

while True:
    user_choice=input("rock/paper/sciccer (r/p/s):").lower()
    computer_choice=random.choice(choices)

    print(f"you choose {emojis[user_choice]}")
    print(f"computer choice {emojis[computer_choice]} ")

    if user_choice==computer_choice:
        print("tie!")
    elif (user_choice=='r' and computer_choice=='s')\
    or (user_choice=='s' and computer_choice=='p')\
    or (user_choice=='p' and computer_choice=='r'):
        print("you win.")
    else:
        print("you lost..")
    user=input("do you want to play again (Y/N):  ").lower()
    if user=='y':
        continue
    elif user=='n':
        print("Thank you ....")
        break
    else:
        print("enter correct choice.")