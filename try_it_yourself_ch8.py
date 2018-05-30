# 8 - 1 Message

def display_message():
	print("This chapter I am learning about methods err.. (cough cough.. I mean...) function")

display_message()

# 8 - 2 

def favorite_book(title):
	print("\nOne of my favorite books is " + title.title() + ".\n")

favorite_book("Zen Baggage")

# 8 - 3 T- shirt ; 8 - 4 Large shirts

def make_shirt(size = 'L', text = 'I love python'):
	print("T-shirt size: " + size.upper() + "\nT-shirt text: " + text.upper() )

make_shirt("L", "digi_mon")
make_shirt(text = "digi", size = 's')
make_shirt() # default values
make_shirt('m') # default with medium size
make_shirt(text = 'Python for life') # only change text


print("\n----------------------------------------------")

# 8 - 5 Cities 


def describe_city(city, country = "Ireland"):
	print(city.title() + ", is in " + country.title() + ".")

describe_city("reykjavik", "iceland")
describe_city("dublin")
describe_city("kilarney")


print("\n--------------------------------------------------\n")
# 8-6 City Names
def city_country(city, country):
	return(city.title() + ', ' + country.title() )

print(city_country('santiago', 'chile') )
print(city_country('belfast', 'ireland') )
print(city_country('haining', 'china') )

print("\n--------------------------------------------------\n")
# 8-7 and 8-8 Album && User Albums

def make_album(artist_name, album_title, tracks = ''):
	album = {'name' : artist_name, 'title' : album_title}

	if tracks:
		album['tracks'] = tracks

	return album

print(make_album('vampire weekend', 'contra', 15))
print(make_album('pink floyd', 'animals'))
print(make_album('tycho', 'dive'))


# while loop practice with make_album

while True:
	print("\nPlease tell me the artist's name and album, number of tracks is optional: ")
	print("\n(ENTER Q AT ANY TIME TO QUIT)")
	a_name = input("Artist name: ")
	if a_name.upper() == 'Q':
		break

	al_name = input("Album name: ")
	if al_name.upper() == 'Q':
		break

	track = input("Number of tracks: ")
	if track.upper() == 'Q':
		break

	formatted_album = make_album(a_name, al_name, track)
	
	print("Following are the albums info: " + str(formatted_album) + ".")
	
