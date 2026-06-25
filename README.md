# Python Task Manager

A command-line Task Manager built in Python to practice object-oriented programming, project architecture, modular design, and clean code principles.

Originally developed as a learning project, the application was later refactored into a more maintainable architecture inspired by real backend applications.

---

## Features

* Add new tasks
* Remove tasks
* Mark tasks as complete
* View all tasks
* View completed tasks
* View incomplete tasks
* Search tasks by name
* Prevent duplicate task names
* Automatically save tasks between sessions
* Persistent JSON storage
* Application logging
* Custom exception handling

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* JSON Serialization
* Abstract Base Classes (ABC)
* File Handling
* Python Logging
* Exception Handling
* Git & GitHub

---

## Project Structure

```text
python-task-manager/
│
├── main.py              # Application entry point
├── task_manager.py      # Core business logic
├── task.py              # Task model
├── storage.py           # Storage abstraction & JSON implementation
├── utils.py             # Input validation and helper functions
├── logger.py            # Logging configuration
├── exceptions.py        # Custom application exceptions
│
├── tasks.json           # Local task storage (generated automatically)
├── task_manager.log     # Application logs (generated automatically)
│
└── README.md
```

---

## Architecture

The project follows a layered architecture where each module has a single responsibility.

```
User
 │
 ▼
main.py
 │
 ▼
TaskManager
 │
 ├── Task
 ├── Storage
 └── Logger
```

This separation makes the application easier to maintain, extend, and test.

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/altamash-cs/python-task-manager.git
```

Navigate into the project:

```bash
cd python-task-manager
```

Run the application:

```bash
python main.py
```

---

## Example Menu

```text
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
```

---

## Example Output

```text
1. ❌ Study Python (2026-06-25 15:42)
2. ✅ Update README (2026-06-25 16:10)
3. ❌ Learn FastAPI (2026-06-25 18:00)
```

---

## Concepts Practiced

This project was built to reinforce Python fundamentals and object-oriented programming concepts, including:

* Classes and Objects
* Composition
* Abstract Base Classes (ABC)
* Magic Methods (`__str__`, `__repr__`, `__eq__`)
* Alternate Constructors (`@classmethod`)
* Modular Programming
* JSON Serialization
* File Handling
* Logging
* Custom Exceptions
* Separation of Responsibilities
* Refactoring
* Clean Code Principles

---

## Refactoring Highlights (v1.1)

Compared to the initial implementation, Version 1.1 introduced:

* Dedicated `TaskManager` class
* Storage abstraction using an Abstract Base Class
* Configurable JSON storage
* Logging system
* Custom exceptions
* Improved project architecture
* Better separation of business logic from the user interface
* Cleaner, more maintainable code structure

---

## Future Improvements

* Unit tests using `unittest` or `pytest`
* Task priorities
* Due dates
* Categories and tags
* CSV export
* SQLite support
* REST API using FastAPI
* Authentication
* Docker support

---

## What I Learned

This project started as a simple command-line application and gradually evolved through multiple refactoring stages.

Along the way, I learned not only Python syntax, but also how to organize code into reusable components, separate responsibilities, refactor existing code, and design applications that are easier to extend and maintain.

---

## Author

**Altamash Ulde**

Built as part of my Python backend development learning journey.
