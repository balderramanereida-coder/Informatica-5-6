def main():
    valid_nums = []
    for i in range(1,11):
        valid_nums.append(str(i))

    while True:
        times_table = input("Enter a number(1-10 or exit): ").lower().strip()

        if times_table == "exit":
            break

        elif times_table in valid_nums:
            max_value = int(input("Enter maxium value for the times table: "))

        while True:
            try:
                name = input("Enter your name")
                f_letter = name[0]
                print("Name stored successfuly.")
            except IndexError:
                print("You MUST enter a number between 1 and 10.")

if __name__ == "__main__":
    main()
