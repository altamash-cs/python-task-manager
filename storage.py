import json
from abc import ABC, abstractmethod

from task import Task

from logger import logger


class Storage(ABC):

    """
    Abstract base class for all storage systems.
    """

    @abstractmethod
    def save(self, tasks):

        """Save tasks."""
        pass

    @abstractmethod
    def load(self):

        """Load tasks."""
        pass


class JSONStorage(Storage):

    """
    Handles saving and loading tasks from a JSON file.
    """

    def __init__(self, filename="tasks.json"):

        self.filename = filename

    def save(self, tasks):

        json_tasks = [
            task.to_dict()
            for task in tasks
        ]

        with open(self.filename, "w") as file:

            json.dump(
                json_tasks,
                file,
                indent=4
            )

    def load(self):

        try:

            with open(self.filename, "r") as file:
                
                data = json.load(file)

            return [
                Task.from_dict(task_data)
                for task_data in data
            ]

        except FileNotFoundError:

            logger.warning(
                "No saved tasks found."
            )

            return []

        except json.JSONDecodeError:

            logger.error(
                "tasks.json is corrupted."
            )

            return []