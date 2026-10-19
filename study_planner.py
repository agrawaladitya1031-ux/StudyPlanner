
import json
import os

FILE_NAME = "study_tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not load saved tasks. Starting with an empty list.")
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    subject = input("Enter subject: ").strip()
    description = input("Enter study task: ").strip()

    if not subject or not description:
        print("Subject and task cannot be empty.")
        return

    task = {
        "subject": subject,
        "description": description,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Study task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("\nNo study tasks found.")
        return

    print("\n--- Your Study Tasks ---")

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. [{status}] {task['subject']} - "
              f"{task['description']}")


def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed['description']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def show_progress(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed

    print("\n--- Study Progress ---")
    print(f"Total tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")

    if total:
        percentage = completed / total * 100
        print(f"Completion rate: {percentage:.1f}%")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== STUDY PLANNER =====")
        print("1. Add study task")
        print("2. View all tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. View progress")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            show_progress(tasks)
        elif choice == "6":
            print("Good luck with your studies!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
