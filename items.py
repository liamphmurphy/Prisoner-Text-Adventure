class Inventory:
	def __init__(self, name, description, totalinventory):
		self.name = name
		self.description = description
		self.totalinventory = []

	def add_item(self, item):
		self.totalinventory.append(item)

	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.totalinventory)

class GuardKey(Inventory):
	def __init__(self,name,description):
		self.description = "A key from a guard near the prison cell, the use seems obvious."
	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description)