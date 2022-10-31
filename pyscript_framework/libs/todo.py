from datetime import datetime as dt
from utils import add_class, remove_class

tasks = []
# define the task template that will be use to render new templates to the page

task_template = Element("task_template").select(".task", from_content=True)
task_list = Element("list-tasks-container")
new_task_content = Element("new-task-content")


def add_task(*args, **kwargs):
    pass


def add_task_event(e):
    if e.key == "Enter":
        add_task()

new_task_content.element.onkeypress = add_task_event