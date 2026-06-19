import funciones

def main():

    lst_identificador = []    
    lst_Descripcion = []
    lst_stock = []
    lst_categorias = []
    lst_precios = []
    lst_marcas = []
    
    # #lista para casos de prueba
    # (lst_identificador,lst_Descripcion, lst_categorias, lst_stock, lst_precios, lst_marcas)= funciones.CasosdePrueba()

    opcion = 0

    while opcion != "8":

        funciones.mostrarMenu()

        opcion = funciones.ingresar_opcionMenu()

        match opcion:

            case "1":
                print("\nIngrese el identificador del producto para iniciar el alta del producto.")
                identificador = input("Ingrese un identificador (-1 para finalizar): ")
                (identificador,Ident_Valido) = funciones.validacionIdentificador(identificador)
                if Ident_Valido:
                    funciones.altaProductos(
                        identificador,
                        lst_identificador,
                        lst_Descripcion,
                        lst_categorias,
                        lst_precios,
                        lst_stock,
                        lst_marcas
                    )

            case "2":
                funciones.modificarproducto(
                    lst_identificador,
                    lst_Descripcion,
                    lst_categorias,
                    lst_stock,
                    lst_precios,
                    lst_marcas
                )

            case "3":
                funciones.eliminarProducto(
                    lst_identificador,
                    lst_Descripcion,
                    lst_categorias,
                    lst_precios,
                    lst_stock,
                    lst_marcas
                )

            case "4":
                funciones.ordenarProductos(
                    lst_identificador,
                    lst_Descripcion,
                    lst_categorias,
                    lst_precios,
                    lst_stock,
                    lst_marcas
                )
                funciones.mostrarProductos(
                    lst_identificador,
                    lst_Descripcion,
                    lst_categorias,
                    lst_precios,
                    lst_stock,
                    lst_marcas
                )

            case "8":
                print("Programa finalizado")


main()
