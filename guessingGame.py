secretNumber = 29
guessCount = 0
while guessCount <3:
    guess = int(input("Your Guess: "))
    if guess == secretNumber:
        print("Congratulation!! You won")
        break
    guessCount += 1
else:
    print("You fail to guess")