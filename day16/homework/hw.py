# 1
count = 10
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Blast off!")

# 2
import random

number_to_guess = random.randint(1, 10)
guess = None

while guess != number_to_guess:
    guess = int(input("Guess the number (between 1 and 10): "))
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")

# 3
total = 0
number = 1

while number <= 100:
    total += number
    number += 1

print(f"The sum of numbers from 1 to 100 is: {total}")

# 4
correct_password = "password123"
input_password = ""

while input_password != correct_password:
    input_password = input("Enter the password: ")

print("Password accepted!")

# 5
number = 5
factorial = 1
i = 1

while i <= number:
    factorial *= i
    i += 1

print(f"The factorial of {number} is: {factorial}")
