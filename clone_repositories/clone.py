import re
import os

# Abre el archivo con la lista de repositorios
with open("gits.txt", "r") as file:
    repositorios = file.readlines()

#Nombre del directorio segun el numero de tarea.
nombre_directorio = "Tarea1"

# Intenta crear el directorio (o acceder a uno ya existente) y cambia al directorio creado/existente
try:
    os.mkdir(nombre_directorio)
except FileExistsError:
    print(f"El directorio {nombre_directorio} ya existe. Se usará este directorio.")
os.chdir(nombre_directorio)

for repo in repositorios:
    s = repo
    #De lo que esta entre git@github.com: y / copiemelo como una variable
    result = re.search("git clone git@github.com:(.*)/", s)
    repo_url = repo.strip()
    username = result.group(1)
    #print(repo_url + ' ' + username)
    os.system(repo_url + ' ' + username)

#Linea que se ejecuta en la terminal
#os.system("git clone git@github.com:GabrielBO4/i2023-ie0217.git")
