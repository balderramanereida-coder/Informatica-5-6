def main():

    print("The five layers of the Earth´s atmosphere")
    print()

    layer = input("Decent atmosphere layer: ")



    if layer == "Exosphere":
        print("Your altitude lever will be between 700 and 10,000 km")
        altitude = float(input("Enter exact altitude: "))
        print(altitude )

    elif layer == "Mesosphere":
        print("Your altitude lever will be between 700 and 10,000 km")

    elif layer == "Stratosphere":
        print("Your altitude lever will be between 700 and 10,000 km")
    elif layer == "Troposphere":
        print("Your altitude lever will be between 700 and 10,000 km")


    else:
        print("Incorrect value, recheck your answer")







if __name__ == "__main__":
    main()
