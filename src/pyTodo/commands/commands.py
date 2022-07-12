"""Defines Commands for the Todo App"""
from builtins import list
from dataclasses import dataclass, field, asdict
import datetime
import shutil
import argparse as ap

class ValidationException(Exception):
    """Exception for validation errors"""

@dataclass
class Create:
    title: str
    description: str = field(default='')
    due_date: str = field(default='')
    priority: str = field(default='')
    completed: bool = field(default=False)
    def __post_init__(self):
        try:
            if self.title == '':
                raise ValidationException("Title is required")
        except Exception:
            raise ValidationException("Title is required")
        try:
            date = datetime.datetime.strptime(self.due_date, "%Y-%m-%d")
            print(date)
        except Exception:
            raise ValidationException("Due date should be in format YYYY-MM-DD.")
        if date < datetime.datetime.today():
            raise ValidationException("Due date must be in the future")
        if self.priority not in ['low', 'medium', 'high']:
            raise ValidationException("Priority must be low, medium, or high")
        print(self.completed)
        if self.completed not in ["True", "False"]:
            raise ValidationException("Completed must be True or False")


@dataclass
class List:
    tasks: list[Create] = field(default_factory=list)
    def list_tasks(self):
        """List tasks"""
        for task in self.tasks:
            print(task)

def create():
    parser = ap.ArgumentParser(description='A CLI tool for managing todo lists')
    parser.add_argument('-n', '--name', help='Name of the task')
    parser.add_argument('-d', '--description', help='Description of the task')
    parser.add_argument('-dd', '--due_date', help='Due date of the task')
    parser.add_argument('-p', '--priority', help='Priority of the task')
    parser.add_argument('-c', '--completed', help='Completed status of the task')
    args = parser.parse_args()

    create = Create(title=args.name, description=args.description, due_date=args.due_date, priority=args.priority,
                    completed=args.completed)
def pytd():
    parser = ap.ArgumentParser(description='A CLI tool for managing todo lists')
    parser.add_argument('-l', '--list', help='List tasks', action='store_true')
    parser.add_argument('-c', '--create', help='Create a task', action='store_true')
    args = parser.parse_args()
    if args.list:
        list = list()
        list.list_tasks()
    elif args.create:
        create()
