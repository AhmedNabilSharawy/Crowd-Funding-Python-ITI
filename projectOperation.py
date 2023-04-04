from fileOperation import *
from validations import *
from userOperation import *


def addNewProject():
    projTitle = validString("Enter Project Title: ")
    projDetails = input("Enter Project Details: ")
    projTarget = validInteger("enter Project Target: ")
    start_time = checkDate("Enter Start Time: ")
    end_time = checkDate("Enter End Time: ")
    owner = setProjectOwner()
    newProject = f"{projTitle}:{projDetails}:{projTarget}:{start_time}:{end_time}:{owner}\n"
    saveUserData(newProject, "projects.txt")


def setProjectOwner():
    while True:
        ownerName = validString("Enter Owner Name: ")
        ownerPassword = input("Enter Owner Password: ")
        owner = checkUserInDb(ownerName, ownerPassword)
        if owner == True:
            return ownerName
        else:
            print("Check your credentials again")


def listProjects():
    print("Project Title: Project Details : Project Target : Start Time : End Time : Owner ")
    projectList = readFileData("projects.txt")

    for project in projectList:
        p = project.strip("\n").split(":")
        print(f"{p[0]}:{p[1]}:{p[2]}:{p[3]}:{p[4]}:{p[5]}")


def checkProjectInDb(title):
    projectList = readFileData("projects.txt")
    for project in projectList:
        if title == project.strip("\n").split(":")[0]:
            return True
    else:
        return False


def updateProject():
    title = input("Enter Title of project: ")
    checkProject = checkProjectInDb(title)
    if checkProject == True:
        while True:
            choice = int(validInteger(
                "Enter Number-> (0)Title,(1)Details,(2)Target,(3)Start Time,(4) End Time, (5)Owner: "))
            value = validString("Enter updated Value: ")
            projectList = readFileData("projects.txt")
            for i in range(len(projectList)):
                p = projectList[i].strip("\n").split(":")
                if title == p[0]:
                    p[choice] = value
                    projectList[i] = ":".join(p)+"\n"
                    writeFileData(projectList, "projects.txt")
                    print(projectList[i])
                    print ("Record updated Successfully")
                    return True
    else:
        return False


def deleteProject():
    title = input("Enter Title of project: ")
    checkProject = checkProjectInDb(title)
    if checkProject == True:
        projectList = readFileData("projects.txt")
        for i in range(len(projectList)):
            p = projectList[i].strip("\n").split(":")
            if title == p[0]:
                ownerName = checkOwner(p[5])
                if ownerName == True:
                    projectList.remove(projectList[i])
                    writeFileData(projectList, "projects.txt")
                    print ("Record Deleted Successfully")
                    return True
                else:
                    print ("Unauthorized,Check your Credintials")
                    return False
    else:
        print ("No Project Found")
        return False
    

    