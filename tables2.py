def main():

    print("Welcome to the time tables quiz!")
    valid_nums = []
    for i in range(1,11):
        valid_nums.append(str(i))

    while True:
        times_table = input("Enter a times table that you would like to be tested on (1-10 or exit): ").lower().strip()

        if times_table == "exit":
            break

        elif times_table in valid_nums:
            max_value = int(input("Enter maxium value for the times table: "))

            print(f"Here is the {times_table}  +++++++++++++++++++++++++++++++++++++++++++++++++++++++table")

            for x in range(1,max_value+ 1):
                answer = x * int(times_table)
                print(f"{x}times{times_table} is {answer}")
        else:
            print("invalid command.")


if __name__ == "__main__":
    main()
