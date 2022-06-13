class Course:
    def __init__(self, title, date, capacity, active, id=None):
        self.title = title
        self.date = date
        self.capacity = capacity
        self.active = active
        self.id = id