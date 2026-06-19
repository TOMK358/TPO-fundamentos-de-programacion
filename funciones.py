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

    while num < 0:
        print("Error, debe ser positivo")
        num = int(input(msg))

    return num

def existeProducto(lst_identificador, identificador):
    '''Funcion para revisar existencia del identificador en la lista.'''
    #recorre la lista de identificadoers y si encuentra el identificador ingresado, devuelve True, sino devuelve False
    for i in range(len(lst_identificador)):
        if lst_identificador[i] == identificador:
            variableExiste = True
            
            return True
        else:
            variableExiste = False
    
    if variableExiste:
        print("El producto existe!")
    else:
        print("El producto no existe!")

    return False

def validacionIdentificador(identificador):
    '''Funcion hecha para validar el ingreso de los identificadores de los productos.
    \nParametro de ingreso: identificador del producto
    \nProceso: se valida que el identificador ingresado no sea vacio, la longitud del mismo (entre 4 y 10 caracteres), y tenga caracteres alfanumericos o que posea unicamente como caracter especial "_"
    \nParametro de salida: Si el identificador es valido o no
    \nAutor: Sergio Nicolas Carraud Fava'''
    #inicializacion de variables
    IdentPorValidar = True
    #validar el identificador de los productos que se ingresan por consola
    while IdentPorValidar:  
        #Validamos que no este vacio.      
        if identificador == " ":
            print("Ingreso una identificador vacio, no sirve!!!")
            identificador = input("Ingrese un identificador, -1 para salir: ")

        if identificador == "-1":
            IdentPorValidar = False
            identificadorValida = False

        #Validamos la longitud del identificador ingresado
        elif len(identificador) < 4 or len(identificador) > 10:
            print("La longitud del identificador es invalida, ingrese una longitud valida para el identificador!!")
            identificador = input("Ingrese un identificador, -1 para salir: ")
        else:
            seguirValidando = True
            #Validamos los caracteres que se ingresan
            while seguirValidando:
                identificadorNoValida = False
                identificadorValida = False
                while len(identificador) < 4 or len(identificador) > 10:
                    print("La longitud del identificador es invalida, ingrese una longitud valida para el identificador!!")
                    identificador = input("Ingrese un identificador, -1 para salir: ")
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
    aux1 = False
    aux2 = False
    for i in range (len(lst_categorias_disponibles)):
        if CategoriaProd.lower() == lst_categorias_disponibles[i].lower():
            aux1 = True
        else:
            aux2 = True
    if aux1:
        print("\nCategoria del producto ingresada válida")
    elif aux2:
        print("\nLa categoría que ingreso para el producto no existe, por lo que se guardara en categoría Varios")
        CategoriaProd = "Varios"

    return(CategoriaProd)

def validacionMarca(marcaProd):
    '''Funcion para validar la marca del producto ingresado. No debe ser vacio y debe tener 3 letras \nEntrada de la función: 
    Marca del producto \nProceso de la funcion: Validacion de que la descripción no este vacia y debe tener una longitud de 3 caracteres alfabeticos, 
    sino se vuelve a solicitar hasta que sea válida \nSalida de la función: Marca válida del producto \nAutor: Sergio Nicolas Carraud Fava'''
    Marca_X_validar = True  #Variable que nos servira para iterar hasta que nos devuelva una descripcion valida
    while Marca_X_validar:
        AcumuladorLetras = 0  #Variable apra asegurarnos que tenga 3 letras
        if len(marcaProd) < 3:
            print("\nLa marca que ingreso no es valida, recuerde que debe ingresar una marca valida minimo de tres caracteres para el producto.")
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

def validacionPrecio(precio):
    sinPrecio = True
    while sinPrecio:
        if precio.isalnum():
            print("Precio ingresado invalido!!")
            precio = input("\nIngrese el precio del producto: ")
        else:
            print("Precio ingresado valido")
            precio = float(precio)
            sinPrecio = False
    
    return(precio)

def longIdent(lst_identificador):
    '''Funcion para obtener la longitud del identificador mas largo de la lista.
    Entrada de la funcion: Lista de identificadores
    Proceso de la funcion: Se recorre la lista comparando la longitud de cada identificador,
    si algun identificador supera los 13 caracteres (longitud del encabezado "Identificador"),
    se guarda el mas largo, sino se usa la longitud del encabezado como base
    Salida de la funcion: Longitud del identificador mas largo + 1
    Autor: Kevin Li'''
    IdentMasLargo = len(lst_identificador[0])
    x = True
    for i in lst_identificador:
        if len(i) > len("ID"):
            if len(i) > IdentMasLargo:
                IdentMasLargo = len(i)
                x = False
        elif x:
            IdentMasLargo = len("ID")
    IdentMasLargo = IdentMasLargo + 1
    
    return(IdentMasLargo)

def longDescrip(lst_descripcion):
    '''Funcion para obtener la longitud de la descripcion mas larga de la lista.
    Entrada de la funcion: Lista de descripciones
    Proceso de la funcion: Se recorre la lista comparando la longitud de cada descripcion,
    si alguna descripcion supera los 11 caracteres (longitud del encabezado "Descripcion"),
    se guarda la mas larga, sino se usa la longitud del encabezado como base
    Salida de la funcion: Longitud de la descripcion mas larga + 1
    Autor: Kevin Li'''
    DescripMasLargo = len(lst_descripcion[0])
    x = True
    for i in lst_descripcion:
        if len(i) > len("Descripcion"):
            if len(i) > DescripMasLargo:
                DescripMasLargo = len(i)
                x = False
        elif x:
            DescripMasLargo = len("Descripcion")
    DescripMasLargo = DescripMasLargo + 1
    
    return(DescripMasLargo)

def longCateg(lst_categorias):
    '''Funcion para obtener la longitud de la categoria mas larga de la lista.
    Entrada de la funcion: Lista de categorias
    Proceso de la funcion: Se recorre la lista comparando la longitud de cada categoria,
    si alguna categoria supera los 9 caracteres (longitud del encabezado "Categoria"),
    se guarda la mas larga, sino se usa la longitud del encabezado como base
    Salida de la funcion: Longitud de la categoria mas larga + 1
    Autor: Kevin Li'''
    CategMasLargo = len(lst_categorias[0])
    x = True
    for i in lst_categorias:
        if len(i) > len("Categoria"):
            if len(i) > CategMasLargo:
                CategMasLargo = len(i)
                x = False
        elif x:
            CategMasLargo = len("Categoria")
    CategMasLargo = CategMasLargo + 1
    
    return(CategMasLargo)

def longPrecios(lst_precios):
    '''Funcion para obtener la longitud del precio mas largo de la lista.
    Entrada de la funcion: Lista de precios
    Proceso de la funcion: Se recorre la lista convirtiendo cada precio a string y comparando
    su longitud, si algun precio supera los 6 caracteres (longitud del encabezado "Precio"),
    se guarda el mas largo, sino se usa la longitud del encabezado como base
    Salida de la funcion: Longitud del precio mas largo + 1
    Autor: Kevin Li'''
    PreciosMasLargo = len(str(lst_precios[0]))
    x = True
    for i in lst_precios:
        i_str = str(i)
        if len(i_str) > len("Precio"):
            if len(i_str) > PreciosMasLargo:
                PreciosMasLargo = len(i_str)
                x = False
        elif x:
            PreciosMasLargo = len("Precio")
    PreciosMasLargo = PreciosMasLargo + 1
    
    return(PreciosMasLargo)

def longStocks(lst_stock):
    '''Funcion para obtener la longitud del stock mas largo de la lista.
    Entrada de la funcion: Lista de stocks
    Proceso de la funcion: Se recorre la lista convirtiendo cada stock a string y comparando
    su longitud, si algun stock supera los 5 caracteres (longitud del encabezado "Stock"),
    se guarda el mas largo, sino se usa la longitud del encabezado como base
    Salida de la funcion: Longitud del stock mas largo + 1
    Autor: Kevin Li'''
    StockMasLargo = len(str(lst_stock[0]))
    x = True
    for i in lst_stock:
        i_str = str(i)
        if len(i_str) > len("Stock"):
            if len(i_str) > StockMasLargo:
                StockMasLargo = len(i)
                x = False
        elif x:
            StockMasLargo = len("Stock")
    StockMasLargo = StockMasLargo + 1
    
    return(StockMasLargo)

def longMarcas(lst_marcas):
    '''Funcion para obtener la longitud de la marca mas larga de la lista.
    Entrada de la funcion: Lista de marcas
    Proceso de la funcion: Se recorre la lista comparando la longitud de cada marca,
    si alguna marca supera los 5 caracteres (longitud del encabezado "Marca"),
    se guarda la mas larga, sino se usa la longitud del encabezado como base
    Salida de la funcion: Longitud de la marca mas larga + 1
    Autor: Kevin Li'''
    MarcasMasLargo = len(lst_marcas[0])
    x = True
    for i in lst_marcas:
        if len(i) > len("Marca"):
            if len(i) > MarcasMasLargo:
                MarcasMasLargo = len(i)
                x = False
        elif x:
            MarcasMasLargo = len("Marca")
    MarcasMasLargo = MarcasMasLargo + 1
    
    return(MarcasMasLargo)

'funcion para dar de alta un producto y agregarlo a las listas correspondientes, se pide al usuario que ingrese la informacion del producto a agregar,'
'y se valida cada uno de los datos ingresados, si el identificador ya existe, se muestra un mensaje de error, sino se agrega el producto a las listas correspondientes'
'autor Tomas Kondratowicz'
def altaProductos(identificador,lst_identificador, lst_descripcion, lst_categorias, lst_precios, lst_stock, lst_marcas):
    
    descripcion = input("\nDescripción del producto: ")
    descripcion = validacionDescripcion(descripcion)
    categoria = input("\nCategoria del producto: ")
    categoria = validacionCategoria(categoria)
    precio =input("\nPrecio del producto: ")
    precio = validacionPrecio(precio)
    eleccion = input("\nDesea ingresar manualmente o generar automáticamente utilizando valores aleatorios la cantidad de stock del producto? (m/a) ")
    while eleccion != "m" and eleccion != "M" and eleccion != "a" and eleccion != "A":
        eleccion = input("\nError! Por favor, ingrese 'm/M' (manual) o 'a/A' (automatico) para continuar: ")
    if eleccion == "a" or eleccion == "A":
        cantidad = random.randint(1, 50)
    elif eleccion == "m" or eleccion == "M":
        cantidad = int(input("\nPor favor, ingrese una cantidad exacta de stock: "))
        while cantidad < 0:
            cantidad = int(input("\nError! Por favor, ingrese una cantidad exacta de stock: "))
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
    print("\n--- LISTA DE PRODUCTOS ---")

    IdentMasLargo = longIdent(lst_identificador)
    DescripMasLargo = longDescrip(lst_descripcion)
    CategMasLargo = longCateg(lst_categorias)
    PreciosMasLargo = longPrecios(lst_precios)
    StockMasLargo = longStocks(lst_stock)
    MarcasMasLargo = longMarcas(lst_marcas)

    if len(lst_identificador) == 0:
        print("No hay productos cargados")
    else:
        'La clave es que el número después de < debe ser mayor que la longitud máxima de los datos '
        'de esa columna. En este caso la descripción necesita al menos unos 35-40 caracteres para que no se pise con Categoría.'
        

        print(f"{'ID':<{IdentMasLargo}}"
              f"{'Descripcion':<{DescripMasLargo}}"
              f"{'Categoria':<{CategMasLargo}}"
              f"{'Precio':<{PreciosMasLargo}}"
              f"{'Stock':<{StockMasLargo}}"
              f"{'Marca':<{MarcasMasLargo}}"
        )

        for i in range(len(lst_identificador)):
            print(
                f"{lst_identificador[i]:<{IdentMasLargo}}"
                f"{lst_descripcion[i]:<{DescripMasLargo}}"
                f"{lst_categorias[i]:<{CategMasLargo}}"
                f"{lst_precios[i]:<{PreciosMasLargo}}"
                f"{lst_stock[i]:<{StockMasLargo}}"
                f"{lst_marcas[i]:<{MarcasMasLargo}}"
            )

def eliminarProducto(lst_identificador, lst_descripcion, lst_categorias, lst_precios, lst_stock, lst_marcas):#actualizar esto
    Mantener_Eliminar=True

    if len(lst_identificador) == 0:
        print("No hay productos actualmente. Debe al menos haber un producto.")
    else:    
        while Mantener_Eliminar:
            #previo debemos validar si la lista esta vacia....
            identificador = input("Ingrese el identificador del producto (-1 para finalizar): ")
            (identificador,identificadorValida) = validacionIdentificador(identificador)
            if identificador == "-1":
                Mantener_Eliminar = False
            if identificadorValida:
            #si el identificador existe, se obtiene el indice del producto a eliminar, y se eliminan tanto el identificador, el stock y nombre de las listas correspondientes
                if existeProducto(lst_identificador, identificador):
                    eleccion_Borrar = input("Prodcuto encontrado, desea eliminarlo? Ingrese Si para continuar... ")
                    if eleccion_Borrar.lower() == "si":
                        for i in range(len(lst_identificador)):
                            if lst_identificador[i] == identificador:
                                indice = i
                            if lst_stock[i] !=0:
                                HayStock = True
                            else:
                                lst_identificador.pop(indice)
                                lst_stock.pop(indice)
                                lst_descripcion.pop(indice)
                                lst_categorias.pop(indice)
                                lst_precios.pop(indice)
                                lst_marcas.pop(indice)

                                print("Producto eliminado correctamente")
                                Mantener_Eliminar = False

                        if HayStock:
                            print("El producto ingresado tiene STOCK, no se puede borrar.")
                            print("Se regresa al menu anterior")
                    
                    Mantener_Eliminar=False
                    print("Se regresa al menu anterior")

                else:
                    print("Producto no encontrado")
            

'funcion para modificar un producto, se pide al usuario que ingrese la descripcion del producto a modificar, si el producto existe, '
'se muestra un sub menu con las opciones de modificar cada atributo del producto, y se pide al usuario que seleccione una opcion, '
'si la opcion seleccionada no es valida, se pide nuevamente hasta que sea valida'
'autor Tomas Kondratowicz'

def modificarproducto (lst_identificador,lst_descripcion, lst_categorias, lst_stock, lst_precios, lst_marcas):#actualizar esto

    descripcion = input("Ingrese la descripcion del producto : ")
    if len(lst_descripcion) == 0:
        print("No hay productos actualmente. Debe al menos haber un producto.")
    else:    
        #previo debemos validar si la lista esta vacia....
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
                    nuevo_precio = input("Ingrese el nuevo precio: ")
                    lst_precios[indice] = validacionPrecio(nuevo_precio)
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
                    (nuevo_identificador, valida) = validacionIdentificador(nuevo_identificador)
                    if existeProducto(lst_identificador, nuevo_identificador):
                        print("El identificador ya existe")
                    else:
                        lst_identificador[indice] = nuevo_identificador
                        print("identificador modificado correctamente")

            else:
                print("Producto no encontrado")
            seguir = input("Desea modificar otro producto? (s/n): ")
            if seguir != "s" and seguir != "S" and seguir != "si" and seguir != "SI" and seguir != "Si" and seguir != "sI":
                seguir = False

            else:
                descripcion = input("Ingrese la descripcion del producto : ")

        return lst_identificador, lst_descripcion, lst_categorias, lst_stock, lst_precios, lst_marcas

#Casos de prueba.
def CasosdePrueba():
    lst_identificador =["MON_001","Silla01","MOUSE99","RAM_RGB_01","Al_SSD_25"]    
    lst_descripcion = ["Monitor OLed Razer curvo 40'","Silla Ergonómica gamer Corsair - Roja","Mouse asus Next Gaming Inalambrico","Memoria ram 16gb SATA DDR5","Memoria de almacenamiento Kingston SSD 1 TB - RED - 4,5'"]
    lst_stock = [random.randint(1, 50),random.randint(1, 50),random.randint(1, 50),random.randint(1, 50),random.randint(1, 50)]
    lst_categorias = ["Monitor","Sillas","Periféricos","Hardware","Hardware"]
    lst_precios = [44.95,75,20,80,200]
    lst_marcas = ["Razer","Corsair","ASUS","Samsung","Kingston"]

    return(lst_identificador,lst_descripcion, lst_categorias, lst_stock, lst_precios, lst_marcas)