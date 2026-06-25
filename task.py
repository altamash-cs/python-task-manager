from datetime import datetime


class Task:
    """
    Represents a single task in the Task Manager.
    """

    def __init__(self, name, timestamp=None, done=False):

        self.name = name
        self.timestamp = (
            timestamp
            if timestamp is not None
            else datetime.now().strftime("%Y-%m-%d %H:%M")
        )
        self.done = done

    def mark_complete(self):

        """Marks the task as completed."""
        self.done = True

    def mark_incomplete(self):

        """Marks the task as incomplete."""
        self.done = False

    def to_dict(self):

        """Converts the task into a dictionary for JSON storage."""
        return {
            "name": self.name,
            "timestamp": self.timestamp,
            "done": self.done,
        }

    @classmethod
    def from_dict(cls, data):

        """Creates a Task object from a dictionary."""
        return cls(
            name=data["name"],
            timestamp=data["timestamp"],
            done=data["done"],
        )

    def __str__(self):

        """User-friendly string representation."""
        status = "✅" if self.done else "❌"
        return f"{status} {self.name} ({self.timestamp})"

    def __repr__(self):

        """Developer-friendly representation."""
        return (
            f"Task("
            f"name={self.name!r}, "
            f"done={self.done}, "
            f"timestamp={self.timestamp!r})"
        )

    def __eq__(self, other):
        
        if not isinstance(other, Task):
            return NotImplemented

        return (
            self.name == other.name
            and self.timestamp == other.timestamp
            and self.done == other.done
        )