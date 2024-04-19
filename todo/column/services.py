from column.models import Column

def create_column(name: str, color: str):
    column, created = Column.objects.get_or_create(name=name, color=color)
    return column