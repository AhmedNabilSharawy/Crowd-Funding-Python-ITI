from userOperation import *
from projectOperation import *

def mainMenu():
    choice = validString(""" **********************************************
    Press:
        n : to add new user
        l : to list projects
        a : to add new Project
        r : to remove existing project
        u : to update existing project.
        e : to exit program
    -> : """)
    return choice

def switch():
    choice = mainMenu()
    if choice == "n":
        return addUser()
    elif choice == "l":
        return listProjects()
    elif choice == "a":
        return addNewProject()
    elif choice == "r":
        return deleteProject()
    elif choice == "u":
        return updateProject()
    elif choice == "e":
        exit()
    
while True: 
    switch()