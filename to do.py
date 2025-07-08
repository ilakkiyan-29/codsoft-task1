import os
from time import sleep as s

try:
    def display_tasks():
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Press ctr+c anywhere to quit")
        print("============================================\n")
        with open("list.txt",'r') as database:
            list = database.readlines()
            if list == []:#if there is no tasks
                print("Looks like you have completed all you'r tasks \n\n\"You can add new tasks using the user menu press enter to open it\"  \n")
            else:
                for i,l in enumerate(list):
                    print(f"{i+1}. {l}")
                
        print("\n============================================\n")

    def add_single():
        task_to_be_added = input("\nEnter the new task(leave it blank if want to go back):")
        if task_to_be_added:
            with open("list.txt",'a') as database:
                database.write(task_to_be_added+"\n")
                database.flush()#not required but just in case

            print("\nYour task has been added succesfully\n")

        else:#doesnt add anything if the task is empty
            print("\nThe task is empty hence nothing will be added\n")  
        
        input("Press enter to continue")      

    def add_multi():
        tasks_to_be_added = []
        while True:
            task_to_be_added = input("\nEnter the new task:").strip()
            if task_to_be_added:
                tasks_to_be_added.append(task_to_be_added+"\n")
            
            else:#if the user leave a task empty then the loop ends
                    break
        
        if not(tasks_to_be_added):#doesnt add anything if the list is empty
            print("\nThe list of task is empty hence nothing will be added\n")

        elif tasks_to_be_added:
            with open("list.txt",'a') as database:
                database.writelines(tasks_to_be_added)
                database.flush()
            print("\nYour task has been added succesfully\n")

        input("\nPress Enter to continue")

    def delete_task():
            try:
                task_to_be_deleted = int(input("Enter the task number to delete(0 to not delete any):"))-1

            except ValueError:
                input("\nEnter a valid option\nPress Enter to continue")
            
            with open("list.txt",'r') as database:
                list = database.readlines()
            with open("list.txt",'w') as database:
                database.writelines(list[0:task_to_be_deleted]+list[task_to_be_deleted+1::])

    def change_task():
        try:
            task_to_be_changed = int(input("Enter the task number to edit:"))-1
        
        except ValueError:
            input("\nEnter a valid option\nPress Enter to continue")    

        task_to_be_changed_into = input("Enter the edited version task:")+ "\n"

        if task_to_be_changed_into:
            with open("list.txt",'r') as database:
                list = database.readlines()
            with open("list.txt",'w') as database:
                database.writelines(list[0:task_to_be_changed]+[task_to_be_changed_into]+list[task_to_be_changed+1::])
            print("The task is successfully changed")

        else:
            print("\nThe task cannot be empty\n")  
        
        input("Press enter to continue") 

    def clear_tasks():
        with open("list.txt",'w') as database:
            pass

    def done_task_single():
        try:
            completed_task = int(input("Enter the completed task:"))-1

        except ValueError:
            input("\nEnter a valid option\nPress Enter to continue")    

        try:
            with open("list.txt",'r') as database:
                list = database.readlines()
                list[completed_task]

        except IndexError:
            input("\nEnter a valid option\nPress Enter to continue")    
            return
        
        with open("list.txt",'w') as database:
            database.writelines(list[0:completed_task]+list[completed_task+1::])
        with open("completed list.txt",'a') as database:
            database.write(list[completed_task])
            database.flush()

        display_tasks()
        input("Press enter to continue")

    def done_task_multi():
        while True:
            try:
                display_tasks()
                completed_task = int(input("Enter the completed task(0 to leave):"))-1

            except ValueError:
                input("\nEnter a valid option\nPress Enter to continue")    

            if completed_task >= 0:
                    try:
                        with open("list.txt",'r') as database:
                            list = database.readlines()
                            list[completed_task]

                    except IndexError:
                        input("\nEnter a valid option\nPress Enter to continue")    
                        return
                    
                    with open("list.txt",'w') as database:
                        database.writelines(list[0:completed_task]+list[completed_task+1::])
                    with open("completed list.txt",'a') as database:
                        database.write(list[completed_task])
                        database.flush()
            else:
                break 

        input("Press enter to continue")
        
    def display_completed():
        print("============================================\nCompleted Tasks:")
        try:
            with open("completed list.txt",'r') as database:
                list = database.readlines()
                if list != []:
                    for i,l in enumerate(list):
                        print(f"{i+1}. {l}")
        
                else:
                    print("No tasks is completed\n")
        except FileNotFoundError:
            print("A file is missing")

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
            try:
                choice = int(input('''\t---Press ctr+c to quit---
============================================
Would you like to:
1. Add a single task
2. Add multiple tasks
3. User Menu
============================================
Enter your choice: '''))
            
            except ValueError:
                input("\nEnter a valid option\nPress Enter to continue")
                continue

            if choice == 1:
                add_single()

            elif choice == 2:
                add_multi()

            elif choice == 3:
                break

            else:
                input("\nEnter a valid option\nPress Enter to continue")
                continue 

    def update():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                choice = int(input('''\t---Press ctr+c to quit---
============================================
Would you like to:
1. Delete a task
2. Edit a existing tasks
3. Clear all the tasks
4. User menu
============================================
Enter your choice: '''))
                
            except ValueError as e:
                input("\nEnter a valid option\nPress Enter to continue")
                continue

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

            else:
                input("\nEnter a valid option\nPress Enter to continue")
                continue 

    def completed():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                choice = int(input('''\t---Press ctr+c to quit---
============================================
Would you like to:
1. Display completed task
2. Clear completed tasks
3. User Menu
============================================
Enter your choice: '''))
            except:
                input("\nEnter a valid option\nPress Enter to continue")
                continue

            if choice == 1:
                display_completed()

            elif choice == 2:
                clear_completed()

            elif choice == 3:
                break

            else:
                input("\nEnter a valid option\nPress Enter to continue")
                continue 

    def done():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                choice = int(input('''\t---Press ctr+c to quit---
============================================
Would you like to:
1. Tick a single completed task
2. Tick multiple completed tasks
3. User Menu
============================================
Enter your choice: '''))
            
            except ValueError:
                input("\nEnter a valid option\nPress Enter to continue")
                continue

            if choice == 1:
                display_tasks()
                done_task_single()

            elif choice == 2:
                display_tasks()
                done_task_multi()

            elif choice == 3:
                break

            else:
                input("\nEnter a valid option\nPress Enter to continue")
                continue 

    def user_menu():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                choice = int(input('''\t---Press ctr+c to quit---
============================================
1. Add a new Task(multiple/single)
2. Update tasks
3. Tick off a completed task(multiple/single)
4. Completed tasks(display/clear)
5. Display the tasks
============================================
Enter your choice:'''))
            
            except ValueError as e:
                input("\nEnter a valid option\nPress Enter to continue")
                continue

            if choice == 1:
                add()

            elif choice == 2:
                update()

            elif choice == 3:
                done()

            elif choice == 4:
                completed()

            elif choice == 5:
                display()
                
            else:
                input("\nEnter a valid option\nPress Enter to continue")
                continue 

    while True:
        display()

except KeyboardInterrupt:
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in "Thanks for using":
        s(0.07)
        print(i,end = '')
    quit()