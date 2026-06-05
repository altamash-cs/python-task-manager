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
* JSON Serialization
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
└── README.md
```

### File Descriptions

* **main.py** - Main application logic and menu handling
* **task.py** - Task class definition, object serialization, and special methods
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

## Example Output

```text
1. ❌ Study Python (2026-06-05 17:30)
2. ✅ Upload GitHub Project (2026-06-05 18:15)
```

## Concepts Practiced

* Classes and Objects
* Inheritance and Composition
* Special Methods (`__str__`, `__eq__`)
* Modular Programming
* JSON Serialization
* Exception Handling
* Input Validation
* Searching and Sorting
* Python Data Structures (Lists and Sets)

## Challenges Faced

* Implementing JSON serialization for Task objects
* Preventing duplicate tasks efficiently using sets
* Designing modular architecture across multiple files
* Handling invalid user input safely
* Managing object persistence between program runs
* Refactoring display logic using Python special methods

## Future Improvements

* Task priorities
* Due dates
* Task categories
* Export tasks to CSV
* Graphical User Interface (GUI)
* Database support using SQLite

## Author

Altamash Ulde
