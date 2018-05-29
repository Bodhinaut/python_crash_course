# Below is Deli program and No Pastrami program
sandwich_orders = ['pepper jack', 'pb & j', 'tofu', 'egg', 'pastrami', 'pastrami', 'pastrami']

finished_sandwiches = []

print("\nWe're sorry folks, the Deli is out of pastrami!")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print("\nI made your " + current_sandwich + " sandwich!")
	finished_sandwiches.append(current_sandwich)

print("\nSandwich orders are done for " )

for finished_sandwiches in finished_sandwiches:
	print("The " + finished_sandwiches.title() + " sandwich!")

print("\nTaking more sandwich orders!")

# end program



# Below is the Dream Vacation program


name_dream_vaca = {}

polling_active = True

while polling_active:
	name = input("What is your name? > ")
	dream_vaca = input(name.title() + ", where is your dream vacation? > ")

	name_dream_vaca[name] = dream_vaca

	continue_poll = input("Continue asking others for this poll? \nENTER (yes/no) > ")
	if continue_poll.lower() == 'no':
		polling_active = False

for name, dream_vaca in name_dream_vaca.items():
	print("\n------Poll Results------")
	print(name.title() + " would LOVE to go to " + dream_vaca.title() + "!")

