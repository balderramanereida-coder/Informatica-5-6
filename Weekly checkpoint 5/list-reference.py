def main():
    tacos = ["Pastor","Asada","Suadero","Rajas","Papa","Dorados","Buche"]
    print(tacos)
    print(tacos.pop(3))
    print(tacos)
#.pop has to be with the number, .remove has to be the written word

    numbers = [1,2,3,6,8,9,4,5]
    numbers.sort(reverse = True)
    print(numbers)

    number = [10,25,57,98,55,2,5,]
    print("Numbers:", number)
    print("Maximum:", max(number))
    print("Minimum:", min(number))
    print("Sum:", sum(number))

# Initialize a list
    numbers = [10, 30, 40]

# Insert 20 at index 1 (second position)
    numbers.insert(1, 20)
    print(numbers)
# Output: [10, 20, 30, 40]

# Insert at index 0 (beginning of the list)
    numbers.insert(0, 5)
    print(numbers)
# Output: [5, 10, 20, 30, 40]


# Initialize a list
    fruits = ["apple", "banana"]

# Append a single item
    fruits.append("cherry")
    print(fruits)
# Output: ['apple', 'banana', 'cherry']

# Appending another list adds the list as a single element (nested list)
    fruits.append(["date", "elderberry"])
    print(fruits)
# Output: ['apple', 'banana', 'cherry', ['date', 'elderberry']]


    x = len("hello")

    print(x)
    password = [1, 2, 3, 4, 5, 6, 7, 8]
    xx = ["a", "b", "c", "d"]
    print(len(xx))
    print(password)
    change = input(" ")
    if change == "y":
        password[1] = 4
        password[0] = 2
        password[7] = 1
        password[6] = 9
        password[5] = 10
        print(password)




if __name__=="__main__":
    main()
