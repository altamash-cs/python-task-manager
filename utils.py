def print_menu():

    """Displays the main menu."""

    print("""
==============================
        TASK MANAGER
==============================
1. View Tasks
2. Add Task
3. Remove Task
4. Mark Task Complete
5. Show Completed
6. Show Incomplete
7. Search Task
8. Exit
""")


def validate_number(prompt="Enter your choice: ", minimum=1):

    """
    Prompts the user for a valid integer.

    Args:
        prompt (str): The message displayed to the user.
        minimum (int): The smallest accepted value.

    Returns:
        int: A validated integer.
    """

    while True:

        choice = input(prompt).strip()

        if not choice:

            print("Please enter a number before submitting.")
            continue

        try:

            number = int(choice)

            if number < minimum:

                print(f"Please enter a number greater than or equal to {minimum}.")
                continue

            return number

        except ValueError:
            
            print("Please enter a valid number.")