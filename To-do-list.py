import time
def main():

    print("Welcome to your personal To-do list app!")


    tasks = []

    while True:
        print(f"Tasks to do: {len(tasks)}")
        print(tasks)
        command = input("What do you want to do? (add,complete,exit):")
        if command == "add":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
        




if __name__ == "__main__":
    main()
