filename = 'learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

txt_string = ''

for line in lines:
	print (line)
	txt_string += line.strip() + "\n"

print(txt_string)


with open('learning_python.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip() )