import os
from time import sleep as s


def display_tasks():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("============================================\n")
    with open("list.txt",'r') as database:
        list = database.readlines()
        if list == []:
            print("Looks like you have completed all you taks enter 1 to add new ones\n")
        else:
            for i,l in enumerate(list):
                print(f"{i+1}. {l}")
            
    print("\n============================================\n")
def add_single():
    print("\nEnter the new task:")
    task_to_be_added = input()
    with open("list.txt",'a') as database:
        database.write(task_to_be_added+"\n")
        database.flush()

    print("\nYour task has been added succesfully\n")
    input("\nPress Enter to continue")
def add_multi():
    tasks_to_be_added = []
    while True:
        task_to_be_added = input("\nEnter the new task:")
        if task_to_be_added:
            tasks_to_be_added.append(task_to_be_added+"\n")
        
        else:
                break
    
    if not(tasks_to_be_added):#doesnt add anything if the list is empty
        print("\nThe task is empty hence nothing will be added\n")

    elif tasks_to_be_added:
        with open("list.txt",'a') as database:
            database.writelines(tasks_to_be_added)
            database.flush()
        print("\nYour task has been added succesfully\n")
        input("\nPress Enter to continue")
def delete_task():
        task_to_be_deleted = int(input("Enter the task number to delete:"))-1
        with open("list.txt",'r') as database:
            list = database.readlines()
        with open("list.txt",'w') as database:
            database.writelines(list[0:task_to_be_deleted]+list[task_to_be_deleted+1::])
def change_task():
    task_to_be_changed = int(input("Enter the task number to edit:"))-1
    print("Enter the edited task:")
    task_to_be_changed_into = input()+ "\n"

    with open("list.txt",'r') as database:
        list = database.readlines()
    with open("list.txt",'w') as database:
        database.writelines(list[0:task_to_be_changed]+[task_to_be_changed_into]+list[task_to_be_changed+1::])
def clear_tasks():
    with open("list.txt",'w') as database:
        pass
def done_task_single():
    completed_task = int(input("Enter the completed task:"))-1
    with open("list.txt",'r') as database:
        list = database.readlines()
        print(str(list)+","+str(completed_task))
    with open("list.txt",'w') as database:
        database.writelines(list[0:completed_task]+list[completed_task+1::])
    with open("completed list.txt",'a') as database:
        database.write(list[completed_task])
        database.flush()
    display_tasks()
def done_task_multi():
    while True:
        completed_task = int(input("Enter the completed task:"))-1
        if completed_task:
            with open("list.txt",'r') as database:
                list = database.readlines()
                print(str(list)+","+str(completed_task))
            with open("list.txt",'w') as database:
                database.writelines(list[0:completed_task]+list[completed_task+1::])
            with open("completed list.txt",'a') as database:
                database.write(list[completed_task])
                database.flush()
        else:
            display_tasks()
def display_completed():
    print("============================================\nCompleted Tasks:")
    with open("completed list.txt",'r') as database:
        list = database.readlines()
        for i,l in enumerate(list):
            print(f"{i+1}. {l}")
    print("============================================\n")
    input("Press Enter to display the user menu")
    user_menu()
def clear_completed():
    with open("completed list.txt",'w') as database:
        pass

def display():
    display_tasks()
    input("Press any key to open the user menu to perform actions ")
    user_menu()

def add():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        choice = int(input('''============================================
    Would you like to:
    1. Add a single task
    2. Add multiple tasks
    3. User Menu
============================================
    Enter your choice: '''))
        if choice == 1:
            add_single()

        elif choice == 2:
            add_multi()

        elif choice == 3:
            break

def update():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        choice = int(input('''============================================
    Would you like to:
    1. Delete a task
    2. Edit a existing tasks
    3. Clear all the tasks
    4. User menu
============================================
    Enter your choice: '''))
        if choice == 1:
            display_tasks()
            delete_task()

        elif choice == 2:
            display_tasks()
            change_task()

        elif choice == 3:
            display_tasks()
            clear_tasks()

        elif choice == 4:
            break

def completed():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        choice = int(input('''============================================
    Would you like to:
    1. Display completed task
    2. Clear completed tasks
    3. User Menu
============================================
    Enter your choice: '''))
        if choice == 1:
            display_completed()

        elif choice == 2:
            clear_completed()

        elif choice == 3:
            break
    
def done():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        choice = int(input('''============================================
    Would you like to:
    1. Tick a single completed task
    2. Tick multiple completed tasks
    3. User Menu
============================================
    Enter your choice: '''))
        if choice == 1:
             done_task_single()

        elif choice == 2:
            done_task_multi()

        elif choice == 3:
            break
    
def user_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        choice = int(input('''============================================
    1. Add a new Task(multiple/single)
    2. Update tasks
    3. Tick off a completed task(multiple/single)
    4. Completed tasks(display/clear)
    5. Display the tasks
============================================
    Enter your choice:'''))
    
        if choice == 1:
            add()


        elif choice == 2:
            update()

        elif choice == 3:
            done()
            break

        elif choice == 4:
            completed()

        elif choice == 5:
            break
    
while True:
    display()
