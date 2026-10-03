def main():

    print("Welcome to the times table quiz")
    while True:
        try:
            times_table = int(input("Enter a times table that you would like to be tested on (1-10): "))
        if 1 <= times_table <= 10:
            break
        print("Please enter a number between 1 and 10.")
            except ValueError:
        print("Invalid input. Please enter a valid whole number.")


    while True:
        try:
        max_value = int(input("Enter the maximum value for your times table: "))
        if max_value > 0:
        break
    print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")
        print(f"Here is your quiz on the {times_table} times table")


        score = 0
        total_questions = max_value


        for x in range(1, max_value_adjusted):
        correct_answer = x * times_table


        print(f"{x} times {times_table} is ...")

        while True:
            try:
            user_answer = int(input("Answer: "))
            break
        except ValueError:
        print("Invalid input. Please enter a valid number for your answer.")


        if user_answer == correct_answer:
        print("correct")
        score += 1
        else:
        print("incorrect")


        print(f"\nQuiz complete! You scored {score} out of {total_questions}.")


if __name__ == "__main__":
    main()
