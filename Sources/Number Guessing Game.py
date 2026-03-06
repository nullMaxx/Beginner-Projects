import math, random

print("Welcome to the Number GUESSING GAME!")

low = int(input("Enter the lower bound number: "))
high = int(input("Enter the highper bound number: "))

tries = math.ceil(math.log2(high - low + 1))
print(f"\nYou have {tries} chances to guess the number between {low} and {high}. Let\'s start!")

number = random.randint(low,high)
guess_count = 0

while guess_count < tries:
    guess = int(input("Enter your guess: "))
    
    if guess < low or guess > high:
        print("Please enter appropriate number.")
        continue

    if not isinstance(guess, int):
        print("Please enter a number.")
        continue

    guess_count += 1

    if guess < number:
        print("Your number too small.")
    elif guess > number:
        print("Your number too big.")
    else:
        print("Congratulations! You gueesed the number!")
        break