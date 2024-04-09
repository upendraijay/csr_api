# Add your database models here if applicable
# Sample data (you can replace this with a database)
class Task:
    def __init__(self, id, title, description, done):
        self.id = id
        self.title = title
        self.description = description
        self.done = done