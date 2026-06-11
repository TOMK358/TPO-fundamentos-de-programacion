#aca creamos funciones
import random

#MENU USADO PARA MOSTRAR LAS OPCIONES DISPONIBLES AL USUARIO
def mostrarMenu():
    print("\n--- MENU ---")
    print("1. Alta de productos")
    print("2. Modificar Producto")
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

def existeproducto (lst_descripcion, descripcion):

    #recorre la lista de descripciones y si encuentra la descripcion ingresada, devuelve True, sino devuelve False
    for i in range(len(lst_descripcion)):
        if lst_descripcion[i] == descripcion:
            return True

    return False

def altaProductos(lst_codigos, lst_descripcion, lst_categorias, lst_precios, lst_stock, lst_marcas):

    codigo = input("Ingrese un codigo (-1 para finalizar): ")

    #comprueba que el codigo ingresado sea positivo o -1 para finalizar, si no lo es, pide nuevamente el codigo
    while "-" in codigo and codigo != "-1":
        codigo = input("ERROR. Ingrese un codigo valido: ")

    while codigo != "-1":

        nombre = input("Nombre del producto: ")
        print("\n")
        categoria = input("Categoria del producto: ")
        print("\n")
        precio = float(input("Precio del producto: "))
        print("\n")
        cantidad = random.randint(1, 50)
        print("\n")
        marca = input("Marca del producto: ")

        #si el codigo ya existe, se muestra un mensaje de error, sino se agrega el producto a las listas correspondientes
        if existecodigo(lst_codigos, codigo):
            print("El codigo ya existe")
        else:
            lst_codigos.append(codigo)
            lst_descripcion.append(nombre)
            lst_categorias.append(categoria)
            lst_precios.append(precio)
            lst_stock.append(cantidad)
            lst_marcas.append(marca)

            print("Producto agregado correctamente")

        #se pide el codigo nuevamente para seguir agregando productos, o finalizar el proceso ingresando -1
        codigo = input("Ingrese un codigo (-1 para finalizar): ")

        #realiza la misma comprobacion que al inicio para asegurarse de que el codigo ingresado sea positivo o -1 para finalizar, si no lo es, pide nuevamente el codigo
        while "-" in codigo and codigo != "-1":
            codigo = input("ERROR. Ingrese un codigo valido: ")

def ordenarProductos(lst_codigos, lst_descripcion, lst_categorias, lst_precios, lst_stock, lst_marcas):
#nos falta el caso de que haya mas de un producto con la misma cantidad de stock, ordenarlos por alfabeticamente por la descripcion del producto
    for i in range(len(lst_stock)-1):
        for j in range(i+1, len(lst_stock)):
            if lst_stock[i] < lst_stock[j]:
                # Intercambiar stock
                lst_stock[i], lst_stock[j] = lst_stock[j], lst_stock[i]
                # Intercambiar codigos
                lst_codigos[i], lst_codigos[j] = lst_codigos[j], lst_codigos[i]
                # Intercambiar descripciones
                lst_descripcion[i], lst_descripcion[j] = lst_descripcion[j], lst_descripcion[i]
                # Intercambiar categorias
                lst_categorias[i], lst_categorias[j] = lst_categorias[j], lst_categorias[i]
                # Intercambiar precios
                lst_precios[i], lst_precios[j] = lst_precios[j], lst_precios[i]
                # Intercambiar marcas
                lst_marcas[i], lst_marcas[j] = lst_marcas[j], lst_marcas[i]

            if lst_stock[i] == lst_stock[j]:
                # si el stock es igual, se ordena por nombre alfabeticamente
                aux1_descripcion = lst_descripcion[i].lower()  # convertimos a minuscula para evitar problemas con mayusculas
                aux2_descripcion = lst_descripcion[j].lower()  
                if aux1_descripcion > aux2_descripcion:
                    # Intercambiar stock
                    lst_stock[i], lst_stock[j] = lst_stock[j], lst_stock[i]
                    # Intercambiar codigos
                    lst_codigos[i], lst_codigos[j] = lst_codigos[j], lst_codigos[i]
                    # Intercambiar descripciones
                    lst_descripcion[i], lst_descripcion[j] = lst_descripcion[j], lst_descripcion[i]
                    # Intercambiar categorias
                    lst_categorias[i], lst_categorias[j] = lst_categorias[j], lst_categorias[i]
                    # Intercambiar precios
                    lst_precios[i], lst_precios[j] = lst_precios[j], lst_precios[i]
                    # Intercambiar marcas
                    lst_marcas[i], lst_marcas[j] = lst_marcas[j], lst_marcas[i]

def mostrarProductos(lst_codigos, lst_descripcion, lst_categorias, lst_precios, lst_stock, lst_marcas):

    print("\n--- LISTA DE PRODUCTOS ---")

    if len(lst_codigos) == 0:
        print("No hay productos cargados")
    else:

        print(f"{'Codigo':<10}{'Descripcion':<40}{'Categoria':<20}{'Precio':<10}{'Stock':<10}{'Marca':<20}")

        for i in range(len(lst_codigos)):
            print(
                f"{lst_codigos[i]:<10}"
                f"{lst_descripcion[i]:<40}"
                f"{lst_categorias[i]:<20}"
                f"{lst_precios[i]:<10}"
                f"{lst_stock[i]:<10}"
                f"{lst_marcas[i]:<20}"
            )

def eliminarProducto(lst_codigos, lst_descripcion, lst_categorias, lst_precios, lst_stock, lst_marcas):

    codigo = input("Ingrese el codigo del producto (-1 para finalizar): ")

    #comprueba que el codigo ingresado sea positivo o -1 para finalizar, si no lo es, pide nuevamente el codigo
    while "-" in codigo and codigo != "-1":
        codigo = input("ERROR. Ingrese un codigo valido: ")

    #mientras el codigo sea diferente de -1, se va 
    while codigo != "-1":

        #si el codigo existe, se obtiene el indice del producto a eliminar, y se eliminan tanto el codigo, el stock y nombre de las listas correspondientes
        if existecodigo(lst_codigos, codigo):

            indice = -1

            for i in range(len(lst_codigos)):
                if lst_codigos[i] == codigo:
                    indice = i

            lst_codigos.pop(indice)
            lst_stock.pop(indice)
            lst_descripcion.pop(indice)
            lst_categorias.pop(indice)
            lst_precios.pop(indice)
            lst_marcas.pop(indice)

            print("Producto eliminado correctamente")

        else:
            print("Producto no encontrado")

        #se pide el codigo nuevamente para seguir eliminando productos, o finalizar el proceso ingresando -1
        codigo = input("Ingrese el codigo del producto (-1 para finalizar): ")
        while "-" in codigo and codigo != "-1":
            codigo = input("ERROR. Ingrese un codigo valido: ")


def modificarproducto (lst_codigos,lst_descripcion, lst_categorias, lst_stock, lst_precios, lst_marcas):

    descripcion = input("Ingrese la descripcion del producto : ")

    seguir = True

    while seguir:

        #si el nombre existe, se obtiene el indice del producto a modificar
        #luego se muestra un sub menu con las opciones de modificar cada atributo del producto, 
        #y se pide al usuario que seleccione una opcion, si la opcion seleccionada no es valida, se pide nuevamente hasta que sea valida

        if existeproducto(lst_descripcion, descripcion):

            indice = lst_descripcion.index(descripcion)

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
                lst_descripcion[indice] = nueva_descripcion
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
                nuevo_codigo = input("Ingrese el nuevo codigo: ")

                while "-" in nuevo_codigo and nuevo_codigo != "-1":
                    print("ERROR. Ingrese un codigo valido: ")
                    nuevo_codigo = input("Ingrese el nuevo codigo: ")

                    

                if existecodigo(lst_codigos, nuevo_codigo):
                    print("El codigo ya existe")
                else:
                    lst_codigos[indice] = nuevo_codigo
                    print("Codigo modificado correctamente")


        else:
            print("Producto no encontrado")

        continuar = input("Desea modificar otro producto? (s/n): ")
        continuar = continuar.lower()
        if continuar != "s" and continuar != "si":
            seguir = False

        else:
            descripcion = input("Ingrese la descripcion del producto : ")

    return lst_codigos, lst_descripcion, lst_categorias, lst_stock, lst_precios, lst_marcas
