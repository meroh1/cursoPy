def menu():
    print("--------------------------------")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Modificar contacto")
    print("6. Salir")
    print("--------------------------------")
    opcion = input("Seleccione una opcion: ")
    return opcion

def agregarContacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ").strip().lower() #porque strip aqui, y no en los otras funcioens?
    telefono = input("Ingrese el telefono del contacto: ").strip()
    email = input("Ingrese el email del contacto: ").strip()
    agenda.append({"nombre": nombre, "telefono": telefono, "email": email})
    print("Contacto agregado correctamente")

def verContactos(agenda):
    for contacto in agenda:
        print(f"Nombre: {contacto['nombre']}, Telefono: {contacto['telefono']}, Email: {contacto['email']}")

def buscarContacto(agenda):
    nombre = input("Ingrese el nombre del contacto a buscar: ").strip().lower()
    for contacto in agenda:
        if contacto['nombre'] == nombre:
            print(f"Nombre: {contacto['nombre']},\nTelefono: {contacto['telefono']},\nEmail: {contacto['email']}")
            break

def eliminarContacto(agenda):
    nombre = input("Ingrese el nombre del contacto a eliminar: ").strip().lower()
    for contacto in agenda:
        if contacto['nombre'] == nombre:
            agenda.remove(contacto)
            print("Contacto eliminado correctamente")
            break

def modificarNombre(agenda):
    nombre = input("Ingrese el nombre del contacto a modificar: ").strip().lower()
    for contacto in agenda:
        if contacto['nombre'] == nombre:
            newName = input("Ingrese el nuevo nombre del contacto: ").strip().lower()
            contacto['nombre'] = newName
            print("Nombre modificado correctamente")
            break
        else:
            print("Contacto no encontrado")

def agendaContactos():
    agenda = []
    while True:
        opcion = int(menu())
        if opcion is not int:
            if opcion == 1:
                agregarContacto(agenda) # 
            elif opcion == 2:
                verContactos(agenda)
            elif opcion == 3:
                buscarContacto(agenda)
            elif opcion == 4:
                eliminarContacto(agenda)
            elif opcion == 5:
                modificarNombre(agenda)
            elif opcion == 6:
                break
        else:
            print(f"Opcion seleccionada: {opcion}")
            print("Opcion no valida")
            continue
            

agendaContactos()