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


def isempty (lst):

    #comprueba si la lista esta vacia, si lo esta devuelve True, sino devuelve False
    if len(lst) == 0:
        return True
    else:
        return False


def altaProductos(lst_codigos, lst_descripcion, lst_categorias, lst_precios, lst_stock, lst_marcas):

    codigo = input("Ingrese un identificador (-1 para finalizar): ")
    #validar el identificador de los productos que se ingresan por consola
    while codigo != "-1":
        if len(codigo) < 3 or len(codigo) > 10:
            print("La longitud del identificador es invalida, ingrese una longitud valida para el identificador!!")
            codigo = input("Ingrese un identificador, -1 para salir: ")
        
        if codigo == " ":
            print("Ingreso una identificador vacio, no sirve!!!")
            codigo = input("Ingrese un identificador, -1 para salir: ")
        
        seguirValidando = True
        
        while seguirValidando:
            codigoNoValida = False
            codigoValida = False
            for i in range (len(codigo)):
                if codigo[i] == "_"  or (("A"<=codigo[i] <="Z") or ("a"<=codigo[i] <="z")) or ("0"<=codigo[i] <="9"):
                    if codigoNoValida != True:
                        codigoValida = True
                else:
                    codigoNoValida = True
                    codigoValida = False
                
            if codigoNoValida:
                print ("Identificador invalido, vuelva a ingresarlo!!")
                codigo = input("Ingrese un identificador, -1 para salir: ")
                            
            if codigoValida:
                print("Ingreso una codigo valida!")
                seguirValidando = False
                nombre = input("\nNombre del producto: ")
                categoria = input("\nCategoria del producto: ")
                precio = float(input("\nPrecio del producto: "))
                cantidad = random.randint(1, 50)
                marca = input("\nMarca del producto: ")

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
    
        codigo = input("Ingrese una codigo, -1 para salir: ")

    return()
        
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
        'La clave es que el número después de < debe ser mayor que la longitud máxima de los datos '
        'de esa columna. En este caso la descripción necesita al menos unos 35-40 caracteres para que no se pise con Categoría.'

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

    if len(codigo) < 3 or len(codigo) > 10:
            print("La longitud del identificador es invalida, ingrese una longitud valida para el identificador!!")
            codigo = input("Ingrese un identificador, -1 para salir: ")
        
            if codigo == " ":
                print("Ingreso una identificador vacio, no sirve!!!")
                codigo = input("Ingrese un identificador, -1 para salir: ")
        
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

                while nuevo_codigo != "-1":
                    while len(nuevo_codigo) < 4 or len(nuevo_codigo) > 10 or nuevo_codigo == "":
                        nuevo_codigo = input("ERROR. Ingrese un codigo valido: ")

                    aux_validar_codigo = False
                    while aux_validar_codigo == False:
                        for i in nuevo_codigo:
                            alfabeto = ("a" <= i <= "z") or ("A" <= i <= "Z")
                            numeros = "0" <= i <= "9"
                            especiales = i == "_"
                            if not (alfabeto or numeros or especiales):
                                nuevo_codigo = input("ERROR. Ingrese un codigo valido: ")
                            else:
                                aux_validar_codigo = True
                    

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