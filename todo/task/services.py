from .models import Task


def create_column(name: str, color: str, column_id: str):
    task, created = Task.objects.get_or_create(name=name, color=color, )
    return task