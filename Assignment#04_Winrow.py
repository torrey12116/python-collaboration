# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 19:30:13 2025

@author: Torrey
"""
ListOfTasks = ["Do Laundry", "Go to Gym", "Study for test Tuesday"]
#============================================================================

def ViewList(): #function that iterates through list of tasks and prints the tasks out
    for i in range(len(ListOfTasks)):
        print("Task", i + 1, "is", ListOfTasks[i])
        
#=====================================================================================================================

def AddToList(): #function to add tasks to list
    AddToList = input("What task would you like to add?") #figures out what task the user would like to add
    ListOfTasks.append(AddToList) #function to add to the list
    
    print("The new list of tasks is: ") #prints out the new list using a loop including the new task
    for i in range(len(ListOfTasks)):
        print("Task",  i + 1, "is", ListOfTasks[i])
        
#=======================================================================================================================

def DeleteFromList(): #function to delete task from list
    print("This is your current list of tasks") #shows user the list by printing it out using a loop
    for i in range(len(ListOfTasks)):
        print("Task", i + 1, "is", ListOfTasks[i])
        
    DeleteTask = eval(input("Which task would you like to delete (give numerical value):")) #User says which number task to delete
    ValueOfList = DeleteTask - 1 #python starts counting at 0 so the minus one accounts for that
    ListOfTasks.pop(ValueOfList) #Deletes that task from list

    print("Your new list is:") #prints new list using for loop to iterate through tasks
    for i in range(len(ListOfTasks))    :
        print("Task", i + 1, "is", ListOfTasks[i])
        
#========================================================================================================================

def main(): #main function to run the code using other functions
    RepeatAgain = "y" #variable to decide whether the user wants to run again
    while RepeatAgain == "y": #while the repeating again variable is equal to y...runs this code below
        UserAnswer = input("Do you want to view your tasks? (Please respond with y or n).") #asks user if they want to view tasks
        if UserAnswer == "y": #if user wants to see their tasks, runs ViewList Function
            ViewList()
        else: #otherwise asks user if they would like to add more tasks
            UserAddition = input("Would you like to add more tasks? (Please respond with y or n).")
            if UserAddition == "y": #if the user does want to add more tasks
                AddToList() #runs AddtoList Function
            else: #otherwise checks if user wants to delete tasks
                UserSubtraction = input("Would you like to delete a task from the list? (Please respond with y or n).")
                if UserSubtraction == "y": #if they say yes...
                    DeleteFromList() #runs DeleteFromList function
        RepeatAgain = input("Would you like to continue? (Please respond with y or n).") #checks if user wants to run the loop again
#========================================================================================================================
main() #calls the main function to run
    
    
    