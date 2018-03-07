import random
number = random.randint(1, 100)
flag=True
N=1
while flag== True:
    guessnumber=int(input("Enter a number between 1 - 100: "))
    if guessnumber<number:
        flag=True
        print("too low")
        N=N+1
    elif guessnumber>number:
        flag=True
        print("too high")
        N=N+1
    else:
        flag=False
        print("Well done! You guessed",number,"in",N,"guesses")
        