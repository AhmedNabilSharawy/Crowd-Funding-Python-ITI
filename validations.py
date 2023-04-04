from datetime import datetime
import re

def validString(message):
    while True:
        userInput = input(message)
        if (userInput).isalpha():
            return userInput
        else:
            print ("Please Enter String only")
        

def validInteger(message):
    while True:
        userInput = input(message)
        if userInput.isdigit():
            return userInput
        else:
            print ("Please Enter Numbers only")
            
def confirmPassword(password):
    while True:
        confPassword = input("Confirm Password: ")
        if confPassword == password:
            return confPassword
        else:
            print ("Password does not match")


def checkEmail(message):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    while True:
        userEmail = input(message)
        if re.fullmatch(regex, userEmail):
            break
    return userEmail

def checkPhoneNumber(message):
    regex = r'^01[0125][0-9]{7,8}$'
    while True:
        userNumber = input(message)
        if re.fullmatch(regex, userNumber):
            break
    return userNumber
        
def checkDate(message):
    while True:
        userDate = input(message)
        datetime_str = userDate
        try:
            datetime_object = datetime.strptime(datetime_str, '%m/%d/%y')
        except Exception as e:
            print (e)
        else:
            return(datetime_object.date()) 
    