'''
alien_color = 'red'

if alien_color == 'green':
    print("Player just recieved 5 points!")
else:
    print("You earned 10 points!")


age = 70

if age < 2:
    print("You are a baby. Go to sleep.")
elif age >= 2 and age < 4:
    print("You are a toddler. Go to sleep.")
elif  age >= 4 and age < 13:
    print("You're still a kid, so, go do something away from here.")
elif age >= 13 and age < 20:
    print("You are a teenager, go skate and write poems while you have the chance..")
elif age >= 20 and age < 65:
    print("You made it, congrats adult, go get a job.")
elif age >= 65:
    print("You are an elder, I hope your life was enjoyable.")


favorite_fruits = ['orange', 'fig', 'grapes', 'bananas']

if 'orange' in favorite_fruits:
    print("Oranges are in this list!")
if 'fig' in favorite_fruits:
    print("So you dig the fig?")
if 'grapes' in favorite_fruits:
    print("not for dogs dog")
if 'Bananas'.lower() not in favorite_fruits:
    print("Bananas are not in this list? I know you love them though!")


usernames = ['admin', 'kshive', 'acornell', 'theo', 'lyla']
# usernames = []

if not usernames:
    print("Users are empty, we need to make some users!")

for user in usernames:
    if user == 'admin':
        print("Hello Administrator, would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again.")



current_users = ['admin', 'kshive', 'acornell', 'theo', 'lyla']

new_users = ['sean', 'lucas', 'mike', 'linda', 'THEO', 'lyla']


for users in new_users:
    if users.lower() in current_users:
        print("That username already exits, please choose a different name!")
    else:
        print("You're in luck, that username is available!")



ordinal_num = list(range(1 , 10) )

for num in ordinal_num:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")


'''
































