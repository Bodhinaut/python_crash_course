import string
filename = 'program_poll.txt'
print("Please enter 'q' to terminate program..")
while True:
	reason = input("Please enter why you like programming: ")
	if reason == 'q':
		break

	with open(filename, 'a') as file_object:
		file_object.write(string.capwords(reason) + "\n" )
