# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 19:30:13 2025

@author: Torrey
"""
ListOfTasks = ["Do laundry", "Go to gym", "Study for test Tuesday"]
#============================================================================

def ViewList():
    for i in range(len(ListOfTasks)):
        print("Task", i + 1, "is", ListOfTasks[i])
        
#=====================================================================================================================

def AddToList():
    AddToList = input("What task would you like to add?")
    ListOfTasks.append(AddToList)
    
    print("The new list of tasks is: ")
    for i in range(len(ListOfTasks)):
        print("Task",  i + 1, "is", ListOfTasks[i])
        
#=======================================================================================================================

def DeleteFromList():
    print("This is your current list of tasks")
    for i in range(len(ListOfTasks)):
        print("Task", i + 1, "is", ListOfTasks[i])
        
    DeleteTask = eval(input("Which task would you like to delete (give numerical value):"))
    ValueOfList = DeleteTask - 1
    ListOfTasks.pop(ValueOfList)

    print("Your new list is:")
    for i in range(len(ListOfTasks))    :
        print("Task", i + 1, "is", ListOfTasks[i])
        
#========================================================================================================================

def main():
    RepeatAgain = "y"
    while RepeatAgain == "y":
        UserAnswer = input("Do you want to view your tasks? (Please respond with y or n).")
        if UserAnswer == "y":
            ViewList()
        else:
            UserAddition = input("Would you like to add more tasks? (Please respond with y or n).")
            if UserAddition == "y":
                AddToList()
            else:
                UserSubtraction = input("Would you like to delete a task from the list? (Please respond with y or n).")
                if UserSubtraction == "y":
                    DeleteFromList()
        RepeatAgain = input("Would you like to continue? (Please respond with y or n).")
#========================================================================================================================
main()
    
    
    