#Add these functions:
    # - Add a task
    # - List all tasks
    # - Mark a task complete
    # - Delete a task

tasks = [
    {"task": "buy milk", "done": False},
    {"task": "email client", "done": True},
]

while True:
    print("Welcome to task manager\n")

    print("Type 1 if you wish to add a task")
    print("Type 2 if you wish to list all task")
    print("Type 3 if you wish to mark a task complete")
    print("Type 4 if you wish to delete a task")
    print("Type 5 if you wish to quit\n")

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        task = input("Enter the task: ").lower()
        taskDict = {
            "task": {task},
            "done": False
        }
        tasks.append(taskDict)
        print("Task added!")

    elif user_choice == 2:
        print("\nHere's all of your tasks:")
        for i in tasks:
            if i["done"] == False:
                print(f"{(tasks.index(i) + 1)}.) {i["task"]} []")
            else:
                print(f"{(tasks.index(i) + 1)}.) {i["task"]} [X]")

    elif user_choice == 3:
        taskPos = int(input("Enter the task position here: "))
        tasks[taskPos - 1]["done"] = True

        print("\nTask marked done")

    elif user_choice == 4:
        taskPos = int(input("Enter the task position here: "))
        tasks.pop(taskPos - 1)

        print("\nTask Deleted\n")

    elif user_choice == 5:
        print("Bye!")
        break
    else:
        print("\nWrong input, try again.\n")