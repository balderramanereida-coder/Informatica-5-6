def main():
    welcome()
    get_item()


def welcome():
    menu = ["Torta de puerco","Torta de cochinita", "Torta de jamon","Torta de asada","Fries","Sodas","Chips","Desserts"]
    print("welcome to Hanna´s tortas las mas ricas")
    print("Here´s the menu:")
    for i in range(len(menu)):
        print(f"{i+1} {menu[i]}")



def get_item():






if __name__ == "__main__":
    main()
