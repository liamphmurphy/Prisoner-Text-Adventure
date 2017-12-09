class Inventory:
    def __init__(self, name, description, totalinventory, damage):
        self.name = name
        self.description = description
        self.totalinventory = []
        self.damage = damage

    def add_item(self, item):
        self.totalinventory.append(item)

    def remove_item(self, item):
        self.totalinventory.remove(item)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.totalinventory)

class GuardKey(Inventory):
    def __init__(self,name,description):
        self.description = "A key from a guard near the prison cell, the use seems obvious."
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description)
class Sword(Inventory):
    def __init__(self,name,description,damage):
        self.name = "Sword"
        self.description = "A simple sword that you found in the prison armory."
        self.damage = 4
    def __str__(self):
        return "\n\nValue: {}\n".format(self.name, self.description, self.damage)
