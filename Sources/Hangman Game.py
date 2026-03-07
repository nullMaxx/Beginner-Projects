import random
from collections import Counter

Words = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut 
watermelon cherry papaya berry peach lychee muskmelon'''
Words = Words.split(' ')

word = random.choice(Words)

print("Welcome to Hangman Game! You need to guess a secret word. HINT: word is a fruit!")

for i in word:
    print("_", end=" ")
print()

letterGuessed = ""
flag = 0
chances = len(word) + 2

try:
    while chances > 0 and flag == 0:
        print()
        chances -= 1

        try:
            guess = input("Enter a letter to guess: ").lower()
        except:
            print("Please enter only a letter.")
            continue

        if not guess.isalpha():
            print("Please enter only a letter.")
            continue
        elif len(guess) > 1:
            print("Please enter only a single letter.")
            continue
        elif guess in letterGuessed:
            print("You have already guessed that letter!")
            continue

        if guess in word:
            letterGuessed += guess * word.count(guess)

        for char in word:
            if char in letterGuessed:
                print(char, end=" ")
            else:
                print("_", end=" ")

        if Counter(letterGuessed) == Counter(word):
            print("\nCongratulations! You guessed a word: ", word)
            flag = 1
            break
    if chances <= 0 and Counter(letterGuessed) != Counter(word):
        print("\nYou lost! The word was: ", word)

except KeyboardInterrupt:
    print("\nGame interrupt. Bye!")
    exit()