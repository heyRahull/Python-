print("\n--------------------------------THIS IS A NUMBER GUESSING GAME-------------------------------------\n")

print("YOU HAVE 8 GUESSES TO PLAY THE GAME : ")
print("The original number is a number between 1 to 100")
print("Guess  your number between 1 to 100")
num = 5
for x in range(1, 9):
    print("\nThis is your Guess : ", x)
    guess = int(input("Enter Your guess : "))
    if guess < num:
        print("The number you guessed is SMALLER than the original number")
    elif guess == 5:
        print("This is the original number")
        print("\n----------------CONGRATS, YOU HAVE WON THE GAME-----------------------------")
        print("The number of Guesses that you took is : ", x)
        break;
    else:
        print("The number you guessed is LARGER than the original number")

while x == 8:
    print("\nYour Guesses are finished")
    print("GAME OVER")
    break;