# the method call will automatically pass the self argument.
# Every method call associated with a class automatically passes self, which
# is a reference to the instance itself
# it gives the individual instance access to
# the attributes and methods in the class
# Any variable
# prefixed with self is available to every method in the class, and we’ll also be
# able to access these variables through any instance created from the class.
# self.name = name takes the value stored in the parameter name and stores it
# in the variable name, which is then attached to the instance being created. 
# Variables that are accessible
# through instances like this are called attributes.
class Dog():
	"""A simple attemt to model a dog"""

	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(self.name.title() + " rolled over!")


my_dog = Dog("willie", 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")

# After we create an instance from the class Dog, we can use dot notation to
# call any method defined in Dog. Let’s make our dog sit and roll over:

my_dog.sit()
my_dog.roll_over()
your_dog.sit()
your_dog.roll_over()