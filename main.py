from task_manager import TaskManager
from utils import print_menu, validate_number
from exceptions import(
    DuplicateTaskError,
    TaskNotFoundError
)


def display_tasks(tasks):

    """Displays a numbered list of tasks."""

    if not tasks:

        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):

        print(f"{index}. {task}")


def main():

    manager = TaskManager()

    while True:

        print_menu()
        choice = validate_number()

        if choice == 1:

            display_tasks(manager)

        elif choice == 2:

            task_name = input("Enter your task: ").strip()

            if not task_name:

                print("Please enter a task name.")
                continue

            try:

                added_task = manager.add_task(
                    task_name
                )

                print(
                    f"Added: {added_task.name}"
                )

            except DuplicateTaskError as e:

                print(e)

            except ValueError as e:

                print(e)

        elif choice == 3:

            display_tasks(manager)

            task_number = validate_number(
                "Task number: "
            )

            try:

                removed = manager.remove_task(task_number - 1)
                print(f"{removed.name} removed!")

            except TaskNotFoundError:

                print("Invalid task number.")

        elif choice == 4:

            display_tasks(manager)

            task_number = validate_number(
                "Task number: "
            )

            try:

                manager.complete_task(task_number - 1)
                print("Task marked complete!")

            except TaskNotFoundError:
                
                print("Invalid task number.")

        elif choice == 5:

            display_tasks(
                manager.get_completed_tasks()
            )

        elif choice == 6:

            display_tasks(
                manager.get_incomplete_tasks()
            )

        elif choice == 7:

            keyword = input(
                "Search: "
            ).strip()

            results = manager.search_tasks(keyword)

            display_tasks(results)

        elif choice == 8:

            print("See you later!")
            break

        else:

            print("Please enter a valid option.")


if __name__ == "__main__":
    main()