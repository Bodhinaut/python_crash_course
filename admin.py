# 9 - 7
class User():

	def __init__(self, first_name, last_name, *user_attributes):
		self.first_name = first_name
		self.last_name = last_name
		self.user_attributes = user_attributes

	def describe_user(self):
		output = ""
		print("Summary of user profile: \n" + self.first_name.title() + "\n" +
			self.last_name.title() ) 
		if self.user_attributes:
			for attr in self.user_attributes:
				print(attr.title() + ", " )

	def greet_user(self):
		print("Hello " + self.first_name.title() + " " + self.last_name.title() + ", 'ave a g'day!")

class Admin(User):

	def __init__(self, first_name, last_name, *user_attributes):
		super().__init__(first_name, last_name, *user_attributes)
		#self.privleges = ["can add post", "can delete post", "can ban user"]
		self.privleges = Privleges()

class Privleges():

	def __init__(self, privleges=["can add post", "can delete post", "can ban user"]):
		self.privleges = privleges

	def show_privleges(self):
		[print (values) for values in self.privleges]


kshive = Admin('kyle', 'shive','admin','lots of power')
kshive.describe_user()
kshive.privleges.show_privleges()