todo_list = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task = input("Enter a new task: ")
            todo_list.append(task)
            print("Task added.")
        elif choice == '2':
            print("\nTasks:")
            for idx, task in enumerate(todo_list, 1):
                print(f"{idx}. {task}")
        elif choice == '3':
            task_num = int(input("Enter task number to remove: "))
            if 0 < task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

main()

