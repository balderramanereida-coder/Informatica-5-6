def main():
    # planet = input("Planet:")

    # #Separation
    # print("Hello", planet)

    # #Concaten<tion
    # print("Hello" + planet)

    # #Formatted Strings
    # print(f"Hello {planet}")

    # #Ending
    # print("Hello",end=" ")
    # print(planet)

    name = input("What is your name?: ")
    color = input("Tell me a color: ")
    goal = input("A goal you would like to achieve: ")
    adj= input("Give me an adjective: ")

    print(f"Hello, {name}!", end="\n\n")
    print("This is your story:")
    print(f"At dawn the sky turned {color} and the air felt {adj}. So I decided today I {goal}")

if __name__=="__main__":
    main()
