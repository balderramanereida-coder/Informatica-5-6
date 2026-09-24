def main():
    

        while True:
        user_input = input("Enter a number (1-10): ").strip().lower()
        
        
        if user_input == 'exit':
            break
        
        try:
            number = int(user_input)
            
            
            if 1 <= number <= 10:
                print(f"Here is the {number} times table")
                
        
                for i in range(1, 11):
                    result = i * number
                    print(f"{i} times {number} is {result}")
            else:
                print("Error: Please enter a number between 1 and 10.")
                
        except ValueError:
            
            print("Error: Invalid input. Enter a number from 1 to 10 or 'exit' to quit.")
            
        print()

if __name__ == "__main__":
    main()
