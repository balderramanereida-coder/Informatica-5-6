def main():

        Transistors= 17800000000
        Years= int(input("How many years into the future? "))

        Transistors *= round(2** (Years/2))
        print(f"{Transistors:,}")


if __name__=="__main__":
    main()


