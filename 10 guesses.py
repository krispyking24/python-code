import random
import os
#clear screen code from https://github.com/Nadelio/SOTF/blob/main/GAMEFILES/clear_screen.py
windows_os_name = "nt"
# Commands for each OS to clear the terminal
clear_screen_command_windows = "cls"
clear_screen_command_other = "clear"
# Clear the terminal screen
def clear_screen():
    os.system(clear_screen_command_windows if os.name==windows_os_name else clear_screen_command_other)
num=(random.randint(1, 100))
guesses=0
while True:
    game=True
    print("number of guesses taken", guesses)
    guess=int(input("Please guess a number between 1 and 100: "))
    if guess<num:
        print("too low")
        guesses=guesses+1
    elif guess>num:
        print("too high")
        guesses=guesses+1
    elif guess==num:
        print("correct")
        again=input("would like to go again? ")
        if again=="yes" or again=="y":
            num=(random.randint(1, 100))
            game=True
            guesses=0
            clear_screen()
        elif again=="no" or again=="n":
            game=False
            break
    if guesses==11:
        print("too many guesses, the number was", num)
        again=input("would like to go again? ")
        if again=="yes" or again=="y":
            num=(random.randint(1, 100))
            game=True
            guesses=0
            clear_screen()
        elif again=="no" or again=="n":
            game=False
            break
    if guesses==10:
        print("last guess")
