import funciones as func

trabajadores = []

while True:
    opcion = func.menu()
    if opcion == "1":
        # Nombre y Apellido, Cargo, Sueldo bruto
        func.registro(trabajadores)
    elif opcion == "2":
        print("--------------------------------------------")
        func.listar(trabajadores)
        print("--------------------------------------------")
    elif opcion == "3":
        print("--------------------------------------------")
        cargo = input("1.-Imprimir todos\n2.-Seleccionar e imprimir\nIngresa una opcion: ")
        func.imprimir(cargo)
        print("--------------------------------------------")
    elif opcion == "4":
        break
    else:
        print("Ingresa una opcion valida")