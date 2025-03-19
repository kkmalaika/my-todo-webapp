FILEPATH = "Ma_Todo_Quotidienne.txt"

def get_todos(filepath = FILEPATH):

    with open(filepath, 'r', encoding="ISO-8859-1") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):

    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

# print(__name__)

if __name__ == "__main__" :
    print ("Hello from functions")
    print(get_todos())