
user_0 = {
	'username' : 'bodhi',
	'first' : 'kyle',
	'last' : 'shive',
	}

for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)


fav_lang = {
	'kyle' : 'python',
	'zach' : 'c++',
	'justin' : 'java',
	'cody' : 'java',
	'socrates' : 'swift',
}

for name, lang in fav_lang.items():
	print ("\n" + name + ' : ' + lang)



skate_ppl_brands = {
	'mullen' : 'enjoi',
	'dollin' : 'baker',
	'mike v' : 'element',
	'bam' : 'element',
	'kyle' : 'mystery',
}

for names, decks in skate_ppl_brands.items():
	print(names.title() + " skates the " + decks.title() + " brand deck.")

for decks in skate_ppl_brands.values():
	print ("\n" + decks.title() )

for names in sorted(skate_ppl_brands.keys() ):
	print ("\n" + names.title() ) 






friends = ['bill', 'elon', 'jobs', 'zuckerberg', 'kyle', 'zach']


fav_lang = {
	'kyle' : 'python',
	'zach' : 'c++',
	'justin' : 'java',
	'cody' : 'java',
	'socrates' : 'swift',
}

for not_taken in friends:
	if not_taken not in fav_lang.keys():
		print(not_taken.title() + ", please take our language poll!")

for taken in fav_lang.keys():
	if taken in friends:
		print(
			taken.title() + ", thank you for taking the poll!" + 
			" Your favorite language is " + fav_lang[taken].title() + "!"
			)
	


aliens = []

# Make 30 green aliens

for alien_number in range(30):
	new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
	aliens.append(new_alien)



for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15


# Show first five aliens 
for alien in aliens[:5]:
	print(alien)
print("...")


# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens) ) )




people = [
	{ 'first' : 'kyle',
	'lang' : 'python' },
	{'first' : 'zach',
	'lang' : 'c++'},
	{'first' : 'justin',
	'lang' : 'java'},
	]



for peoples in people:
	print(peoples)





juno = {'welsh terrier' : 'sean'}

zeus = {'chinchilla' : 'lucas'}

peaches = {'fairy' : 'family'}

pets = [juno, zeus, peaches]

for pet in pets:
	for key, value in pet.items():
		print(key + " " + value)





fav_places = {
	'raw beauty' : 'iceland',
	'livability and culture' : 'ireland',
	'best camping' : 'isle of sky',
	}


for rating, location in fav_places.items():
	print (rating.title() + " goes to " + location.title() )





cities = {
	'edinbrugh' : {"location" : "scotland", "pop" : "regular?", "fact" : "castles"},
	'galway' : {"location" : 'ireland', "pop" : "humble?", "fact" : "that music"},
	'haining' : {"location" : 'china', "pop" : "always massive", "fact" : "i miss it"},
	}


for key, values in cities.items():
	print ( str(key) + " " + str(values) )























