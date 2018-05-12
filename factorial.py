def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print("Please enter a number to recieve its factorial.")
num = int(input() )
print (factorial(num))

# good recursion practice


