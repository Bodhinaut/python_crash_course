# The keyword with closes the file once access to it is no longer needed. 
# here is an example of a file path 
# example of absolute path
# file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
# with open(file_path) as file_object:

#with open('py_text_files/pi_digits.txt') as file_object:
#	contents = file_object.read()
#	print(contents.rstrip() )


filename = 'py_text_files/pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
		print(line.rstrip() )


