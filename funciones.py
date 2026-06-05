#aca creamos funciones
import random

def mostrarMenu():
    print("\n--- MENU ---")
    print("1. Alta de productos")
    print("2. Modificar stock")
    print("3. Buscar producto")
    print("4. Mostrar productos")
    print("8. Salir")


def ingresar_opcionMenu():
    op = int(input("Seleccione una opcion: "))

    while (op < 1 or op > 5) and op != 8:
        print("La opcion seleccionada no es valida")
        op = int(input("Seleccione una opcion: "))

    return op


def ingresarPositivo(msg):
    num = int(input(msg))

    while num <= 0:
        print("Error, debe ser positivo")
        num = int(input(msg))

    return num


def existecodigo(lst_codigos, codigo):

    for i in range(len(lst_codigos)):
        if lst_codigos[i] == codigo:
            return True

    return False


def altaProductos(lst_codigos, lst_nombres, lst_stock):

    codigo = int(input("Ingrese un codigo (-1 para finalizar): "))

    while codigo <= 0 and codigo != -1:
        codigo = int(input("ERROR. Ingrese un codigo valido: "))

    while codigo != -1:

        nombre = input("Nombre del producto: ")

        cantidad = random.randint(1, 50)

        if existecodigo(lst_codigos, codigo):
            print("El codigo ya existe")
        else:
            lst_codigos.append(codigo)
            lst_nombres.append(nombre)
            lst_stock.append(cantidad)

            print("Producto agregado correctamente")

        codigo = int(input("Ingrese un codigo (-1 para finalizar): "))

        while codigo <= 0 and codigo != -1:
            codigo = int(input("ERROR. Ingrese un codigo valido: "))


def mostrarProductos(lst_codigos, lst_nombres, lst_stock):

    print("\n--- LISTA DE PRODUCTOS ---")

    if len(lst_codigos) == 0:
        print("No hay productos cargados")
    else:
        print("codigo | nombre | stock")
        for i in range(len(lst_codigos)):
            print(
                lst_codigos[i],   lst_nombres[i],   lst_stock[i]
            )


def buscarProducto(lst_codigos, lst_stock):

    codigo = int(input("Ingrese el codigo a buscar (-1 para finalizar): "))

    while codigo != -1:

        if existecodigo(lst_codigos, codigo):

            indice = lst_codigos.index(codigo)

            print("Stock disponible:", lst_stock[indice])

            if lst_stock[indice] < 5:
                print("Stock por debajo del minimo")

        else:
            print("Producto no encontrado")

        codigo = int(input("Ingrese el codigo a buscar (-1 para finalizar): "))




def modificarStock(lst_codigos, lst_stock):

    codigo = int(input("Ingrese el codigo del producto (-1 para finalizar): "))

    while codigo != -1:

        if existecodigo(lst_codigos, codigo):

            indice = lst_codigos.index(codigo)

            nueva_cantidad = ingresarPositivo("Ingrese la nueva cantidad: ")

            lst_stock[indice] = nueva_cantidad

            print("Stock modificado correctamente")

        else:
            print("Producto no encontrado")

        codigo = int(input("Ingrese el codigo del producto (-1 para finalizar): ")) 