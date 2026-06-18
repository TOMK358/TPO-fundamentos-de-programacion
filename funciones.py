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
    op = input("Seleccione una opcion: ")

    while (op < "1" or op > "4") and op != "8":
        print("La opcion seleccionada no es valida")
        op = input("Seleccione una opcion: ")

    return op

#comprueba que el numero ingresado sea positivo, si no lo es, pide nuevamente el numero hasta que sea positivo
def ingresarPositivo(msg):
    num = int(input(msg))

    while num <= 0:
        print("Error, debe ser positivo")
        num = int(input(msg))

    return num

def existeProducto(lst_identificador, identificador):
    '''Funcion para revisar existencia del identificador en la lista.'''
    #recorre la lista de identificadoers y si encuentra el identificador ingresado, devuelve True, sino devuelve False
    for i in range(len(lst_identificador)):
        if lst_identificador[i] == identificador:
            print("El producto existe!")
            return True
        else:
            print("El producto no existe!")

    return False

def validacionIdentificador(identificador):
    '''Funcion hecha para validar el ingreso de los identificadores de los productos.\nParametro de ingreso: identificador del producto
    \nProceso: se valida que el identificador ingresado no sea vacio, la longitud del mismo (entre 4 y 10 caracteres), y tenga caracteres alfanumericos o que posea unicamente como caracter especial "_"
    \nParametro de salida: Si el identificador es valido o no\nAutor: Sergio Nicolas Carraud Fava'''
    #inicializacion de variables
    IdentPorValidar = True
    #validar el identificador de los productos que se ingresan por consola
    while IdentPorValidar:  
        #Validamos que no este vacio.      
        if identificador == " ":
            print("Ingreso una identificador vacio, no sirve!!!")
            identificador = input("Ingrese un identificador, -1 para salir: ")
        #Validamos la longitud del identificador ingresado
        if len(identificador) < 4 or len(identificador) > 10:
            print("La longitud del identificador es invalida, ingrese una longitud valida para el identificador!!")
            identificador = input("Ingrese un identificador, -1 para salir: ")
        else:
            seguirValidando = True
            #Validamos los caracteres que se ingresan
            while seguirValidando:
                identificadorNoValida = False
                identificadorValida = False
                for i in range (len(identificador)):
                    if identificador[i] == "_"  or (("A"<=identificador[i] <="Z") or ("a"<=identificador[i] <="z")) or ("0"<=identificador[i] <="9"):
                        if identificadorNoValida != True:
                            identificadorValida = True
                    else:
                        identificadorNoValida = True
                        identificadorValida = False
                #Para identificadores no validos
                if identificadorNoValida:
                    print ("Identificador invalido, vuelva a ingresarlo!!")
                    identificador = input("Ingrese un identificador, -1 para salir: ")
                #Para identificadores validos            
                if identificadorValida:
                    print("Ingreso una identificador valido!")
                    seguirValidando = False
                    IdentPorValidar = False
                #Condicion de salida
                if identificador == "-1":
                    IdentPorValidar = False

    return(identificador,identificadorValida)

def validacionDescripcion(descripcion):
    '''Funcion para validar la descripcion del producto ingresado. No debe ser vacio y debe iniciar con una letra 
    \nEntrada de la función: Descripción del producto \nProceso de la funcion: Validacion de que la descripción no este vacia y su primer caracter sea una letra, sino se vuelve a solicitar hasta que sea valida 
    \nSalida de la función: Descripcion valida del producto \nAutor: Sergio Nicolas Carraud Fava'''
    Descrip_X_validar = True#Variable que nos servira para iterar hasta que nos devuelva una descripcion valida
    while Descrip_X_validar:
        if descripcion == "":
            descripcion= " "
            print("La Descripción que ingreso no es valida, recuerde que debe ingresar una descripción para el producto.")
        else:
            if (("A"<=descripcion[0] <="Z") or ("a"<=descripcion[0] <="z")):#revisamos solamente el primer caracter
                Descrip_X_validar = False#Cortamos el ciclo en caso de que el primer caracter sea una letra
                print("Ingreso una descripción válida")
            else:
                print("La Descripción que ingrego no es válida, la descrición del producto debe empezar por una letra.")
                descripcion = input("\nDescripción del producto: ")

    return(descripcion)

def validacionCategoria(CategoriaProd):
    '''Funcion para asignar una categoría al producto \nEntrada de la función: Categoría del producto 
    \nProceso de la funcion: Se ingresa la categoría del producto, y se verifica que pertenezca a alguno de las categorías validas; monitores, periféricos,
    sillas o hardware. En caso de ser otra categoría se le asigna Varios \nSalida de la función: Descripcion válida del producto
     \nAutor: Sergio Nicolas Carraud Fava'''
    lst_categorias_disponibles = ["Monitores","Sillas","Periféricos","Hardware","Accesorios"]#lista valida de categoría de productos para el sistema.
    for i in range (len(lst_categorias_disponibles)):
        if CategoriaProd.lower() == lst_categorias_disponibles[i].lower():
            print("\nCategoria del producto ingresada válida")
        else: 
            print("\nLa categoría que ingreso para el producto no existe, por lo que se guardara en categoría Varios")
            CategoriaProd = "Varios"

    return(CategoriaProd)

def validacionMarca(marcaProd):
    '''Funcion para validar la marca del producto ingresado. No debe ser vacio y debe tener 3 letras \nEntrada de la función: 
    Marca del producto \nProceso de la funcion: Validacion de que la descripción no este vacia y debe tener una longitud de 3 caracteres alfabeticos, 
    sino se vuelve a solicitar hasta que sea válida \nSalida de la función: Marca válida del producto \nAutor: Sergio Nicolas Carraud Fava'''
    Marca_X_validar = True  #Variable que nos servira para iterar hasta que nos devuelva una descripcion valida
    AcumuladorLetras=0  #Variable apra asegurarnos que tenga 3 letras
    while Marca_X_validar:
        if len(marcaProd) < 3:
            print("\nLa marca que ingreso no es valida, recuerde que debe ingresar una marca valida para el producto.")
            marcaProd = input("\nMarca del producto: ")
        else:
            for i in range (len(marcaProd)):
                if (("A"<=marcaProd[i] <="Z") or ("a"<=marcaProd[i] <="z")):
                    AcumuladorLetras = AcumuladorLetras + 1
            if AcumuladorLetras >= 3:
                print("\nMarca de producto ingresada valida")
                Marca_X_validar = False
            else:
                print("\nIngreso una marca no valida para el producto. Por favor volver a ingresar:")
                marcaProd = input("\nMarca del producto: ")
        
                
        

    return(marcaProd)


'funcion para dar de alta un producto y agregarlo a las listas correspondientes, se pide al usuario que ingrese la informacion del producto a agregar,'
'y se valida cada uno de los datos ingresados, si el identificador ya existe, se muestra un mensaje de error, sino se agrega el producto a las listas correspondientes'
'autor Tomas Kondratowicz'
def altaProductos(identificador,lst_identificador, lst_descripcion, lst_categorias, lst_precios, lst_stock, lst_marcas):
    
    descripcion = input("\nDescripción del producto: ")
    descripcion = validacionDescripcion(descripcion)
    categoria = input("\nCategoria del producto: ")
    categoria = validacionCategoria(categoria)
    precio = float(input("\nPrecio del producto: "))
    cantidad = random.randint(1, 50)
    marca = input("\nMarca del producto: ")
    marca = validacionMarca(marca)
    #si el identificador ya existe, se muestra un mensaje de error, sino se agrega el producto a las listas correspondientes
    if existeProducto(lst_identificador, identificador):
        print("El identificador ya existe")
    else:
        lst_identificador.append(identificador)
        lst_descripcion.append(descripcion)
        lst_categorias.append(categoria)
        lst_precios.append(precio)
        lst_stock.append(cantidad)
        lst_marcas.append(marca)

        print("Producto agregado correctamente")
        
    #    identificador = input("Ingrese una identificador, -1 para salir: ")

    return()
        
def ordenarProductos(lst_identificador, lst_descripcion, lst_categorias, lst_precios, lst_stock, lst_marcas):

    for i in range(len(lst_stock)-1):
        for j in range(i+1, len(lst_stock)):
            if lst_stock[i] < lst_stock[j]:
                # Intercambiar stock
                lst_stock[i], lst_stock[j] = lst_stock[j], lst_stock[i]
                # Intercambiar identificador
                lst_identificador[i], lst_identificador[j] = lst_identificador[j], lst_identificador[i]
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
                    # Intercambiar identificador
                    lst_identificador[i], lst_identificador[j] = lst_identificador[j], lst_identificador[i]
                    # Intercambiar descripciones
                    lst_descripcion[i], lst_descripcion[j] = lst_descripcion[j], lst_descripcion[i]
                    # Intercambiar categorias
                    lst_categorias[i], lst_categorias[j] = lst_categorias[j], lst_categorias[i]
                    # Intercambiar precios
                    lst_precios[i], lst_precios[j] = lst_precios[j], lst_precios[i]
                    # Intercambiar marcas
                    lst_marcas[i], lst_marcas[j] = lst_marcas[j], lst_marcas[i]



'funcion para mostrar los productos ordenados por stock de mayor a menor, '
'se muestra el identificador, descripcion, categoria, precio, stock y marca del producto'
'autor Tomas Kondratowicz'
def mostrarProductos(lst_identificador, lst_descripcion, lst_categorias, lst_precios, lst_stock, lst_marcas):
#armar la salida de forma tal que se se tome de base la longitud del producto con mayor cantidad de caracteres
    print("\n--- LISTA DE PRODUCTOS ---")

    if len(lst_identificador) == 0:
        print("No hay productos cargados")
    else:
        'La clave es que el número después de < debe ser mayor que la longitud máxima de los datos '
        'de esa columna. En este caso la descripción necesita al menos unos 35-40 caracteres para que no se pise con Categoría.'
        

        print(f"{'Identificador':<15}{'Descripcion':<80}{'Categoria':<50}{'Precio':<10}{'Stock':<10}{'Marca':<30}")

        for i in range(len(lst_identificador)):
            print(
                f"{lst_identificador[i]:<15}"
                f"{lst_descripcion[i]:<80}"
                f"{lst_categorias[i]:<50}"
                f"{lst_precios[i]:<10}"
                f"{lst_stock[i]:<10}"
                f"{lst_marcas[i]:<30}"
            )

def eliminarProducto(lst_identificador, lst_descripcion, lst_categorias, lst_precios, lst_stock, lst_marcas):#actualizar esto
    if len(lst_identificador) == 0:
        print("No hay productos actualmente. Debe al menos haber un producto.")
    else:    
        #previo debemos validar si la lista esta vacia....
        identificador = input("Ingrese el identificador del producto (-1 para finalizar): ")
        (identificador,identificadorValida) = validacionIdentificador(identificador)

        if identificadorValida:
        #si el identificador existe, se obtiene el indice del producto a eliminar, y se eliminan tanto el identificador, el stock y nombre de las listas correspondientes
            if existeProducto(lst_identificador, identificador):
                indice = -1
                for i in range(len(lst_identificador)):
                    if lst_identificador[i] == identificador:
                        indice = i
                lst_identificador.pop(indice)
                lst_stock.pop(indice)
                lst_descripcion.pop(indice)
                lst_categorias.pop(indice)
                lst_precios.pop(indice)
                lst_marcas.pop(indice)

                print("Producto eliminado correctamente")

            else:
                print("Producto no encontrado")

'funcion para modificar un producto, se pide al usuario que ingrese la descripcion del producto a modificar, si el producto existe, '
'se muestra un sub menu con las opciones de modificar cada atributo del producto, y se pide al usuario que seleccione una opcion, '
'si la opcion seleccionada no es valida, se pide nuevamente hasta que sea valida'
'autor Tomas Kondratowicz'

def modificarproducto (lst_identificador,lst_descripcion, lst_categorias, lst_stock, lst_precios, lst_marcas):#actualizar esto

    if len(lst_descripcion) == 0:
        print("No hay productos actualmente. Debe al menos haber un producto.")
    else:    
        #previo debemos validar si la lista esta vacia....
        descripcion = input("Ingrese el identificador del producto (-1 para finalizar): ")
        (descripcion) = validacionDescripcion(descripcion)

        seguir = True

        while seguir:

            #Si existe un producto con esa descripción, se obtiene el indice del producto a modificar
            #luego se muestra un sub menu con las opciones de modificar cada atributo del producto, 
            #y se pide al usuario que seleccione una opcion, si la opcion seleccionada no es valida, se pide nuevamente hasta que sea valida

            if existeProducto(lst_descripcion, descripcion):

                indice = lst_descripcion.index(descripcion)

                print("1. Modificar descripcion del producto")
                print("2. Modificar precio")
                print("3. Modificar stock")
                print("4. Modificar marca del fabricante")
                print("5. Modificar categoria")
                print("6. Modificar identificador")
                print("8. Salir")

                opcion = int(input("Seleccione una opcion: "))

                while (opcion < 1 or opcion > 6) and opcion != 8:
                    print("Opcion no valida")
                    opcion = int(input("Seleccione una opcion: "))

                if opcion == 1:
                    nueva_descripcion = input("Ingrese la nueva descripcion: ")
                    nueva_descripcion = validacionDescripcion(nueva_descripcion)
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
                    nueva_marca = validacionMarca(nueva_marca)
                    lst_marcas[indice] = nueva_marca
                    print("Marca del fabricante modificada correctamente")

                elif opcion == 5:
                    nueva_categoria = input("Ingrese la nueva categoria: ")
                    nueva_categoria = validacionCategoria (nueva_categoria)
                    lst_categorias[indice] = nueva_categoria
                    print("Categoria modificada correctamente")
                
                elif opcion == 6:#ACA HAY QUE METER LA VALIDACION ENCAPSULADA
                    nuevo_identificador = input("Ingrese el nuevo identificador: ")
                    nuevo_identificador = validacionIdentificador(nuevo_identificador)
                    if existeProducto(lst_identificador, nuevo_identificador):
                        print("El identificador ya existe")
                    else:
                        lst_identificador[indice] = nuevo_identificador
                        print("identificador modificado correctamente")

            else:
                print("Producto no encontrado")
            continuar = input("Desea modificar otro producto? (s/n): ")
            continuar = continuar.lower()
            if continuar != "s" and continuar != "si":
                seguir = False

            else:
                descripcion = input("Ingrese la descripcion del producto : ")

        return lst_identificador, lst_descripcion, lst_categorias, lst_stock, lst_precios, lst_marcas

#Casos de prueba.
def CasosdePrueba():
    lst_identificador =["MON_001","SillaGamer01","MOUSE99","RAM_RGB_01","Al_SSD_25"]    
    lst_descripcion = ["Monitor OLed Razer curvo 40'","Silla Ergonómica gamer Corsair - Roja","Mouse asus Next Gaming Inalambrico","Memoria ram 16gb SATA DDR5","Memoria de almacenamiento Kingston SSD 1 TB - RED - 4,5'"]
    lst_stock = [random.randint(1, 50),random.randint(1, 50),random.randint(1, 50),random.randint(1, 50),random.randint(1, 50)]
    lst_categorias = ["Monitor","Sillas","Periféricos","Hardware","Hardware"]
    lst_precios = [44.95,75,20,80,200]
    lst_marcas = ["Razer","Corsair","ASUS","Samsung","Kingston"]

    return(lst_identificador,lst_descripcion, lst_categorias, lst_stock, lst_precios, lst_marcas)
