name = "biniamin"
count = 0

while count < 10:
    print(name)
    count += 1

    import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guess = None

    print("I have selected a number between 1 and 100. Can you guess it?")

    while guess != number_to_guess:
        guess = int(input("Enter your guess: "))
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the correct number.")


guess_the_number()

