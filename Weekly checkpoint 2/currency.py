def main():
    P=float(input("What do you have left in pesos? "))
    S=float(input("What do you have left in soles? "))
    R=float(input("What do you have left in reais? "))

    usd=(P*0.00032)+(S*0.30)+(R*0.19)
    mxn =round(usd*17.07,2)

    print(f"USD: {round(usd,2)}")
    print(f"MXN: {mxn}")


if __name__=="__main__":
    main()
