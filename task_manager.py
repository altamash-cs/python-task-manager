from storage import JSONStorage
from task import Task
from logger import logger
from exceptions import (
    DuplicateTaskError,
    TaskNotFoundError
)


class TaskManager:

    """
    Manages all task operations.
    """

    def __init__(self, storage=None):

        self.storage = storage or JSONStorage()
        self.tasks = self.storage.load()

    def save(self):

        """Saves all tasks."""
        self.storage.save(self.tasks)

    def add_task(self, name):

        if not name.strip():

            raise ValueError(
                "Task name cannot be empty."
            )

        if any(
            task.name.lower() == name.lower()
            for task in self.tasks
        ):

            raise DuplicateTaskError(
                "Task already exists."
            )

        task = Task(name)

        self.tasks.append(task)

        logger.info(
            f"Task added: {task.name}"
        )

        self.save()

        return task

    def remove_task(self, index):

        if not (
            0 <= index < len(self.tasks)
        ):
            
            raise TaskNotFoundError(
                "Invalid task index."
            )

        task = self.tasks.pop(index)
        logger.info(
            f"Task removed: {task.name}"
        )

        self.save()

        return task

    def complete_task(self, index):

        """Marks a task as completed."""
        if not (
            0 <= index < len(self.tasks)
        ):
            
            raise TaskNotFoundError(
                "Invalid task index."
            )

        self.tasks[index].mark_complete()
        logger.info(
            f"Task completed: {self.tasks[index].name}"
        )
        self.save()

    def get_all_tasks(self):

        """Returns every task."""

        return self.tasks

    def get_completed_tasks(self):

        """Returns completed tasks."""

        return [
            task
            for task in self.tasks
            if task.done
        ]

    def get_incomplete_tasks(self):

        """Returns incomplete tasks."""

        return [
            task
            for task in self.tasks
            if not task.done
        ]

    def search_tasks(self, keyword):
        
        """Searches for tasks by name."""

        keyword = keyword.lower()

        return [
            task
            for task in self.tasks
            if keyword in task.name.lower()
        ]

    def __len__(self):
        return len(self.tasks)

    def __iter__(self):
        return iter(self.tasks)