# Registro de estudiantes y sus notas (Diccionario)
estudiantes = {}
print ("-"*20,"Bienvenido","-"*20)

while True:
    print("\n1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")

    opcion = input("Elige una opción: ")

#registro de estudiantes (agregar datos)
    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        nota = input("Nota del estudiante: ")
        estudiantes[nombre] = nota

#mostrar información
    elif opcion == "2":
        print("\nLista de estudiantes:")
        for nombre, nota in estudiantes.items():
            print(nombre, ":", nota)
            
#buscar datos
    elif opcion == "3":
        buscar = input("Nombre a buscar: ")
        if buscar in estudiantes:
            print("Nota:", estudiantes[buscar])
        else:
            print("No encontrado")
#eliminar datos
    elif opcion == "4":
        eliminar = input("Nombre a eliminar: ")
        if eliminar in estudiantes:
            del estudiantes[eliminar]
            print("Eliminado")
        else:
            print("No existe")

    elif opcion == "5":
        print ("\n","-"*10,"GRACIAS","-"*10)
        break

    else:
        print("Opción inválida")