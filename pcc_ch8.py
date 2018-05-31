unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
	current_design = unprinted_designs.pop()

	print("Printing model: " + current_design.title() )
	completed_models.append(current_design)

	# Display all confirmed users.
print("\nThe following models have been printed:")
for completed_model in completed_models:
 	print(completed_model.title() )