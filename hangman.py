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
    print(random.choice(content))

if __name__ == "__main__":
    main()

