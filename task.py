from datetime import datetime

class Task:
    
    def __init__(self, name):

        self.name = name
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.done = False

    def mark_complete(self):

        self.done = True

    def __str__(self):

        status = "✅" if self.done else "❌"
        return f"{status} {self.name} ({self.timestamp})"
    
    def __eq__(self, other):

        if not isinstance(other, Task):
            return False
        
        return self.name == other.name
    
    def to_dict(self):
        
        return {
            "name": self.name,
            "timestamp" : self.timestamp,
            "done" : self.done
        }
    
    @classmethod
    def from_dict(cls, data):

        task = cls(data["name"])
        task.timestamp = data["timestamp"]
        task.done = data["done"]
        return task