from collections import OrderedDict

user_0 = OrderedDict()

user_0['username'] = 'bodhinaut'
user_0['first'] = 'kyle'
user_0['last'] = 'shive'

for value, key in user_0.items():
	print("The " + value + " is " + key + ".")
