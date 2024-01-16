import random
import time
rps = True
while rps:
    rps=["rock","paper","scissors"]
    comp=random.choice(rps)
    print("Please choose from the following:")
    print("r. Rock\np. Paper\ns. Scissors")
    option = input().lower()
    print("Here's the computer's answer:")
    print(comp)
    print("Here's your answer:")
    print(option)
    print("So the result is a")
    # player wins/lose
    if (comp == "paper" and option == "r") or (comp == "rock" and option == "p") or (comp == "scissors" and option == "s"):
        print("player wins")
    elif (comp == "rock" and option == "s") or (comp == "scissors" and option == "p") or (comp == "paper" and option == "r"):
        print("player loses")
    # ties
    elif comp == option:
        print("tie")
    # invalid options
    else:
        print("An invalid option. Please enter one of the following: r, p, s, or evem one of the coresponding words so rock, paper or scissors also works")
    print("")
    time.sleep(1) 
    play_again = input("Y. another game? N. exit\n")
    if play_again.lower() == "y" or play_again.lower() == "yes":
        print("Let's go again!")
        rps = True
    elif play_again.lower() == "n" or play_again.lower() == "no":
        rps = False
        print("Exiting.")
    else:
        print("Invalid input. Exiting.")
        rps = False
    print("")
