from task_manager import TaskManager

def display_menu():
    """
    Display the main menu options for the To-Do List Manager.
    """
    print("\n--- To-Do List Manager ---")
    print("1. List tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

def main():
    """
    The main function that runs the interactive to-do list manager.
    """
    tm = TaskManager()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            tasks = tm.list_tasks()
            if not tasks:
                print("No tasks available.")
            else:
                print("\nTask List:")
                for task in tasks:
                    status = "Completed" if task.completed else "Pending"
                    print(f"[{task.task_id}] {task.description} - {status}")
        elif choice == "2":
            description = input("Enter task description: ")
            tm.add_task(description)
            print("Task added successfully.")
        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                if tm.mark_task_complete(task_id):
                    print("Task marked as completed.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                if tm.delete_task(task_id):
                    print("Task deleted successfully.")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        elif choice == "5":
            print("Exiting the To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
