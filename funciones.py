import random
import config
import csv

def menu():
    num_opcion = 1
    for opc in config.opciones_menu:
        print(f"{num_opcion}. {opc}")
        num_opcion += 1
        while True:
            try:
                seleccion = int(input("Opcion: "))
                break
            except:
                print("El valor debe ser numerico")
        return seleccion

def registro(lista):
    codigo = generar_codigo()
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cargo = input("Cargo: ")
    sueldo = int(input("Sueldo bruto: "))

    trabajador = {
        "nombre": nombre,
        "apellido": apellido,
        "cargo": cargo,
        "sueldo": sueldo,
        "codigo": codigo

    }
    
    lista.append(trabajador)
            
def listar(listado):
    print("Codigo\tNombre\tApellido\tCargo\tSueldo")
    for i in listado:
        print(f"{i["codigo"]} {i["nombre"]} {i["apellido"]} {i["cargo"]}{i["sueldo"]}")

def imprimir(lista, cargo):
    try:
        with open("dato.csv", "w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow({"Codigo", "Nombre", "Apellido", "Cargo", "Sueldo Bruto"})
            if cargo == "Todos":
                escritor.writerow(lista)
            else:
                for trabajador in lista:
                    if trabajador[3] == cargo:
                        escritor.writerow(trabajador)
        print("Planilla creada con exito")
    except:
        print("Ah ocurrido un error")

def generar_codigo():
    return random.randint(1000, 9999)

    