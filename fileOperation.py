def saveUserData(userData,fileName):
    try:
        usersFile = open(fileName, "a")
    except FileNotFoundError as e:
        print(e)
    else:
        usersFile.write(userData)
    usersFile.close()

def readFileData(fileName):
    try:
        usersFile = open(fileName, "r")
    except FileNotFoundError as e:
        print(e)
    else:
        data = usersFile.readlines()
        return data

def writeFileData(data,fileName):
    try:
        fileName = open(fileName, "w")
    except FileNotFoundError as e:
        print(e)
    else:
        fileName.writelines(data)
    fileName.close()