# practice basic functions
# greet_user has been modified to treat lists
def greet_user(username):
	"""Display a simple greeting"""
	for name in username:
		msg = "Hello " + name.title() + ", how are you?"
		print(msg)


# greet_user("kyle") old method only accepted one user at a time, 
usernames = ['hannah', 'amanda', 'kyle']
greet_user(usernames)


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

print("\n--------------------------------------------------\n")

# Below, start with some desings that need to be printed. 
unprinted_designs = ['iphone case', 'robot pendant', 'dodhecahedron']
completed_models = []

# Simulate printing each design, 
# Move each design to complted_models after printing. 
while unprinted_designs:
	current_design = unprinted_designs.pop()
	# Simulate creating a 3D print from the design.
	print("\nPrinting model: " + current_design)
	completed_models.append(current_design)

	# Display all completed models.
print("\nThe following models have been printed: ")
for completed_models in completed_models:
	print(completed_models)


print('\n--------------------------------------------------\n')

# Modularizing and refactoring the above code into methods

def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each design, until none are left.
	Move each design to completed_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()

		# Simulate creating a 3D print from the design.
		print("Printing model: " + current_design.title() )
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were printed."""
	print("\nThe following models have been printed: ")
	for completed_model in completed_models:
		print(completed_model.title() )

unprinted_designs = ['iphone case', 'robo pendant', 'octothorpe']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print("\n--------------------------------------------------\n")



