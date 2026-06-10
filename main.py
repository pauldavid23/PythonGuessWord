import random

player_life = 3
random_words = ["LeBron", "Kobe", "Aardvark", "Jordan", "Trump"]
word = random.choice(random_words).lower()

display = ["_"] * len(word)

while player_life > 0:

    print("\nWord to guess: " + " ".join(display))
    print(f"Lives left: {player_life}")

    guess = input("Guess the letter: ").lower()


    if guess in word:

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct!")
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        player_life -= 1

    if "_" not in display:
        print(f"\nCongratulations! You guessed the word: {word.upper()} 🎉")
        break

if player_life == 0:
    print("\nGame over! You ran out of lives.")
    print(f"The word was: {word}")