#Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:

def crearCliente():
    global lista_clientes
    cliente['NIF'] = input('NIF:')
    cliente['Nombre'] = input("Nombre: ")
    cliente['Apellidos'] = input("Apellidos: ")
    cliente['Telefono'] = input("Telefono: ")
    cliente['Email'] = input("Email: ")
    cliente['Preferente'] = input('¿Es un cliente preferente? (Si / No)')
    
    lista_clientes.append(cliente)

def mostrarClientes():
    global lista_clientes
    for i, cliente in enumerate(lista_clientes):
        print(f"{i} - {cliente['Nombre']} {cliente['Apellidos']}")

def mostrarClienteNIF():
    global lista_clientes
    nif = input('¿NIF?')
    for i, cliente in enumerate(lista_clientes):
        if(nif == cliente['NIF']):
            print(f"{nif} - {cliente['Nombre']} {cliente['Apellidos']}")
            return
    print('No existe ningún cliente con este NIF')

def eliminarClienteNIF():
    global lista_clientes
    nif = input('¿NIF?')
    for i, cliente in enumerate(lista_clientes):
        if(nif == cliente['NIF']):
            lista_clientes.remove(cliente)
            return
    print('No existe ningún cliente con este NIF')

def mensajeCierre():
    print("Cerrando...")

def switch(opcion):
    switcher = {
        #invocar métodos
        1 : crearCliente,
        2 : mostrarClientes, 
        3 : mostrarClienteNIF,
        4 : eliminarClienteNIF, 
        0 : mensajeCierre,
    }

    func = switcher.get(opcion, "¡Opción no valida!")
    func() # Ejecutamos la función asignada a la propiedad escogida

opciones = """
Opcion 1 : Añadir un cliente
Opcion 2 : Mostrar Todos los Clientes
Opcion 3 : Mostrar Cliente por NIF
Opcion 4 : Eliminar Cliente por NIF
Opcion 0 : Salir 
"""


opcion = ""

while(opcion!=0):
      print(opciones)
      try:
        opcion = int(input("Bienvenido a tu cartera de clientes. Escoge una opción: "))
        print(f'Escogida {opcion}')
        switch(opcion)
      except:
        print("Opcion no valida")