class Course:
    def __init__(self, title, level, date, capacity, active, id=None):
        self.title = title
        self.level = level
        self.date = date
        self.capacity = capacity
        self.active = active
        self.id = id