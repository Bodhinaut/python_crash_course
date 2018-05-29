polling_active = True

while polling_active:
	#Prompt for the person's name and response.
	name = input("\nWhat is your name? < ")
	mtn_quest = input("Which mountain would you like to climb someday? < ")

	#Store response in the dictionary:
	name_mtn_quest[name] = mtn_quest

	#Anyone else want to take?
	repeat = input("Would you like to let another person respond? (yes/no) < ")
	if repeat.lower() == 'no':
		polling_active = False

	#Polling complete, show results,

	print("\n--- Poll Results ---")
	for name, mtn_quest in name_mtn_quest.items():
		print(name.title() + " would like to climb " + mtn_quest.title() + ".")

