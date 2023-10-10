from platform import system
import os

print("Inserte links a proyectos de figma:")
links = []
while True:
    entrada = input("\t|__ ")

    if entrada.lower() == 'q':
        break

    links.append(entrada)

sistema = system()

if sistema == "Windows":
    os.system("cls")
else:
    os.system("clear")

print("Se evaluarán:")
for i in links:
    print("\t|__", i)