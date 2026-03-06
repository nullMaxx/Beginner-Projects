import random

words = ["apple", "pineapple", "elephant", "python", "water", "science", "letter", "friend", 
         "playground", "board", "condition", "reverse", "contribute", "polarity", "store", 
         "official", "house", "effect", "probability"]

word = random.choice(words)

print("Welcome to Word Guessing Game!")
print("In this game you need to enter the character and then you will see if there any.")
print("Please enter a lowercase english letters.\n")
print("I wished a word: ")

guesses = ""
turn = 0
while guesses != word:
    left = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            left += 1

    if left == 0:
        print("You won!")
        print("The word is: ", word)
        break

    guess = input("\nGuess the character: ")
    guesses += guess

    if guess not in word:
        print("Wrong character. Try again")
