def main():

    print("Welcome to Binary to Decimal Converter!")
    print()
    print("In this program, you will be able to convert your binary numbers into decimals automatically so it´s easier for you to work with this numbers")
    find = int(input("Enter a binary number: "))
    binary_to_decimal(find)

def binary_to_decimal(binary):

    decimal = 0
    list = []

    for i in binary:
        list.append(binary[i])
        list.reverse()

    for digit in range(len(list)):

        if digit == "1":
            decimal += 2 **(i+1)



if __name__ == "__main__":
    main()
