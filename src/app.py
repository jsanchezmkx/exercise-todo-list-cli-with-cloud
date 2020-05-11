import json, requests
todos = []
usuario = "chemisanchez"
url = "https://assets.breatheco.de/apis/fake/todos/user/"

def get_todos():
    global todos
    return todos

def add_one_task(title):
    # your code here
    data= {'label': title,
     'done': False
    }
    todos.append(data)

def print_list():
    print("Lista de tareas:")
    y=1
    for x in todos:
        print(y , x)
        y=y+1
    

def delete_task(number_to_delete):
    number_to_delete=int(number_to_delete)-1
    return get_todos().pop(number_to_delete)

def initialize_todos():
    global todos
    header = {'Content-Type':'application/json'}
    r = requests.get(url+usuario, headers=header) 
    if(r.status_code == 404):
        print("No previous todos found, starting a new todolist")
        r = requests.post(url = url+usuario,  headers=header, data=json.dumps(todos)) 
        if r.status_code == 200:
            print("Tasks initialized successfully")
    else:
        print("A todo list was found, loading the todos...")
        todos = r.json()
    print(todos)

    
def save_todos():
    # your code here
    #header={'Content-Type':'application/json'}
 #   url1="https://assets.breatheco.de/apis/fake/todos"
    header = {'Content-Type':'application/json'}
    req = requests.put(url + usuario, headers=header, data=json.dumps(todos))
    print (req.text)

def load_todos():
    header = {'Content-Type':'application/json'}
    req = requests.get(url + usuario, headers=header)
    todos = req.json()
    print(todos)
    
# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    stop = False
    print("Initializing todos with previous data or creating a new todo's list...")
    initialize_todos()
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Send/Save todo's to API
        5. Retrieve todo's from API
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")