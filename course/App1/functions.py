FILEPATH = "C:/Users/Kelly/PycharmProjects/PythonProject/course/App1/Ma_Todo_Quotidienne.txt"
def get_todos(filepath = FILEPATH):
    """ouvrir ma todo
     montrer la liste"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH):
    """Ecrire dans ma liste todo et
    dans le fichier txt """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

# print(__name__)

if __name__ == "__main__" :
    print ("Hello from functions")
    print(get_todos())