'''
Input: username and password

Output:
Condition 1: if username and password are correct shows up a success message
Condition 2: if username is incorrect shows up a specific error message from username
Condition 3: if password is incorrect shows up a specific error message from password
'''
print("Login Validation")

username_db="test"
password_db="123456abc"

isValidUsername = input("Type the username:") == username_db
isValidPassword = input("Type the password:") == password_db

if isValidUsername and isValidPassword:
    print("Logged successfully!!!")
if isValidUsername and not isValidPassword:
    print("Password is incorrect!!! Try again.")
if not isValidUsername:
    print("Username not found!!! Try again.")






