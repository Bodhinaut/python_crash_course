class User():

	def __init__(self, first_name, last_name, *user_attributes):
		self.first_name = first_name
		self.last_name = last_name
		self.user_attributes = user_attributes
		self.login_attempts = 0

	def describe_user(self):
		output = ""
		print("Summary of user profile: \n" + self.first_name.title() + "\n" +
			self.last_name.title() ) 
		for attr in self.user_attributes:
			print(attr.title() + ", " )

	def greet_user(self):
		print("Hello " + self.first_name.title() + " " + self.last_name.title() + ", 'ave a g'day!")

	def increment_login_attemps(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

kshive = User('kyle', 'shive', 'has a great job')
kshive.describe_user()
kshive.increment_login_attemps()
for x in range(5):
	kshive.increment_login_attemps()
print(kshive.login_attempts)
kshive.reset_login_attempts()
print(kshive.login_attempts)