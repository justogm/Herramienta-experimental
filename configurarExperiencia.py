from platform import system
import os
import json


pantalla = {}
print("Inserte dimensiones de pantalla:")
pantalla["ancho"] = input("\t|__ Ancho: ")
pantalla["alto"] = input("\t|__ Alto: ")

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
            "dimensionesPantalla" : pantalla,
            "links" : links,
            "decisionAnimacion" : animacion
        }
        json.dump(config, archi, indent=4)