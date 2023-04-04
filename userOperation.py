from fileOperation import *
from validations import * 

def addUser():
    userFirstName = validString("Enter your first name: ")
    userLastName = validString("Enter your last name: ")
    userEmail = checkEmail('Enter your email: ')
    userPassword = input('Enter password: ')
    confPassword = confirmPassword(userPassword)
    userPhoneNumber = checkPhoneNumber("Enter phone number: ")
    newUser = f"{userFirstName}:{userLastName}:{userEmail}:{userPassword}:{userPhoneNumber}\n"
    saveUserData(newUser,"users.txt")

def checkUserInDb(userName,userPassword):
    userList = readFileData("users.txt")
    for user in userList:
        if userName == user.strip("\n").split(":")[0]:
            if userPassword == user.strip("\n").split(":")[3]:
                return True
    else:
        return False
      
def login():
    userName = validString("Enter your name: ")
    userPass = input("Enter your password: ")
    checkUser = checkUserInDb(userName,userPass)
    if checkUser == True:
        print("You are logged in")
        return True
    else:
        print (f"Check your Credintials")
        return False
    
def checkOwner(onwerName):
    userName = onwerName
    userPass = input("Enter Owner password: ")
    checkUser = checkUserInDb(userName,userPass)
    if checkUser == True:
        return True
    else:
        return False
    