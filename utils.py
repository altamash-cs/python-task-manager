def print_menu():
    print("""
    1. View Tasks
    2. Add Task
    3. Remove Task
    4. Mark Task Complete
    5. Show Completed
    6. Show Incomplete
    7. Search Task
    8. Exit
    """)

def validate_number():

    while True:

        choice = input("Enter your choice: ")
        try:

            if choice.strip() =="":

                raise ValueError("Please Enter a Number before Submitting.")
            
            number = int(choice)
            
            if number <= 0:
                raise ValueError("Please Enter a Positive Number.")
            
            return number

        except ValueError as e:

            print(e)