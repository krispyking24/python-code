import random
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
            game=True
            guesses=0
        elif again=="no" or again=="n":
            game=False
            break
    if guesses==11:
        print("too many guesses, the number was", num)
        again=input("would like to go again? ")
        if again=="yes" or again=="y":
            game=True
            guesses=0
            num=(random.randint(1, 100))
        elif again=="no" or again=="n":
            game=False
            break
    if guesses==10:
        print("last guess")
