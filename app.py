import funciones
lista = []
while True:

    print("""
*******************************
1.Registrar consumo.
2.Listar todos los consumos.
3.Imprimir hoja consumo.
4.Buscar un consumo por ID.
5.Salir del programa.
*******************************
       """)
    opc = int(input("Eliga una opción: "))

    if opc == 1:
        print("")  
        funciones.registrar(lista)
    elif opc == 2:
        print("")
        funciones.listar(lista)
    elif opc  == 3:
        print("")
        funciones.imprimir(lista,)
    elif opc == 4:
        print("")
    elif opc == 5:
        break
    else:
        print(">>>CERRANDO PROGRAMA...<<<")

