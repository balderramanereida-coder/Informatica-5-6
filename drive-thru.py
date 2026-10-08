def main():

    welcome()

    user_order = input("\nWhat would you like to order?: ")
    get_item(user_order)

def welcome():

    menu = ["Hamburgir", "Fries", "Sodas", "Waffles", "Desserts", "Paella", "Baguete"]
    print("Welcome to The Pou´s landia food!!")
    print("Here´s the menu:")
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")

def get_item(order):

    order = order.strip().lower()

    if order == "hamburgir" or order == "1":
        print("Enjoy! 🍔")
    elif order == "fries" or order == "2":
        print("Enjoy! 🍟")
    elif order == "sodas" or order == "3":
        print("Enjoy! 🥤")
    elif order == "waffles" or order == "4":
        print("Enjoy! 🧇")
    elif order == "desserts" or order == "5":
        print("Enjoy! 🧁")
    elif order == "paella" or order == "6":
        print("Enjoy! 🥘")
    elif order == "baguete" or order == "7":
        print("Enjoy! 🥖")
    else:
        print("❌ Option not found on the menu")


if __name__ == "__main__":
    main()
