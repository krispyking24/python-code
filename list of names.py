def printNames():
    index=0
    while index < len(names):
        print(str(index+1)+". "+names[index])
        index = index + 1

cont = True
names=[]
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

while cont:
    print("plese chose from the following:")
    print("a.enter a name")
    print("b.find a name")
    print("c.delete a name")
    print("d.time")
    print("e.exit")
    
    option=input()

    if option=="a":
        n=input("what is a name? ")
        names.append(n)
        print("thanks for the name.")
    elif option=="b":
        if names==[]:
            print("you dont have a name?")
        else:
            print("your names are: ")
            printNames()
    elif option=="c":
        print("please select from the following names to remove")
        printNames()
        f=input()
        names.pop(int(f)-1)
        print("you have been erased from earth.")
    elif option=="e":
        cont=False
        print("exiting")
    elif option=="d":
        print("date and time =", dt_string)
        print("now =", now)
    else:
        print("invalid option. please enter one of the following a, b, c, d")
    print("")
