from user_prac import User
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