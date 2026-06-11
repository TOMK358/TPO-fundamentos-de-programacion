import funciones

def main():

    lst_codigos = []    
    lst_Descripcion = []
    lst_stock = []
    lst_categorias = []
    lst_precios = []
    lst_marcas = []

    opcion = 0

    while opcion != 8:

        funciones.mostrarMenu()

        opcion = funciones.ingresar_opcionMenu()

        match opcion:

            case 1:
                funciones.altaProductos(
                    lst_codigos,
                    lst_Descripcion,
                    lst_categorias,
                    lst_precios,
                    lst_stock,
                    lst_marcas
                )

            case 2:
                funciones.modificarproducto(
                    lst_codigos,
                    lst_Descripcion,
                    lst_categorias,
                    lst_precios,
                    lst_stock,
                    lst_marcas
                )

            case 3:
                funciones.eliminarProducto(
                    lst_codigos,
                    lst_Descripcion,
                    lst_categorias,
                    lst_precios,
                    lst_stock,
                    lst_marcas
                )

            case 4:
                funciones.ordenarProductos_porstock(
                    lst_codigos,
                    lst_Descripcion,
                    lst_categorias,
                    lst_precios,
                    lst_stock,
                    lst_marcas
                )
                funciones.mostrarProductos(
                    lst_codigos,
                    lst_Descripcion,
                    lst_categorias,
                    lst_precios,
                    lst_stock,
                    lst_marcas
                )

            case 8:
                print("Programa finalizado")



main()

