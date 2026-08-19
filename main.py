#Add these functions:
    # - Add a task
    # - List all tasks
    # - Mark a task complete
    # - Delete a task

while True:
    print("Welcome to task manager\n")

    print("Type 1 if you wish to add a task")
    print("Type 2 if you wish to list all task")
    print("Type 3 if you wish to mark a task complete")
    print("Type 4 if you wish to delete a task")
    print("Type 5 if you wish to quit\n")

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        print("\nTask added\n")
    elif user_choice == 2:
        print("\nHere's all your task: \n")
    elif user_choice == 3:
        print("\nThis task has been marked complete\n")
    elif user_choice == 4:
        print("\nTask Deleted\n")
    elif user_choice == 5:
        print("Bye!")
        break
    else:
        print("\nWrong input, try again.\n")