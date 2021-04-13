import random
name = input("Welcome to pacifistwordgames.com. What's your name? ")
print("Good luck, " + name, ", not like anyone's life depends on it.")

fruits = ['apple', 'banana', 'pear', 'tomato', 'peach',
          'watermelon', 'cantaloupe', 'grape', 'blueberry', 'raspberry']
word = random.choice(fruits)
print("\nGuess a letter ")
guesses = ""

turns = 7
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_ ", end="")
            failed += 1
    if failed == 0:
        print("\nYa did it!")
        print("\nThe word was: ", word)
        break

    guess = input("\nGuess a letter: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("\nNah")
        print("\nYou have ", +turns, "more guesses")

        if turns == 0:
            print("\nGame Over")
