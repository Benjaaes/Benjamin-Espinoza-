import random
import csv

def cod_cunsumo():
    id = random.randint(100, 100000)
    return random.randint(100,100000)
def registrar (lista):
    viernes = 0
    sabado = 0 
    domingo = 0
    id_consumidor = cod_cunsumo
    print("<<<Datos del Jugador>>>")

    nombre = input("nombre: ")

    while True:
        edad = int(input("Ingresar edad: "))
        if edad > 0:
            break
        else:
            print("***Edad tiene que ser mayor a 0***")
            continue
    equipo = input("Ingresar equipo: ")
    while True :   
        cafe_viernes = int(input("Consumo de cafe dia Viernes: "))
        cafe_viernes+=viernes
        cafe_sabado = int(input("Consumo de cafe dia Sabado: "))
        cafe_sabado+=sabado
        cafe_domingo = int(input("Consumo de café dia Domingo: "))
        cafe_domingo+=domingo
        resultado = viernes + sabado + domingo
        if  resultado >= 3:
            print(f"Consumo total de cafés {resultado}")
            continue
        else: 
            print("El minimo de consumo es de 3 cafés")
            break
    lista.append([id_consumidor,nombre,edad,equipo,viernes,sabado,domingo]) 
def listar (lista):
    input("ID CONSUMO\tJUGADOR\tEDAD\tEQUIPO\tVIERNES\tSABADO\tDOMINGO")
    for jugador in lista:
        print(f"{jugador[0]}\t{jugador[1]}\t{jugador[2]}\t{jugador[3]}\t{jugador[4]}")

def imprimir(lista, cod_consumo):
    with open("hoja.csv", "w", newline="") as hoja_cafes:
        hoja_cafes = ("ID CONSUMO\tJUGADOR\tEDAD\tEQUIPO\tVIERNES\tSABADO\tDOMINGO")