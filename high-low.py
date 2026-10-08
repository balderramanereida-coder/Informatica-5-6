def main():


    def highest(a, b):
        if a > b:
            highest_num = a
        else:
            highest_num = b

        print(f"The highest number entered is {highest_num}")

    highest(8, 2)


    def lowest(a, b, c):
        if a < b and a < c:
            lowest_num = a
        elif b < a and b < c:
            lowest_num = b
        else:
            lowest_num = c

        print(f"The lowest number entered is {lowest_num}")

    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    num3 = int(input("Enter your third number: "))


    highest(num1, num2)

    lowest(num1, num2, num3)
    

if __name__ == "__main__":
    main()
