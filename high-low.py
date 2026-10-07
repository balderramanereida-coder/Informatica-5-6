def main():


    def higth(a,b):
        if a > b:
            highest_num = a

        else:
            highest_num = b
        print(f"The highest number entered is {highest_num}")

    higth(8,2)


    def lower(a,b,c):
        if a < (b,c):
            lower_num = a
            print(f"The lower number is {lower_num}")

        elif b < (a,c):
            lower_num = b
            print(f"The lower number is: {lower_num}")

        else:
            c < (a,b)
            print(f"The lower number is: {lower_num}")

    num1 = int(input("Enter your first numer: "))
    num2 = int(input("Enter your second number: "))
    num3 = int(input("Enter your third numer: "))

    lower(num1,num2,num3)


if __name__ == "__main__":
    main()
