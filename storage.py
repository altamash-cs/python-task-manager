import json
from task import Task

def save_tasks(tasks):

    json_save_tasks = []
    for task in tasks:

        task_data = task.to_dict()
        json_save_tasks.append(task_data)
    
    with open("tasks.json", "w") as file:
        
        json.dump(json_save_tasks, file, indent=4)

def load_tasks():

    tasks = []

    try:

        with open("tasks.json", "r") as file:

            data = json.load(file)
            for task_data in data:
                
                task = Task.from_dict(task_data)
                tasks.append(task)

    except json.JSONDecodeError:

        print("JSON file is Corrupted Pls Fix.")
        tasks = []

    except FileNotFoundError:

        print("No saved tasks found.")
        tasks = []

    return tasks