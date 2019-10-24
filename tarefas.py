import sys
import requests
from requests.auth import HTTPBasicAuth
import json



#print ("This is the name of the script: ", sys.argv[0])
#print ("Number of arguments: ", len(sys.argv))
#print ("The arguments are: " , str(sys.argv))
##data = { "title": "Buy groceries","description": "Brelele","done": False}
#r = requests.post('http://127.0.0.1:5000/todo/api/v1.0/tasks',json=json_data,auth=HTTPBasicAuth('lucas', 'python'))
#r = requests.get('http://127.0.0.1:5000/todo/api/v1.0/tasks',auth=HTTPBasicAuth('lucas', 'python'))
#r = requests.delete('http://127.0.0.1:5000/todo/api/v1.0/tasks/4',auth=HTTPBasicAuth('lucas', 'python'))

tarefa=str(sys.argv[1])
function=str(sys.argv[2])
data=None
id=None


print(tarefa)


def adicionar(data):
    json_data = None
    with open(data) as json_file:
        json_data = json.load(json_file)
    r = requests.post('http://127.0.0.1:5000/todo/api/v1.0/tasks',json=json_data,auth=HTTPBasicAuth('lucas','python'))
    print("ADIOCIONEI")

def listar():
    r=requests.get('http://127.0.0.1:5000/todo/api/v1.0/tasks',auth=HTTPBasicAuth('lucas', 'python'))
    print(r.text)

def buscar(id):
    r=requests.get('http://127.0.0.1:5000/todo/api/v1.0/tasks/{}'.format(id),auth=HTTPBasicAuth('lucas','python'))
    print(r.text)

def apagar(id):
    r = requests.delete('http://127.0.0.1:5000/todo/api/v1.0/tasks/{}'.format(id),auth=HTTPBasicAuth('lucas','python'))
    print(r.text)

def atualizar(data,id):
    json_data = None
    with open(data) as json_file:
        json_data = json.load(json_file)
    r = requests.put('http://127.0.0.1:5000/todo/api/v1.0/tasks/{}'.format(id),json=json_data,auth=HTTPBasicAuth('lucas','python'))


if function=="adicionar":
    data=str(sys.argv[3])
    adicionar(data)

elif function=="listar":
    listar()

elif function=="buscar":
     id=str(sys.argv[3])
     print(id)
     buscar(id)

elif function == "apagar":
    id=str(sys.argv[3])
    apagar(id)

elif function == "atualizar":
    id=str(sys.argv[3])
    data=str(sys.argv[4])
    atualizar(data,id)

#locals()[(valor1)]("pokemons")