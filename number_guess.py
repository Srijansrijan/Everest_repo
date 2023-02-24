import random as rd

number = rd.randint(1, 50)

num_guesses = 0

while True:

    guess = int(input("Guess a number between 1 and 50: "))
    num_guesses += 1
    if guess < number:
        print("umm!! your guess is too low.")
    elif guess > number:
        print("Too high Guess!!")
    else:
        print(f"Congratulations, you guessed the correct number.")
        break
