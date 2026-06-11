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

def existenombre (lst_nombres, nombre):

    #recorre la lista de nombres y si encuentra el nombre ingresado, devuelve True, sino devuelve False
    for i in range(len(lst_nombres)):
        if lst_nombres[i] == nombre:
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




def ordenarProductos(lst_codigos, lst_nombres, lst_stock):
#nos falta el caso de que haya mas de un producto con la misma cantidad de stock, ordenarlos por alfabeticamente por la descripcion del producto
    for i in range(len(lst_stock)-1):
        for j in range(i+1, len(lst_stock)):
            if lst_stock[i] < lst_stock[j]:
                # Intercambiar stock
                lst_stock[i], lst_stock[j] = lst_stock[j], lst_stock[i]
                # Intercambiar codigos
                lst_codigos[i], lst_codigos[j] = lst_codigos[j], lst_codigos[i]
                # Intercambiar nombres
                lst_nombres[i], lst_nombres[j] = lst_nombres[j], lst_nombres[i]
            if lst_stock[i] == lst_stock[j]:
                # si el stock es igual, se ordena por nombre alfabeticamente
                lst_nombres[i] = lst_nombres[i].lower()  # convertimos a minuscula para evitar problemas con mayusculas
                lst_nombres[j] = lst_nombres[j].lower()
                if lst_nombres[i] > lst_nombres[j]:
                    # Intercambiar stock
                    lst_stock[i], lst_stock[j] = lst_stock[j], lst_stock[i]
                    # Intercambiar codigos
                    lst_codigos[i], lst_codigos[j] = lst_codigos[j], lst_codigos[i]
                    # Intercambiar nombres
                    lst_nombres[i], lst_nombres[j] = lst_nombres[j], lst_nombres[i]



def mostrarProductos(lst_codigos, lst_nombres, lst_stock):

    print("\n--- LISTA DE PRODUCTOS ---")

    if len(lst_codigos) == 0:
        print("No hay productos cargados")
    else:
        print("codigo  nombre  stock")
        for i in range(len(lst_codigos)):
            print(
                lst_codigos[i],   lst_nombres[i],   lst_stock[i]
            )



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




def modificarproducto (lst_codigos, lst_stock, lst_nombres, lst_categorias, lst_precios, lst_marcas):

    nombre = input("Ingrese el nombre del producto : ")

    seguir = True

    while seguir:

        #si el nombre existe, se obtiene el indice del producto a modificar
        #luego se muestra un sub menu con las opciones de modificar cada atributo del producto, 
        #y se pide al usuario que seleccione una opcion, si la opcion seleccionada no es valida, se pide nuevamente hasta que sea valida

        if existenombre(lst_nombres, nombre):

            indice = lst_nombres.index(nombre)

            print("1. Modificar descripcion del producto")
            print("2. Modificar precio")
            print("3. Modificar stock")
            print("4. Modificar marca del fabricante")
            print("5. Modificar categoria")
            print("6. Modificar codigo")
            print("8. Salir")

            opcion = int(input("Seleccione una opcion: "))

            while (opcion < 1 or opcion > 6) and opcion != 8:
                print("Opcion no valida")
                opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                nueva_descripcion = input("Ingrese la nueva descripcion: ")
                lst_nombres[indice] = nueva_descripcion
                print("Descripcion modificada correctamente")

            elif opcion == 2:
                nuevo_precio = float(input("Ingrese el nuevo precio: "))
                lst_precios[indice] = nuevo_precio
                print("Precio modificado correctamente")

            elif opcion == 3:
                nueva_cantidad = ingresarPositivo("Ingrese la nueva cantidad: ")
                lst_stock[indice] = nueva_cantidad
                print("Stock modificado correctamente")

            elif opcion == 4:
                nueva_marca = input("Ingrese la nueva marca del fabricante: ")
                lst_marcas[indice] = nueva_marca
                print("Marca del fabricante modificada correctamente")

            elif opcion == 5:
                nueva_categoria = input("Ingrese la nueva categoria: ")
                lst_categorias[indice] = nueva_categoria
                print("Categoria modificada correctamente")
            
            elif opcion == 6:
                nuevo_codigo = int(input("Ingrese el nuevo codigo: "))

                while nuevo_codigo <= 0:
                    print("ERROR. Ingrese un codigo valido: ")
                    nuevo_codigo = int(input("Ingrese el nuevo codigo: "))

                if existecodigo(lst_codigos, nuevo_codigo):
                    print("El codigo ya existe")
                else:
                    lst_codigos[indice] = nuevo_codigo
                    print("Codigo modificado correctamente")


        else:
            print("Producto no encontrado")

        seguir = input("Desea modificar otro producto? (s/n): ")
        if seguir != "s" and seguir != "S" and seguir != "si" and seguir != "SI" and seguir != "Si" and seguir != "sI":
            seguir = False

        else:
            nombre = input("Ingrese el nombre del producto : ")
