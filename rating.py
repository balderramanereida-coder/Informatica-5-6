def main():

    print("Welcome to Las mejores hamburgirs!")

    rating = float(input("Please rate my restaurant: "))

    if 5.1 > rating > 4.4:
        print("Perfection.")
    elif 4.5 > rating > 4:
        print("Excellent")
    elif 4 > rating > 3:
        print("Good")
    elif 3 > rating > 2:
        print("Fair")
    elif 2 > rating > 0:
        print("Poor")
    else:
        print("Invalid response")

    print("THANKS!")
    print("Don´t forget to buy your hamburgir :)")

if __name__ == "__main__":
    main()
