import json
import datetime

file_path = r"task manger.json"
todays_date = datetime.date.today()
print("         the date is (" + str(todays_date) + ")\n")

try:
    # get the file if exsist
    with open(file_path, 'r', encoding='utf-8') as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []  # if there isnt file make empty one

def close_the_app():
    print("         good Bye \n         comme in another time :)")

def edit_task(task_id):
    if tasks != []:
        for task in tasks:
            if task["id"] == task_id:
                print("ok")
                new_title = input("          put the new title : ")
                new_description = input("          put the new discription : ")
                task["title"] = new_title
                task["description"] = new_description
                # Write the updated tasks back to the JSON file
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(tasks, file, indent=4, ensure_ascii=False)
                    print(f"task {task["title"]} tha succeflly edited")
                break
        else:
            print("wrong id")

def get_task_list():
    category = input("""
            write
            1 for all tasks
            2 for tasks marked with done
            3 for tasks marked with not done
            4 for tasks marked with in progress
                     """)
    if category == "1":
        if tasks != []:
            for task in tasks:
                print(100 * "_")
                print("task number " + str(task["id"]))
                print(task["title"])
                print(task["description"])
                print(task["status"])
                print(task["due_date"])
                print(100*"_")
    elif category == "2":
         if tasks != []:
            for task in tasks:
                if task["status"] == "done":
                    print(100 * "_")
                    print("task number " + str(task["id"]))
                    print(task["title"])
                    print(task["description"])
                    print(task["due_date"])
                    print(100*"_")
    elif category == "3":
         if tasks != []:
            for task in tasks:
                if task["status"] == "not done":
                    print(100 * "_")
                    print("task number " + str(task["id"]))
                    print(task["title"])
                    print(task["description"])
                    print(task["due_date"])
                    print(100*"_")
    elif category == "4":
         if tasks != []:
            for task in tasks:
                if task["status"] == "in progress":
                    print(100 * "_")
                    print("task number " + str(task["id"]))
                    print(task["title"])
                    print(task["description"])
                    print(task["due_date"])
                    print(100*"_")

def get_todays_tasks():
    if tasks != []:
        for task in tasks:
            if task["due_date"] == str(todays_date):
                print("task number " + str(task["id"]))
                print(task["title"])
                print(task["description"])
                print(task["due_date"])
                print(100*"_")


def add_task(title, description, due_date, filename=file_path):
    
    # get id for the task
    task_id = len(tasks) + 1
    
    # make new task
    new_task = {
        "id": task_id,
        "title": title,
        "description": description,
        "status": "not done",
        "due_date": due_date
    }
    
    tasks.append(new_task)
    
    # add to JSON file
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)
    
    print(f" sucsseful adding for : {title}, and his id is : {task_id}")

def remove_task(task_id):
    if tasks != []:
        for task in tasks:
            if task["id"] == task_id:
                tasks.remove(task)
                # Write the updated tasks back to the JSON file
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(tasks, file, indent=4, ensure_ascii=False)
                    print(f"task {task["title"]} has succeflly removed")

                break
        else:
            print("wrong id")

def mark_task_as_done(task_id):
    if tasks != []:
        for task in tasks:
            if task["id"] == task_id:
                print("ok")
                new_status = input("""           write the state of task
            -done
            -not done 
            -in progress
            """)
                task["status"] = new_status
                # Write the updated tasks back to the JSON file
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(tasks, file, indent=4, ensure_ascii=False)
                    print(f"task {task["title"]} has succeflly edited")
                break
        else:
            print("wrong id")

def main_loop():
    print(100 * "_")
    db = input("""          write 
            1 to see your tasks
            2 to see todays tasks
            3 to add a new task
            4 to change task catigory (done , not done , in progress)
            5 to edit task
            6 to remove a task
            0 to close the app
                        """)
    if db == "3":
        title = input("inter the title : ")
        description = input("add the description : ")
        add_task(title, description, str(todays_date))
        main_loop()
    elif db == "1":
        get_task_list()
        main_loop()
    elif db == "2":
        get_todays_tasks()
        main_loop()
    elif db == "6":
        task_id = input("enter the id of the task : ")
        remove_task(int(task_id))
        main_loop()
    elif db == "5":
        task_id = input("enter the id of the task : ")
        edit_task(int(task_id))
        main_loop()
    elif db == "4":
        task_id = input("enter the id of the task : ")
        mark_task_as_done(int(task_id))
        main_loop()
    elif db == "0":
        close_the_app()
    print(100 * "_")
try:
    main_loop()
except:
    print("error try \nagain")
    main_loop()