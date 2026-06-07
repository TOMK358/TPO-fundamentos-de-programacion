#aca creamos funciones
import random

#MENU USADO PARA MOSTRAR LAS OPCIONES DISPONIBLES AL USUARIO
def mostrarMenu():
    print("\n--- MENU ---")
    print("1. Alta de productos")
    print("2. Modificar stock")
    print("3. Eliminar producto")
    print("4. Mostrar productos")
    print("8. Salir")

#pedimos al usuario que ingrese una opcion para manejar el menu, y comprobamos que la opcion ingresada sea valida (entre 1 y 5, o 8 para salir), si no lo es, 
# se pide nuevamente la opcion hasta que sea valida
def ingresar_opcionMenu():
    op = int(input("Seleccione una opcion: "))

    while (op < 1 or op > 5) and op != 8:
        print("La opcion seleccionada no es valida")
        op = int(input("Seleccione una opcion: "))

    return op

#comprueba que el numero ingresado sea positivo, si no lo es, pide nuevamente el numero hasta que sea positivo
def ingresarPositivo(msg):
    num = int(input(msg))

    while num <= 0:
        print("Error, debe ser positivo")
        num = int(input(msg))

    return num


def existecodigo(lst_codigos, codigo):

    #recorre la lista de codigos y si encuentra el codigo ingresado, devuelve True, sino devuelve False
    for i in range(len(lst_codigos)):
        if lst_codigos[i] == codigo:
            return True

    return False


def altaProductos(lst_codigos, lst_nombres, lst_stock):

    codigo = int(input("Ingrese un codigo (-1 para finalizar): "))

    #comprueba que el codigo ingresado sea positivo o -1 para finalizar, si no lo es, pide nuevamente el codigo
    while codigo <= 0 and codigo != -1:
        codigo = int(input("ERROR. Ingrese un codigo valido: "))

    while codigo != -1:

        nombre = input("Nombre del producto: ")

        cantidad = random.randint(1, 50)

        #si el codigo ya existe, se muestra un mensaje de error, sino se agrega el producto a las listas correspondientes
        if existecodigo(lst_codigos, codigo):
            print("El codigo ya existe")
        else:
            lst_codigos.append(codigo)
            lst_nombres.append(nombre)
            lst_stock.append(cantidad)

            print("Producto agregado correctamente")

        #se pide el codigo nuevamente para seguir agregando productos, o finalizar el proceso ingresando -1
        codigo = int(input("Ingrese un codigo (-1 para finalizar): "))

        #realiza la misma comprobacion que al inicio para asegurarse de que el codigo ingresado sea positivo o -1 para finalizar, si no lo es, pide nuevamente el codigo
        while codigo <= 0 and codigo != -1:
            codigo = int(input("ERROR. Ingrese un codigo valido: "))


def mostrarProductos(lst_codigos, lst_nombres, lst_stock):

    print("\n--- LISTA DE PRODUCTOS ---")

    if len(lst_codigos) == 0:
        print("No hay productos cargados")
    else:
        
        #se tiene que haccer las 3 juntas por los parametros que recibe la funcion, ya que ordena las 3 de una sola vez,
        # y si se ordena solo una, las otras quedan desordenadas y no se pueden mostrar correctamente
        lst_codigos, lst_nombres, lst_stock = ordenarProductos_porstock(lst_codigos, lst_nombres, lst_stock)
        print("codigo  nombre  stock")
        for i in range(len(lst_codigos)):
            print(
                lst_codigos[i],   lst_nombres[i],   lst_stock[i]
            )


#todavia no se usa pero se usara despues (con algunos cambios segun el uso que le demos)
def buscarProducto(lst_codigos, lst_stock):

    codigo = int(input("Ingrese el codigo a buscar (-1 para finalizar): "))

    while codigo != -1:

        if existecodigo(lst_codigos, codigo):

            indice = lst_codigos.index(codigo)

            print("Stock disponible:", lst_stock[indice])

        else:
            print("Producto no encontrado")

        codigo = int(input("Ingrese el codigo a buscar (-1 para finalizar): "))




def modificarStock(lst_codigos, lst_stock):

    codigo = int(input("Ingrese el codigo del producto (-1 para finalizar): "))

    while codigo != -1:

        #si el codigo existe, se obtiene el indice del producto a modificar, se pide la nueva cantidad y se actualiza el stock en la lista correspondiente
        if existecodigo(lst_codigos, codigo):

            indice = lst_codigos.index(codigo)

            nueva_cantidad = ingresarPositivo("Ingrese la nueva cantidad: ")

            lst_stock[indice] = nueva_cantidad

            print("Stock modificado correctamente")

        else:
            print("Producto no encontrado")

        
        #se pide el codigo nuevamente para seguir modificando productos, o finalizar el proceso ingresando -1
        codigo = int(input("Ingrese el codigo del producto (-1 para finalizar): ")) 



def eliminarProducto(lst_codigos, lst_stock, lst_nombres):

    codigo = int(input("Ingrese el codigo del producto (-1 para finalizar): "))

    #comprueba que el codigo ingresado sea positivo o -1 para finalizar, si no lo es, pide nuevamente el codigo
    while codigo <= 0 and codigo != -1:
        codigo = int(input("ERROR. Ingrese un codigo valido: "))

    #mientras el codigo sea diferente de -1, se va 
    while codigo != -1:

        #si el codigo existe, se obtiene el indice del producto a eliminar, y se eliminan tanto el codigo, el stock y nombre de las listas correspondientes
        if existecodigo(lst_codigos, codigo):

            indice = -1

            for i in range(len(lst_codigos)):
                if lst_codigos[i] == codigo:
                    indice = i

            lst_codigos.pop(indice)
            lst_stock.pop(indice)
            lst_nombres.pop(indice)

            print("Producto eliminado correctamente")

        else:
            print("Producto no encontrado")

        #se pide el codigo nuevamente para seguir eliminando productos, o finalizar el proceso ingresando -1
        codigo = int(input("Ingrese el codigo del producto (-1 para finalizar): "))


def ordenarProductos_porstock(lst_codigos, lst_nombres, lst_stock):
    for i in range(len(lst_stock)-1):
        for j in range(i+1, len(lst_stock)):
            if lst_stock[i] < lst_stock[j]:
                # Intercambiar stock
                lst_stock[i], lst_stock[j] = lst_stock[j], lst_stock[i]
                # Intercambiar codigos
                lst_codigos[i], lst_codigos[j] = lst_codigos[j], lst_codigos[i]
                # Intercambiar nombres
                lst_nombres[i], lst_nombres[j] = lst_nombres[j], lst_nombres[i]

