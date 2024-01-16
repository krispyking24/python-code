import tkinter as tk
import tkinter.messagebox
def pressed(event):
    global player
    global playersymbol
    if event.widget["text"]==" ":
        event.widget.configure(text=playersymbol)
        checkwin()
        if player=="1":
            player="2"
            playersymbol="o"
        else:
            player="1"
            playersymbol="x" 
    else:
        tk.messagebox.showinfo(title=None, message="invalid box, choose an empty square")
        event.widget.configure(relief=tk.RAISED, state=tk.DISABLED)
def checkwin():
    global event, row1, row2, row3
    row1=[button[0]["text"],button[1]["text"],button[2]["text"]]
    row2=[button[3]["text"],button[4]["text"],button[5]["text"]]
    row3=[button[6]["text"],button[7]["text"],button[8]["text"]]
    print(row1)
    print(row2)
    print(row3)
    if row1==["x","x","x"]:
        tk.messagebox.showinfo(title=None, message="player 1 is a winner")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
    elif row2==["x","x","x"]:
        tk.messagebox.showinfo(title=None, message="player 1 is a winner")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
    elif row3==["x","x","x"]:
        tk.messagebox.showinfo(title=None, message="player 1 is a winner")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
    #vertical player 1 win states
    elif row1[0] == "x" and row2[0] == "x" and row3[0] == "x":
        tk.messagebox.showinfo(title=None, message="player 1 is a winner")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
    elif row1[1] == "x" and row2[1] == "x" and row3[1] == "x":
        tk.messagebox.showinfo(title=None, message="player 1 is a winner")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
    elif row1[2] == "x" and row2[2] == "x" and row3[2] == "x":
        tk.messagebox.showinfo(title=None, message="player 1 is a winner")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
    #diagonal player 1 win states
    elif row1[0] == "x" and row2[1] == "x" and row3[2] == "x":
        tk.messagebox.showinfo(title=None, message="player 1 is a winner")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
    elif row1[2] == "x" and row2[1] == "x" and row3[0] == "x":
        tk.messagebox.showinfo(title=None, message="player 1 is a winner")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
    #player 2 winning below
    #horizontal player 2 win states 
    elif row1==["o","o","o"]:
        tk.messagebox.showinfo(title=None, message="player 2 is a winner")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
    elif row2==["o","o","o"]:
        tk.messagebox.showinfo(title=None, message="player 2 is a winner")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
    elif row3==["o","o","o"]:
        tk.messagebox.showinfo(title=None, message="player 2 is a winner")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
    #vertical player 2 win states
    elif row1[0] == "o" and row2[0] == "o" and row3[0] == "o":
        tk.messagebox.showinfo(title=None, message="player 2 is a winner")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
    elif row1[1] == "o" and row2[1] == "o" and row3[1] == "o":
        tk.messagebox.showinfo(title=None, message="player 2 is a winner")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
    elif row1[2] == "o" and row2[2] == "o" and row3[2] == "o":
        tk.messagebox.showinfo(title=None, message="player 2 is a winner")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
    #diagonal player 2 win states
    elif row1[0] == "o" and row2[1] == "o" and row3[2] == "o":
        tk.messagebox.showinfo(title=None, message="player 2 is a winner")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
    elif row1[2] == "o" and row2[1] == "o" and row3[0] == "o":
        tk.messagebox.showinfo(title=None, message="player 2 is a winner")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
    #check for a tie
    elif " " not in row1 and " " not in row2 and " " not in row3:
        tk.messagebox.showinfo(title=None, message="It's a tie!")
        response=tkinter.messagebox.askyesno(title=None, message="do you want to play again?")
        print(response)
        if response==True:
            reset_game()
        elif response==False:
            quit()
def reset_game():
    global row1, row2, row3
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]
    for i in range(3):
        for j in range(3):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1)
            frame.grid(row=i, column=j)
            label = tk.Button(master=frame, text=" ", width=10,
                height=5, font=('Arial', 15))
            label.bind("<Button-1>", pressed)
            label.pack()
            button.append(label)
    print(row1)
    print(row2)
    print(row3)
    return False
player="1"
playersymbol="x"
button=[]
window = tk.Tk()
window.title("                                        Tic Tac Toe")
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1)
        frame.grid(row=i, column=j)
        label = tk.Button(master=frame, text=" ", width=10,
            height=5, font=('Arial', 15))
        label.bind("<Button-1>", pressed)
        label.pack()
        button.append(label)
window.mainloop()
button[0].configure(text="")
