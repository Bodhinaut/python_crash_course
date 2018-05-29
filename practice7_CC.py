#message = (input("Tell me something, and I will repeat it back to you: ") )
#print(message)

#print("-----------------------------------------------------------------------")

#prompt = "If you tell us who you are, we can personalize the messages you see."
#prompt += "\nWhat is your first name? "

#name = input(prompt)
#print("\nHello " + str(name.title() ) + "." )

#age = input("How old are you? ")
#age = int(age)
#print(age)



#rental_car = input("What kind of rental car would you like to see? : ")
#print("Let me see if I can find you a " + rental_car.title() + "!")

'''
ppl_table = input("How many people are in your dinner group? : ")
ppl_table = int(ppl_table)

if ppl_table > 8:
	print("I am sorry, for " + str(ppl_table) + " people you will have to wait.")
else:
	print("Great, right this way!")

'''

'''
number = input("Please, give me the Great Binary Buddha a number: ")
number = int(number)

if number % 10 == 0:
	print(str(number) + ", is a multiple of 10.")
else:
	print(str(number) + " is not a multiple of 10.")

'''
'''
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program : "

message = ""
while message.lower() != 'quit':
	message = input(prompt)
	if message.lower() != 'quit':
		print(message)
print("Program has ended.")
print(message)
'''
'''
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program : "

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)
'''
'''
prompt = "\nPlease enter the name of a city you have visited:"
prompt +=  "\n(Enter 'quit' when you are finished.) "


while True:
	city = input(prompt)

	if city.lower() == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")
'''
'''
current_num = 0
while current_num < 10:
	current_num += 1
	if current_num % 2 == 0:
		continue

	print(current_num)
'''
'''
prompt = "Please enter the toppings you want for your pizza: "
prompt += "\n(Please enter QUIT when finished) : "

while True:
	message = input(prompt)
	if message.upper() == 'QUIT':
		print("Your pizza will be ready shortly!")
		break
	else:
		print("Thank you for adding " + message + ", that topping will be delicious!")
	
'''

'''

while True:
	try:
		message = int(input("What is your age? : ") )
	except ValueError:
		print("Please tell me a real age, in integer format..")
		continue

	
	if int(message) < 3:
		print("Your ticket is free!")
		break
	elif int(message) > 3 and int(message) < 12:
		print("Your ticket is $10, I know it's bullshit..")
		break
	elif int(message) > 12 and message < 100:
		print("Your ticket comes to $12, I know, capitalism...")
		break
	elif message > 99:
		print("Damn you old, just go in...")
		break
'''
'''

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("Verifying user: " + current_user.title() )
	confirmed_users.append(current_user)

	# Display all confirmed users.
	print("\nThe following users have been confirmed: ")
	for confirmed_user in confirmed_users:
		print(confirmed_user.title() )

'''

'''
name_mtn_quest = {}

# Set a flag to indicate that polling is active


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

'''




