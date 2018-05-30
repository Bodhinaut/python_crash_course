# practice basic functions

def greet_user(username):
	"""Display a simple greeting"""
	print("Hello " + username.title() + ", how are you?")


greet_user("kyle")


def describe_pet(pet_name, animal_type = 'dog'):
	"""Display info about pet"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('pete', 'gorilla')