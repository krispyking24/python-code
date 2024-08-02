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
start_time = time.time()
rejected=True
def Checkwin():
    #player 1 winning below
    #horizontal player 1 win states 
    if row1==["x","x","x"]:
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("player 1 is a winner")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
        else:
            exit()
    elif row2==["x","x","x"]:
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("player 1 is a winner")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
        else:
            exit()
    elif row3==["x","x","x"]:
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("player 1 is a winner")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
        else:
            exit()
    #vertical player 1 win states
    elif row1[0] == "x" and row2[0] == "x" and row3[0] == "x":
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("player 1 is a winner")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
        else:
            exit()
    elif row1[1] == "x" and row2[1] == "x" and row3[1] == "x":
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("player 1 is a winner")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
        else:
            exit()
    elif row1[2] == "x" and row2[2] == "x" and row3[2] == "x":
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("player 1 is a winner")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
        else:
            exit()
    #diagonal player 1 win states
    elif row1[0] == "x" and row2[1] == "x" and row3[2] == "x":
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("player 1 is a winner")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
        else:
            exit()
    elif row1[2] == "x" and row2[1] == "x" and row3[0] == "x":
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("player 1 is a winner")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
        else:
            exit()
    #player 2 winning below
    #horizontal player 2 win states 
    elif row1==["o","o","o"]:
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("player 2 is a winner")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
        else:
            exit()
    elif row2==["o","o","o"]:
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("player 2 is a winner")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
        else:
            exit()
    elif row3==["o","o","o"]:
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("player 2 is a winner")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
        else:
            exit()
    #vertical player 2 win states
    elif row1[0] == "o" and row2[0] == "o" and row3[0] == "o":
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("player 2 is a winner")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
    elif row1[1] == "o" and row2[1] == "o" and row3[1] == "o":
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("player 2 is a winner")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
    elif row1[2] == "o" and row2[2] == "o" and row3[2] == "o":
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("player 2 is a winner")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
        else:
            exit()
    #diagonal player 2 win states
    elif row1[0] == "o" and row2[1] == "o" and row3[2] == "o":
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("player 2 is a winner")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
        else:
            exit()
    elif row1[2] == "o" and row2[1] == "o" and row3[0] == "o":
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("player 2 is a winner")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
        else:
            exit()
    #check for a tie
    elif " " not in row1 and " " not in row2 and " " not in row3:
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
        print("It's a tie!")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y" or play_again.lower() == "yes":
                reset_game()
        else:
            exit()
def reset_game():
    clear_screen()
    global row1, row2, row3
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]
    printgrid()
def printgrid():
    print("    1   2   3")
    print("  -------------")
    print("1 |" " " + row1[0] + " | " + row1[1] + " | " + row1[2], "|") 
    print("  -------------")
    print("2 |" " " + row2[0] + " | " + row2[1] + " | " + row2[2], "|")
    print("  -------------")
    print("3 |" " " + row3[0] + " | " + row3[1] + " | " + row3[2], "|")
    print("  -------------")
row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]
player="1"
playersymbol="x"
printgrid()
while True:
    wrong=True
    while wrong:
        print("player "+ player + "'s turn")
        y=input("choose a row (1, 2 or 3): ")
        if y not in ["1", "2", "3"]:
            print("Invalid input. Please enter a valid row number (1, 2 or 3)")
        try:
            x=int(input("choose a column (1, 2 or 3): "))-1
            rejected = False
            if y=="1" and row1[x]==" ":
                row1[x]=playersymbol
                wrong=False
            elif y=="2" and row2[x]==" ":
                row2[x]=playersymbol
                wrong=False
            elif y=="3" and row3[x]==" ":
                row3[x]=playersymbol
                wrong=False
            else:
                print("do better and try to use your brain")
        except:
            print("Invalid input. Please enter a valid integer.")
            rejected = True
        wrong=False
    if not rejected:
        if player=="1":
            player="2"
            playersymbol="o"
        else:
            player="1"
            playersymbol="x"
        clear_screen()
        printgrid()
        Checkwin()
