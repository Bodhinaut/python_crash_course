from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['kyle'] = 'python'
favorite_languages['zach'] = 'c++'
favorite_languages['alan'] = 'shell'
favorite_languages['tulodo-san'] = 'ruby'

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + 
		  language.title() + ".")