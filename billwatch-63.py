# === Stage 63: Add relationships between records where useful ===
# Project: BillWatch
class Bill:
    def __init__(self, name, amount, due_date, category, status, payer):
        self.name = name
        self.amount = amount
        self.due_date = due_date
        self.category = category
        self.status = status
        self.payer = payer

class House:
    def __init__(self, name):
        self.name = name
        self.bills = []

    def add_bill(self, bill):
        self.bills.append(bill)

    def bills_for(self, category):
        return [b for b in self.bills if b.category == category]

    def bills_by(self, payer):
        return [b for b in self.bills if b.payer == payer]

    def total_for_category(self, category):
        return sum(b.amount for b in self.bills_for(category))

    def outstanding_total(self):
        return sum(b.amount for b in self.bills if b.status != "paid")

class Household:
    def __init__(self):
        self.houses = {}

    def add_house(self, house):
        self.houses[house.name] = house

    def find_house(self, name):
        return self.houses.get(name)

    def all_bills(self):
        return [b for h in self.houses.values() for b in h.bills]

    def by_category(self, category):
        return [b for b in self.all_bills() if b.category == category]

    def by_payer(self, payer):
        return [b for b in self.all_bills() if b.payer == payer]
