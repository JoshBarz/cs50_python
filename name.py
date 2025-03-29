# Ask the user their name
name = input("What is your name? ")

# Remove whitespace from a string
name = name.strip() 

# Capitalise the first letter of each word in a string
name = name.title()

# Split a string into multiple values which can also be assigned into separate variables
first, last = name.split(" ")


print (f"Hello, {first}")
