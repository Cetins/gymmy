class Payment:
    def __init__(self, amount, date, member, id=None):
        self.amount = amount
        self.date = date
        self.member = member
        self.id = id