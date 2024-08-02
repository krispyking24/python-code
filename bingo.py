#game name is bingo
#random is used for the rng of the grid numbers
import random
#time is imported as its used for the game timer
import time
import os
try:
    #used to auto exit the program if you say no to continuing to play the game look at line 120
    from pynput.keyboard import Key, Controller
    keyboard=Controller()
    pynput_available = True
except ModuleNotFoundError:
    pynput_available = False
    print("pynput not found please install pynput for full function")
def getNum():
    global numbers
    num=random.choice(numbers)
    numbers.remove(num)
    return {"num": num, "chosen":False}
def printAll(choice):
    global row1,row2,row3,row4
    #prints the bingo card
    if choice=="num":
        print("    1    2    3    4")
        print("  ┌────┬────┬────┬────┐")
        printRow(row1, 1), print("  ├────┼────┼────┼────┤")
        printRow(row2, 2), print("  ├────┼────┼────┼────┤")
        printRow(row3, 3), print("  ├────┼────┼────┼────┤")
        printRow(row4, 4)
        print("  └────┴────┴────┴────┘")
    #prints the grid of 1 and 0 used to say if the player has marked that square
    elif choice=="true":
        print("1=true/marked, 0=false/not marked")
        print("  ┌────┬────┬────┬────┐")
        print_t_f(row1, " "), print("  ├────┼────┼────┼────┤")
        print_t_f(row2, " "), print("  ├────┼────┼────┼────┤")
        print_t_f(row3, " "), print("  ├────┼────┼────┼────┤")
        print_t_f(row4, " ")
        print("  └────┴────┴────┴────┘")
        print("1=true/marked, 0=false/not marked")
def printRow(row, num):
    print(num, "│",'{:2d}'.format(row[0]["num"]),"│", '{:2d}'.format(row[1]["num"]),"│", '{:2d}'.format(row[2]["num"]),"│", '{:2d}'.format(row[3]["num"]),"│")
def print_t_f(row, num):
    print(num, "│",'{:2d}'.format(row[0]["chosen"]),"│", '{:2d}'.format(row[1]["chosen"]),"│", '{:2d}'.format(row[2]["chosen"]),"│", '{:2d}'.format(row[3]["chosen"]),"│")
def setTrue(row, col):
    global row1,row2,row3,row4
    if row==1:
        row1[col-1]["chosen"]=True
    elif row==2:
        row2[col-1]["chosen"]=True
    elif row==3:
        row3[col-1]["chosen"]=True
    elif row==4:
        row4[col-1]["chosen"]=True
def getrow(row):
    return [row[0]["chosen"], row[1]["chosen"], row[2]["chosen"], row[3]["chosen"]]
def getcol(col):
    return [row1[col]["chosen"], row2[col]["chosen"], row3[col]["chosen"], row4[col]["chosen"]]
def checkwin():
    global row1,row2,row3,row4,num
    won = False
    if getrow(row1) == [True, True, True, True]:
        won = True
    elif getrow(row2) == [True, True, True, True]:
        won = True
    elif getrow(row3) == [True, True, True, True]:
        won = True
    elif getrow(row4) == [True, True, True, True]:
        won = True
    elif getcol(0) == [True, True, True, True]:
        won = True
    elif getcol(1) == [True, True, True, True]:
        won = True
    elif getcol(2) == [True, True, True, True]:
        won = True
    elif getcol(3) == [True, True, True, True]:
        won = True
    if won:
        print("you have won" )
        print("the game took", round(time.time() - start_time, 3), "seconds to run")
    return won
def reset():
    global numbers, row1, row2, row3, row4, start_time
    clear_screen()
    numbers = [i + 1 for i in range(50)]
    row1 = [getNum() for _ in range(4)]
    row2 = [getNum() for _ in range(4)]
    row3 = [getNum() for _ in range(4)]
    row4 = [getNum() for _ in range(4)]
    start_time = time.time()
    
#clear screen code from https://github.com/Nadelio/SOTF/blob/main/GAMEFILES/clear_screen.py
windows_os_name = "nt"
# Commands for each OS to clear the terminal
clear_screen_command_windows = "cls"
clear_screen_command_other = "clear"
# Clear the terminal screen
def clear_screen():
     os.system(clear_screen_command_windows if os.name==windows_os_name else clear_screen_command_other)

print("mark 4 numbers in a row to win")
numbers=[]
number=random.randint(1,10)
start_time=time.time()
for i in range(50):
    numbers.append(i+1)
row1=[getNum() for _ in range(4)]
row2=[getNum() for _ in range(4)]
row3=[getNum() for _ in range(4)]
row4=[getNum() for _ in range(4)]
#print the numbers that got taken out
#print(numbers)
choice=""
choice2=""
while True:
    if checkwin():
        again=input("want to play again? ").lower()
        if again=="n" or again=="no":
            print("the game was running for", round(time.time() - start_time, 3),"seconds")
            if pynput_available:
                time.sleep(8)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
            exit()
        elif again=="y" or again=="yes":
            reset()
    printAll("num")
    number=random.randint(1,50)
    print("The number is",number)
    numyes=input("do you have the number shown? ").lower()
    if numyes=="y" or numyes=="yes":
        print("from where in the grid do you have any of the numbers shown")
        col_choice=int(input("col: "))
        row_choice=int(input("row: "))
        setTrue(row_choice,col_choice)
        checkwin()
    print("numbers that you have marked that are on the grid")
    printAll("true")
    choice=input("do you want a new number? ").lower()
    if choice=="n" or choice=="no":
        continue_=input("are you sure you would like to quit? ").lower()
        if continue_=="y" or choice=="yes":
            print("the game was running for", round(time.time() - start_time, 3),"seconds")
            if pynput_available:
                time.sleep(8)
                keyboard = Controller()
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
            exit()
        elif continue_=="n" or choice=="no":
            print("the game has been running so far for", round(time.time() - start_time, 3),"seconds")
