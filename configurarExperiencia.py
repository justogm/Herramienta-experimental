from platform import system
import os
import json

print("Inserte links a proyectos de figma:")
links = {}

i = 0
while True:
    entrada = input("\t|__ ")

    if entrada.lower() == 'q':
        break

    i += 1
    links[f"LINK_{i}"] = entrada

if len(links) > 1:
    salida = open("links.py", "w")
    sistema = system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    print("Se evaluarán:")
    for i in links.keys():
        print("\t|__", links[i])

    with open("links.json", "w") as archi:
        json.dump(links, archi)