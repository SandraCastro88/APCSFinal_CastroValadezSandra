import random 

print("Hi! Lets generate a password")

#Define the list of characters
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijkmnlopqrstuvwxyz!@#$%^&*"

#Ask the user how long they want the password to be
passwordLenght = int(input("How many characters long would you like your password to be?"))
#Generate a random password
newPassword = []
for x in range(passwordLenght):
    #Append a random character to the password string 
    newPassword.append(random.choice(characters))
    
#Join the list back into a string 
finalpassword = ''.join(map(str, newPassword))
#every index in newPassword is being converted into a string and then it will be joined together with no spacing which will then be added into the string 

#Tell the user their new password
print("\n This is your new password:", finalpassword)
