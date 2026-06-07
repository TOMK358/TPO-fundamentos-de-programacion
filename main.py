import funciones

def main():

    lst_codigos = []    
    lst_nombre = []
    lst_stock = []

    opcion = 0

    while opcion != 8:

        funciones.mostrarMenu()

        opcion = funciones.ingresar_opcionMenu()

        match opcion:

            case 1:
                funciones.altaProductos(
                    lst_codigos,
                    lst_nombre,
                    lst_stock
                )

            case 2:
                funciones.modificarStock(
                    lst_codigos,
                    lst_stock
                )

            case 3:
                funciones.eliminarProducto(
                    lst_codigos,
                    lst_stock,
                    lst_nombre
                )

            case 4:
                funciones.ordenarProductos_porstock(
                    lst_codigos,
                    lst_nombre,
                    lst_stock
                )
                funciones.mostrarProductos(
                    lst_codigos,
                    lst_nombre,
                    lst_stock
                )

            case 8:
                print("Programa finalizado")



main()

