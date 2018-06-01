# 9 - 3
class User():

	def __init__(self, first_name, last_name, *user_attributes):
		self.first_name = first_name
		self.last_name = last_name
		self.user_attributes = user_attributes

	def describe_user(self):
		output = ""
		print("Summary of user profile: \n" + self.first_name.title() + "\n" +
			self.last_name.title() ) 
		for attr in self.user_attributes:
			print(attr.title() + ", " )

	def greet_user(self):
		print("Hello " + self.first_name.title() + " " + self.last_name.title() + ", 'ave a g'day!")


kshive = User('kyle', 'shive', 'loves python', 'searching for work', 'loves old games')
kshive.describe_user()
kshive.greet_user()

acorntree = User('amanda', 'cornell', 'brilliant, sharp, and resourceful', 'loves robots', 'searching for work as well', 'loves organization and photos', 'incredibly beautiful')
acorntree.describe_user()
acorntree.greet_user()