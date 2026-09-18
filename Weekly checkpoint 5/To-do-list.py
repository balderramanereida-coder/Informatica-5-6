def main():

    tasks = []

    while True:
        print(f"Tasks to do: {len(tasks)}")
        print(tasks)
        command = input("What do you want to do? (add,complete,exit): ")
        if command == "add":
            new_task = input("Enter new task: ")
            tasks.append(new_task)

        elif command == "complete":
            outtask = input("Which task are you removing?: ")
            tasks.remove(outtask)

        elif command == "correct":
            rewrite = input("What task are you rewriting?: ")
            command[rewrite] = command

        elif command == "stop":
            break


if __name__ == "__main__":
    main()
