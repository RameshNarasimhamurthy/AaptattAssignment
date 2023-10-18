tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print("Task added:", task)

# Function to list tasks
def list_tasks():
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")

# Function to remove a task
def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print("Task removed:", removed_task)
    else:
        print("Invalid task index.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. List tasks")
    print("3. Remove a task")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        list_tasks()
        task_index = int(input("Enter the task index to remove: "))
        remove_task(task_index)
    elif choice == '4':
        print("Thanks for using ToDo.")
        break
    else:
        print("Invalid choice. Please try again.")