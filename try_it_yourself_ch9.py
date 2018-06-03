class Restaurant():
	"""Stores name and cuisine type"""
	def __init__(self, name, food_type):
		self.name = name
		self.food_type = food_type

	def describe_restaurant(self):
		print("This is " + self.name.title() + " Restaurant, " +
			"they serve " + self.food_type.title() + " type cuisine!")

	def open_restaurant(self):
		print(self.name.title() + " is open for feasting!")

class IceCreamStand(Restaurant):

	def __init__(self, name, food_type, flavors):
		super().__init__(name, food_type)
		self.flavors = flavors

	def describe_flavors(self):
		print("The flavors of ice cream are we have are: " )
		for x in self.flavors:
			print(x)

ice_cream_stand = IceCreamStand('weather vane', 'ice cream', ['banana, chocolate, vanilla'])
ice_cream_stand.describe_flavors()

