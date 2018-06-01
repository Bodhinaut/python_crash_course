
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

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


print("\n---------------------------------------------------------\n")

def make_pizza(*toppings):
	print(toppings)

make_pizza("peppers")
make_pizza('mushrooms', 'green peppers', 'extra cheese')


 #  pass in as many name-value pairs as they want
def build_profile(first, last, **user_info):
	"""Build dictionary containing everytihn gwe know about a user. """
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein',
								 location = 'princeton',
								 field = 'physics')

print(user_profile)