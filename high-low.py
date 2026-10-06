def main():


    def higth(a,b):
        if a > b:
            highest_num = a

        else:
            highest_num = b
        print(f"The highest number entered is {highest_num}")

    higth(8,2)


    def lower(a,b):
        if a > b:
            highest_num = a
            print(f"highest number = {round(highest_num,1)}")

        elif a < b:
            highest_num2 = b
            print(f"highest number = {round(highest_num2,1)}")

        else:
            print("Equal numbers")

    num1 = float(input("Enter your first numer: "))
    num2 = float(input("Enter your second number: "))

    higth(num1,num2)


if __name__ == "__main__":
    main()
