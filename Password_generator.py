import random


print("Hello! let's generate a password")
print("---------------------------------")

# list characters 
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"

# prompt the user 
passwordlength = int(input("How long would you like your password to be? "))

# generate a random password
new_password = []

for x in range (passwordlength):
# append a random character to the password string
    new_password.append(random.choice(characters))
    
# join the whole list back into a string
final_password = ''.join(map(str, new_password))


# let the user know their know password
print("\n This is your new Password: ", final_password)