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