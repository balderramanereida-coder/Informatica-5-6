#Add an "inport random" before the main function
#Define main function
#Use print function to make the welcome to the user
#
#
#
#
#
#
#
#
#
#
#
#





import random
def main():
    start_game("random_w.txt")
print("Welcome to the HangMan game!")
def start_game(file):

    with open(file) as random_w:
        content = random_w.read().splitlines()
        secret_word = random.choice(content)
        secret_word = (["_"] * len(secret_word))
    print(" ".join(secret_word))

    while True:
        guess = input("Take a guess: ")
        if len(guess) == 1:
            break
        else:
            print("Invalid guess. Try again.")

    for i in secret_word:
        if guess == i


if __name__ == "__main__":
    main()

