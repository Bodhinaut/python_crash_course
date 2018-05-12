# find all numbers divisible by seven but are not a multiple of 5
# between num1 and num2

def search_find(num1, num2):
    array = []
    for x in range(num1, num2):
        if (x % 7 == 0) and (x % 5 != 0):
            array.append(str(x) )

    print (array)


search_find(2000, 3201)
