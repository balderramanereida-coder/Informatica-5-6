#Add an "inport random" before the main function
#Define main function
#Use print function to make the welcome to the user
#I stablished a new function so i can start the game by using variables related to the game and also import my txt file content into a list
#We use the first "while loop" so we can start working with our attempts variables
#Now that we have attempts, our secret word and the user input part, we can start with a "while true"
#We specified our rules with the if,elif and else
#use break inside your while so you can work with differet user answers



#Code:

import random
def main():
    start_game("random_w.txt")

print("Welcome to the HangMan game!")

def start_game(file):
    attempts = 10
    with open(file) as random_w:
        content = random_w.read().splitlines()
    secret_word = random.choice(content)
    hint = (["_"] * len(secret_word))
    incorrect_letters = []

    while attempts > 0:
        print("Current word:", " ".join(hint))

        while True:
            guess = input("Take a guess: ").lower()
            if len(guess) == 1:
                break
            else:
                print("Invalid guess. Try again.")

        if guess in secret_word and guess not in hint:
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    hint[i] = guess
            print("Great guess!")
        elif guess in hint:
            attempts -= 1
            print("You already guessed that letter! Attempts left:", str(attempts))
        else:
            attempts -= 1
            print("Wrong guess! Attempts left:", str(attempts))
            if guess not in incorrect_letters:
                incorrect_letters.append(guess)
            print(f"Incorrect letters: {" ".join(incorrect_letters)}")

        if "_" not in hint:
            print("Congratulations!! You guessed the word:", secret_word)
            break
        if attempts == 0 and "_" in hint:
            print("No attempts left... The word was:", secret_word)



if __name__ == "__main__":
    main()

