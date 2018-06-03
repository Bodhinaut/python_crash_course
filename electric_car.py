class Car():
	"""Simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car. """
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def update_odometer(self, mileage):
		"""
		Set the odometer reading to the given value. 
		Reject the change if it attempts to roll the odometer back.
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back the odometer!")

	def increment_odometer(self, miles):
		"""Add given amount to the odometer reading."""
		if miles < 0:
			print("You cannot add negative miles!")
		else:
			self.odometer_reading += miles
			print("You have updated your odometer to: " + str(self.odometer_reading) + ".")
		

	def get_descriptive_name(self):
		"""Return a neatly formatted descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""Print a statment showing the car's milage."""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

class Battery():
	"""Simple attempt to model a bettery for an electric car."""

	def __init__(self, battery_size=70):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statment describing the battery size."""
		print("The car has a " + str(self.battery_size) + "-kWh battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
		
	# 9 - 9
	def upgrade_battery(self):
		if self.battery_size != 85:
			self.battery_size = 85
			print("The battery has been upgraded to " + str(self.battery_size) )

class ElectricCar(Car):
	"""Represents aspects of a car, specific to electric vehicles."""
	def __init__(self, make, model, year):
		"""Initizlize attributes of the parent class."""
		"""Then initialize attributes specific to an electric car."""
		super().__init__(make, model, year)
		self.battery = Battery()

	def fill_gas_tank():
		"""Electric cars don't have gas tanks."""
		print("This car doesn't need a gas tank!")



my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name() )
# The ElectricCar instance works just like an instance of Car, so now we
# can begin defining attributes and methods specific to electric cars.
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()