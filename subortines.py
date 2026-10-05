def main():

    def calculate(a,b):
        answer = a + b
        print(f"{a}+{b} = {answer}")

    num1 = 10
    num2 = 15

    calculate(num1,num2)

    def average_value(a,b,c):
        answer = (a + b + c) / 3
        print(f"The average value is {round(answer,1)}")

    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    n3 = float(input("Enter third number: "))

    average_value(n1,n2,n3)


if __name__ == "__main__":
    main()


