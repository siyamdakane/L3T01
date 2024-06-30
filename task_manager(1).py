#=====importing libraries===========
'''This is the section where you will import libraries'''

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
''' 
# Reqeusts user to input username and password to login 
user_index = 0
while user_index <=8:
    user_index += 1
    username_list = []
    passwords = []  

    with open("user.txt", "r+", encoding="utf-8") as user_file: 
      
        for line in user_file:
            temp = line.strip()    # Strip function is done first in order to remove newline character
            temp = temp.split()
            username_list.append(temp[0])
            # By appending the index 0 we cssan add to usernames list
            passwords.append(temp[2]) # By appending the index 2 we can add to passwords list
 
        user_input = input("\nEnter a username:")
        user_password = input("Enter a password:")

        if user_input != username_list[user_index - 1] and user_password != passwords[user_index - 1]:
            print("You have not entered a valid username and password, please try again")
            
        elif user_input == username_list[user_index - 1] and user_password != passwords[user_index - 1]:
            print("You have not entered a valid password, please try again")
           
        elif user_input != username_list[user_index - 1] and user_password == passwords[user_index - 1]:
            print("You have not entered a valid username, please try again")
            
        else:
            print("You have successfully logged in")

            break  
         
 
while True:
# Present the menu to the user and 
# make sure that the user input is converted to lower case.
 menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
dt - display statistics
: ''').lower()
 
     
 if menu == 'r'and user_input == "admin":
        pass
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''
        
        user_file = open("user.txt", "a", encoding= "utf-8") 
        user_input = input("Enter a new username:")
        
        user_password = input("Enter a new password:")
        password_confirmation = input("Enter password for confirmation:")
        if user_input == "":
          continue

        if user_password == "":
            continue

        if user_password == password_confirmation:
             user_file.write("\n" +user_input + " " + ", " + " " + user_password )
    
        else:
          print("Enter the correct password")
          continue

        user_file.close()

 elif menu == 'r' and user_input != "admin":
    print("Only user admin can register users")
  
 
 elif menu == 'a':
        pass   
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''
        task_file = open("tasks.txt", "a", encoding="utf-8")
        username = input("Enter the username of the person whom the task is assigned to:")
        task_title = input("Title of the task:")
        task_description = input("The description of the task:")
        due_date = input("What is the due date of the task?:")
        from datetime import date 
        current_date = date.today()

        task_file.write(username + " " + ", " + " " + task_title + " " + ", " + " " +
                        task_description + " " + ", " + " " + due_date + " " + ", " + " " + current_date + "\n")
        
        task_file.close()

 elif menu == 'va':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''
        task_file = open("tasks.txt", "r")
        for line in task_file:
            print("Task:" + " " + line.split()[2],
            "\n" + "Assigned to:" + " " + line.split()[0],
            "\n" + "Date assigned:" + " " + line.split()[8],
            "\n" + "Due Date:" + " " + line.split()[6],
            "\n" + "Task complete: " + "" + "No", 
            "\n" + "Task description:" + " " + line.split()[4])

        task_file.close()

 elif menu == 'vm':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''
        task_file = open("tasks.txt", "r" , encoding= "utf-8")
        tasks_file = task_file.read()
        user =input("Enter your username:")
        
        for i in  range(0, len(tasks_file.split()) + 1):
         
         for line in task_file:
           
            if user == tasks_file.split()[10*i]:
                print("Task:" + " " + line.split()[i+2],
                "\n" + "Assigned to:" + " " + line.split()[i],
                "\n" + "Date assigned:" + " "+ line.split()[i+8],
                "\n" + "Due date:" + " " + line.split()[i+6],
                "\n" + "Task complete:" + " " + "No",
                "\n" + "Task description:" + " " + line.split[i+4])

        
           # Logic for user to view the tasks that are assigned to them,only display the tasks that have been assigned to the current user 
            else:
                print("User invalid to open file")

        task_file.close()
 
 elif menu == 'dt' :
        pass
        tasks_per_user = []
        user_file = open("user.txt", "r+" , encoding="utf-8") 
        task_file = open("tasks.txt", "r+" , encoding="utf-8" )
        users_file = user_file.read()
            
        if user_input == "admin":  
            tasks = task_file.split()
            tasks_calc = tasks_per_user.append(tasks[0])
            amount_of_tasks = len(tasks_calc)
            users = users_file.split(", ")
            amount_of_users = len(users)  - 1
            print("Total number of tasks:",amount_of_tasks)
            print("Total number of users:", amount_of_users)

        else:
           print("You cannot display statistics")

           user_file.close()
           task_file.close()
       
 elif menu == 'e':
     print('Goodbye!!!')
     exit()

 else:
        print("You have entered an invalid input. Please try again")
        
