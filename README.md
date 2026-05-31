# Python Task Manager

A command-line task management application built with Python using Object-Oriented Programming principles and JSON-based data persistence.

## Features

* Add new tasks
* Remove existing tasks
* Mark tasks as complete
* Search tasks by name
* Display completed tasks
* Display incomplete tasks
* Prevent duplicate task names
* Automatically save tasks between sessions

## Technologies Used

* Python
* Object-Oriented Programming (OOP)
* JSON
* File Handling
* Git & GitHub

## Project Structure

```text
python-task-manager/
│
├── main.py
├── task.py
├── storage.py
├── utils.py
├── tasks.json
└── README.md
```

### File Descriptions

* **main.py** - Main application logic and menu handling
* **task.py** - Task class definition and object serialization
* **storage.py** - Saving and loading tasks from JSON files
* **utils.py** - Utility functions such as menu display and input validation

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/altamash-cs/python-task-manager.git
```

2. Navigate to the project directory:

```bash
cd python-task-manager
```

3. Run the application:

```bash
python main.py
```

## Example Menu

```text
1. View Tasks
2. Add Task
3. Remove Task
4. Mark Task Complete
5. Show Completed
6. Show Incomplete
7. Search Task
8. Exit
```

## Concepts Practiced

* Classes and Objects
* Modular Programming
* Data Serialization
* Exception Handling
* Input Validation
* Searching and Sorting
* Python Data Structures (Lists and Sets)

## Future Improvements

* Task priorities
* Due dates
* Task categories
* Export tasks to CSV
* Graphical User Interface (GUI)
* Database support using SQLite

## Author

Altamash Ulde
