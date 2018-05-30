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


def get_formatted_name(first_name, last_name, middle_name = ''):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)

print("\n--------------------------------------------------\n")


def build_person(first_name, last_name, age = ''):
	"""Return a dictionary of information about a person."""
	person = {'first' : first_name, 'last' : last_name}

	if age:
		person['age'] = age

	return (person)

martial_artist = build_person('bruce', 'lee', 'too young to have died')
print (martial_artist)




def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()

# below is while loop utilizing get_formatted_name, 
while True:
	print("\nPlease tell me your name: ")
	print("\n(ENTER Q AT ANY TIME TO QUIT)")
	f_name = input("First name: ")
	if f_name.upper() == 'Q':
		break

	l_name = input("Last name: ")
	if l_name.upper() == 'Q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")
