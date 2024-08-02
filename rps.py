import random
import time
import os
#clear screen code from https://github.com/Nadelio/SOTF/blob/main/GAMEFILES/clear_screen.py
windows_os_name = "nt"
# Commands for each OS to clear the terminal
clear_screen_command_windows = "cls"
clear_screen_command_other = "clear"
# Clear the terminal screen
def clear_screen():
    os.system(clear_screen_command_windows if os.name==windows_os_name else clear_screen_command_other)
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
        print("Win")
    elif (comp == "rock" and option == "s") or (comp == "scissors" and option == "p") or (comp == "paper" and option == "r"):
        print("Loss")
    # ties
    elif comp == option:
        print("Tie")
    # invalid options
    else:
        print("An invalid option. Please enter one of the following: r, p, s, or one of the coresponding words so rock, paper or scissors also works")
    print("")
    time.sleep(1) 
    play_again = input("Y. another game? N. exit\n")
    if play_again.lower() == "y" or play_again.lower() == "yes":
        print("Let's go again!")
        rps = True
        clear_screen()
    elif play_again.lower() == "n" or play_again.lower() == "no":
        rps = False
        print("Exiting.")
    else:
        print("Invalid input. Exiting.")
        rps = False
    print("")
