filename = 'learning_python.txt'
txt_string = ''

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	txt_string += line.strip() + "\n"

txt_string = txt_string.replace('Python', 'Ruby')
print(txt_string)


