import random

name = input ("what is your name?" )

print("Good Luck", name)

words = ['rainbow', 'bridge','quary','sunshine']

word = random.choice(words)

print("Guess the character")

guesses = ''

turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You win!")
        print("The words is", word)
        break

    print()
    guess = input("Guess this character:")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", +turns, 'more guesses')

        if turns == 0:
            print("You lose")
