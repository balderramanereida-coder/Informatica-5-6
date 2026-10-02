def main():

    print("Welcome to the times table quiz")
    while True
        try
        times_table = int(input("Enter a times table that you would like to be tested on (1-10): "))
            if 1<= times_table <= 10:
                break
            print("Please enter a number between (1-10)")

        except ValueError
            print("Invalid input.Please enter a valid whole number")

        while True
            try:
                 max_value = int(input("Enter the maximum value for your times table: "))

            if max_value > 0:
                break
            print("Enter a positive number")
            
        except ValueError


       print(f"Here is the {times_table} times table")

            for x in range(1, 11):
                answer = x * times_table
                print(f"{x} times {times_table} is {answer}")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
