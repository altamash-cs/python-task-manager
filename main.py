from task import Task
from storage import save_tasks, load_tasks
from utils import print_menu, validate_number

task_names = set()
tasks = load_tasks()
for task in tasks:

    task_names.add(task.name)

def add_task(task_obj):
    
    tasks.append(task_obj)
    save_tasks(tasks)
    print("Task Added!")

def main():

    while True:

        print_menu()
        choice = validate_number()

        if choice == 1:

            if len(tasks) == 0:

                print("No tasks yet!")

            else:

                for index, task in enumerate(tasks, start=1):

                    print(f"{index}. {task}")

        elif choice == 2:

            task_name = input("Enter your task: ")
            task_name = task_name.strip()
            if task_name == "":

                print("Pls DO NOT Leave the field Empty.")

            elif task_name in task_names:

                print("Task already exists!")

            else:

                task = Task(task_name)
                add_task(task)
                task_names.add(task.name)

        elif choice == 3:

            task_number = validate_number()
            index = task_number - 1

            if 0 <= index < len(tasks):

                removed = tasks.pop(index)
                task_names.remove(removed.name)
                print(f"{removed.name} removed!")
                save_tasks(tasks)

            else:
                print("Invalid task number!")

        elif choice == 4:

            task_number = validate_number()
            index = task_number - 1

            if 0 <= index < len(tasks):

                tasks[index].mark_complete()
                save_tasks(tasks)
                print("Task marked complete!")

            else:
                print("Invalid task number!")

        elif choice == 5:

            tasks.sort(key=lambda task: task.done)
            for index,task in enumerate(tasks, start=1):

                print(f"{index}. {task}")

        elif choice == 6:

            tasks.sort(key=lambda task: task.done, reverse=True)
            for index,task in enumerate(tasks, start=1):

                print(f"{index}. {task}")

        elif choice == 7:

            target = input("Enter Task to Search: ").strip()
            found = False
            for index,task in enumerate(tasks, start=1):


                if target.lower() in task.name.lower():

                    if not found:

                        print("\nMatching Tasks:")

                    found = True
                    print(f"{index}. {task}")

            if not found:

                print("No matching tasks found.")


        elif choice == 8:

            print("See you later!")
            break

        else:

            print("Please Enter a valid choice between 1-8.")

if __name__ == "__main__":
    main()