# 9-1 Restaurant
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

oriental_spoon = Restaurant("the oriental spoon", "korean")
oriental_spoon.describe_restaurant()
oriental_spoon.open_restaurant()

# 9 - 2

the_orient = Restaurant('the orient', 'american-chinese')
the_orient.describe_restaurant()
the_orient.open_restaurant()

wasabi = Restaurant('wasabi', 'japanese-sushi')
wasabi.describe_restaurant()
wasabi.open_restaurant()