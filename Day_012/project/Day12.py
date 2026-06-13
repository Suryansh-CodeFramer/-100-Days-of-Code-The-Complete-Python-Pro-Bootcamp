import random

print("Welcome to Number Gussing Game!")
print("I'm thinking of a number between 1 and 100")
computerGeneratedNumber = random.randint(1,100)
win=100
def gussing(num, noOfAttempts):

    if computerGeneratedNumber == num:
        print("You guessed the number")
        win=1000


    elif computerGeneratedNumber > num:
        print("Too low")
        print("no. of attempt left ", noOfAttempts)
    elif computerGeneratedNumber < num:
        print("Too high")
        print("no. of attempt left ", noOfAttempts)
    else:
        print("GUSSED NUMBER NOT IN THE RANGE ")
        print("no. of attempt left ", noOfAttempts)


def easy():
    print("You have 10 attempsts remaining")
    noOfAttempts = 0
    for i in range(10):
        noOfAttempts += 1
        num = int(input("Enter a number: "))
        gussing(num, noOfAttempts)
        if win==1000:
            break
        if noOfAttempts==10:
            print("You guessed the number", computerGeneratedNumber)






def hard():
    print("You have 5 attempsts remaining")
    noOfAttempts = 0
    for i in range(5):
        noOfAttempts += 1
        num = int(input("Enter a number: "))
        gussing(num, noOfAttempts)
        if win==1000:
            break
        if noOfAttempts==5:
            print("guessed the number", computerGeneratedNumber)

Difficulty = input("What is your difficulty? Type 'easy' or 'hard': ")
if Difficulty == "easy":
    easy()
elif Difficulty == "hard":
    hard()
else:
    print("Sorry, I didn't understand your difficulty")



