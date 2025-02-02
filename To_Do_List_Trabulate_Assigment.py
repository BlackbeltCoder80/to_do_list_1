# Task Create User Interface
# Created UI using import tabulate 
from tabulate import tabulate
# Menu for Task Outline
selection_table = [["\nWelcome to the To-Do List App"],
                    ["1. Add a task"],
                    ["2. View task"],
                    ["3. Mark a task as complete"],
                    ["4. Delete task"], 
                    ["5. Quit"]]
task = [] # Stores List or Tasks

def menu():
    "Displays Menu Using Tabulate"
    print(tabulate(selection_table, tablefmt="grid")) # Out put Table

# Adding Task
def add_task():
    #Menu Using Tabulate
    title_task = input("Please Enter Title of task:")
    if title_task:
        task.append({"Title":title_task, "Status": "Incomplete"})
        print(f"Your task. {title_task}, has been added succesfully")
    else:
        print("Task Title cannot be empty")

# View Current Task and Status
def view_task():
    """Displays tasks in a formatted table with numbers"""
    if not task:
        print("There are no tasks to view.")
    else:
        numbered_tasks = [{"Number": i + 1, "Title": t["Title"], "Status": t["Status"]} for i, t in enumerate(task)]
        print("\nYour Current Tasks:")
        print(tabulate(numbered_tasks, headers="keys", tablefmt="grid"))  # Displays as a table

# Completed Tasks
def completed_task():
    
    view_task()
    
    try:
        task_num = int(input("Please enter the number of the task you wish to mark completed"))
        
        if 1 <= task_num <= len(task):
            task[task_num -1]["Status"] = "Complete"
            print(f"\nTask '{task[task_num -1 ]["Title"]}' market as completed.")
        else:
            print("\Invalid task number. PLease select a number from the list")
    except ValueError:
            print("\nInvalid input! Please enter a number")

#Delete a Task
def delete_task():
    
    view_task()
    try:
        task_num = int(input("\nEnter the number of the task to delete: "))

        if 1 <= task_num <= len(task):
            removed_task = task.pop(task_num - 1)  # Remove the selected task
            print(f"\nTask '{removed_task['Title']}' has been deleted.")
        else:
            print("\nInvalid task number! Please choose from the list.")

    except ValueError:
        print("\nInvalid input! Please enter a number.")

# Menu Loop
while True:
    menu()
    choose_task =input("Add Select number: ")
    if  choose_task == "1":
        add_task()
    elif choose_task == "2":
        view_task()
    elif choose_task == "3":
        completed_task()
    elif choose_task == "4":
        delete_task()
    elif choose_task == "5":
        print("Goodbye!")
        break
    else:
        print("\nInvalid input! Please enter a number between 1 and 5.")


        