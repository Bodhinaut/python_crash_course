class Restaurant():
	"""Stores name and cuisine type"""
	def __init__(self, name, food_type):
		self.name = name
		self.food_type = food_type
		self.number_served = 0

	def describe_restaurant(self):
		print("This is " + self.name.title() + " Restaurant, " +
			"they serve " + self.food_type.title() + " type cuisine!")

	def open_restaurant(self):
		print(self.name.title() + " is open for feasting!")

	def set_number_served(self, num_served):
		"""Sets the number of people served in the restaurant."""
		# later add conditional to not allow negative numbers
		self.number_served = num_served
		print("Number served set to " + str(self.number_served) )

	def increment_number_served(self, num_served):
		self.number_served += num_served
		print("The current number served is: " + str(self.number_served) )

restaurant = Restaurant('pi', 'pizza')

print("Below printed by setting attribute")
print(restaurant.number_served)
print("Below printed by method")
restaurant.set_number_served(13)
print("Below is printed with increment method")
restaurant.increment_number_served(200)