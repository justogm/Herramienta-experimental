from platform import system
import os
import json

# Se registra la posición de inicio
print("-"*20) 
pos = input("Seleccione posición de inicio:\n|_ 1. Norte\n|_ 2. Sur\n|_ 3. Oeste\n|_ 4. Este\n|_ 5. Centro\n|_ ")
pos = int(pos)
while 1 > int(pos) or int(pos) > 5:
    pos = input("Seleccione una opción válida: ")

posInicial = {
    "x":None,
    "y":None
}

switch = {
    "1":["x/2","0"],
    "2":["x/2","y"],
    "3":["0","y/2"],
    "4":["x", "y/2"],
    "5":["x/2", "y/2"]
}

posInicial["x"], posInicial["y"] = switch[str(pos)][0], switch[str(pos)][1]

print("-"*20) 

animacion = input("Desea generar animaciones? [s/n]: ")
while not animacion.lower() in ["s", "n"]:
    animacion = input("Ingrese una opción valida [s/n]: ")

print("-"*20)
print("Inserte links a proyectos de figma:")
links = {}

i = 0
while True:
    entrada = input("\t|__ ")

    if entrada.lower() == 'q':
        break

    i += 1
    links[f"LINK_{i}"] = entrada

if len(links) >= 1:
    salida = open("links.py", "w")
    sistema = system()
    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    print("Se evaluarán:")

    for i in links.keys():
        print("\t|__", links[i])

    with open("config.json", "w") as archi:
        config = {
            "posInicial" : posInicial,
            "links" : links,
            "decisionAnimacion" : animacion
        }
        json.dump(config, archi, indent=4)