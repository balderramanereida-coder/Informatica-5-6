def main():

    print("Absolute Value Calculator")

    number = float(input("Integer number: "))

    if number < 0:
        print(number*-1)
    else:
        print(number)

    print("Input Calculator")

    number1 = float(input("Select first number: "))

    number2 = float(input("Select second number: "))

    operation = input("Type of opperation: ")

    if operation == "add":
        print(number1 + number2)

    elif operation == "subtract":
        print(number1 - number2)
    elif operation == "multiply":
        print(number1 * number2)
    else:
        print("Not possible")

    print("String Calculator")

    


if __name__ == "__main__":
    main()
