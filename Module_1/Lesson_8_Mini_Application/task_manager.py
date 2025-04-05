import json, os

class Task:
    def __init__(self, task_id, description, completed=False):
        self.task_id = task_id
        self.description = description
        self.completed = completed
    
    def mark_complete(self):
        self.completed = True
        
    def to_dict(self):
        return {
            'task_id': self.task_id,
            'description': self.description,
            'completed': self.completed
            }
        
    @classmethod
    def from_dict(cls, data):
        return cls(data['task_id'], data['description'], data['completed'])
    
class TaskManager:
    def __init__(self, file_path='tasks.json'):
        self.file_path = file_path
        self.tasks = []
        self.load_tasks()
        
    def add_task(self, description):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, description)
        self.tasks.append(new_task)
        self.save_tasks()
        
    def list_tasks(self):
        return self.tasks
    
    def mark_task_complete(self, task_id):
        """
        Mark the task with the provided task_id as completed.

        Parameters:
            task_id (int): The unique identifier of the task.

        Returns:
            bool: True if the task was found and marked, otherwise False.
        """
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_complete()
                self.save_tasks()
                return True
        return False
    
    def delete_task(self, task_id):
        """
        Delete the task with the provided task_id.

        Parameters:
            task_id (int): The unique identifier of the task to delete.

        Returns:
            bool: True if the task was found and deleted, otherwise False.
        """
        for index, task in enumerate(self.tasks):
            if task.task_id == task_id:
                del self.tasks[index]
                self.save_tasks()
                return True
        return False
    
    def load_tasks(self):
        """
        Load tasks from the JSON file specified by file_path. If the file doesn't exist,
        start with an empty task list.
        """
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    tasks_data = json.load(file)
                    self.tasks = [Task.from_dict(task) for task in tasks_data]
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading tasks: {e}")
                self.tasks = []
        else:
            self.tasks = []
            
    def save_tasks(self):
        """
        Save the current tasks to the JSON file specified by file_path.
        """
        try:
            with open(self.file_path, 'w') as file:
                tasks_data = [task.to_dict() for task in self.tasks]
                json.dump(tasks_data, file, indent=4)
        except IOError as e:
            print(f"Error saving tasks: {e}")
        