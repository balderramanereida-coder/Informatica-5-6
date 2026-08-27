def main():

    print("The five layers of the Earth´s atmosphere")
    print()

    layer = input("Decent atmosphere layer: ")



    if layer == "Exosphere":
        print("Your altitude lever will be between 700 and 10,000 km")
        altitude = float(input("Enter exact altitude: "))

        e = 2000
        t = 500
        m = 200
        s = 75
        tr = 20

        print(e/1000/altitude+t/1000/altitude+m/1000/altitude+s/1000/altitude+tr/1000/altitude)E




    elif layer == "Thermosphere":
        print("Your altitude lever will be between 85 and 700 km")
        altitude = float(input("Enter exact altitude: "))

    elif layer == "Mesosphere":
        print("Your altitude lever will be between 50 and 85 km")
        altitude = float(input("Enter exact altitude: "))


    elif layer == "Stratosphere":
        print("Your altitude lever will be between 12 and 50 km")
        altitude = float(input("Enter exact altitude: "))


    elif layer == "Troposphere":
        print("Your altitude lever will be between 0 and 12 km")
        altitude = float(input("Enter exact altitude: "))


    else:
        print("Incorrect value, recheck your answer")

if __name__ == "__main__":
    main()
