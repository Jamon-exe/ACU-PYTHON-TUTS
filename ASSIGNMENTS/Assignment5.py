import random as rd

randomnumber = rd.randint(1, 100)
guess = 0
while randomnumber != guess:
    guess = int(input("Enter a number between 1 and 100: "))
    randomnumber = rd.randint(1, 100)
    if guess < randomnumber:
        print("Too low")
    elif guess > randomnumber:
        print("Too high")
    else:
        print("You guessed it!")
        break
    print(randomnumber)