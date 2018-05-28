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

