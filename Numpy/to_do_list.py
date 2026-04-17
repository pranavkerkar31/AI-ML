tasks = []


def show_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")


def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks found")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])


def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    
    if num > 0 and num <= len(tasks):
        tasks.pop(num - 1)
        print("Task deleted!")
    else:
        print("Invalid number")


while True:
    show_menu()
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")