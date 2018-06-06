
print("(When finished please enter 'q' to quit..)")
filename = 'guest_book.txt'
while True:
	name = input("Please enter your name into our Guest Book: ")
	if name.lower() == 'q':
		break
	
	print("Thanks for coming " + name + "!")

	with open(filename, 'a') as file_object:
		file_object.write(name.title() + "\n")


