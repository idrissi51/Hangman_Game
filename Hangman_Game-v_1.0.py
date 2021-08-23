import random

print("Welcome to Hangman game by DataFlair")
user_name = input("Entry Your name: ").strip().capitalize()
print("Hello "+user_name+"! Best of Luck!")
print("The game is about to start!\n    Let's play Hangman!")


def main():
    global word
    global display
    global count
    global length
    global already_guessed
    words_to_guess = ["january", "border", "image", "film",
                      "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]
    word = random.choice(words_to_guess)
    print(word)
    length = len(word)
    display = "_" * length
    count = 0
    already_guessed = []


def play():
    global already_guessed
    global count
    global display
    global word
    limit = 5
    print("This id the Hangman Word: " + display + " Entry your guess")
    guess = input("=> ").strip()
    if len(guess) != 1:
        print("Invalid Input, Try a letter")
        play()
    else:
        if guess in word:
            x = word.find(guess)
            already_guessed.extend(guess)
            word = word[:x] + "_" + word[x + 1:]
            display = display[:x] + guess + display[x+1:]
            if word == "_" * length:
                print(display)
                print("Congrats! You have guessed the word correctly!")
                play_again()
            else:
                play()
        elif guess not in word:
            count += 1
            if count == 5:
                print("Wrong guess. You are hanged!!!")
                print("The word was: ", already_guessed, word)
                play_again()

            else:
                print(f"Wrong guess {limit - count} guesses remaining")

                play()


def play_again():
    print("Do You want to play again? y = yes, n = no")
    opt = input("=> ")
    if opt == "y":
        main()
        play()
    elif opt == "n":
        print("Thanks For Playing! We expect you back again!")
        exit()
    else:
        play_again()


main()
play()
