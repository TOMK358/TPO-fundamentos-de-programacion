import funciones

def main():

    lst_codigos = []    
    lst_Descripcion = []
    lst_stock = []
    lst_categorias = []
    lst_precios = []
    lst_marcas = []

    lst_codigos = ["MON001","TEC005","SIL073","AUR123"]    
    lst_Descripcion = ["Monitor Samsung 24 pulgadas","Teclado Logitech K120","Silla Gamer SILVERSTONE SGC500","Auriculares Gamer HyperX Cloud Stinger"]
    lst_stock = [5,20,77,5]
    lst_categorias = ["Monitores","Perifericos","Sillas Gamer","Auriculares"]
    lst_precios = [50,20,150,70]
    lst_marcas = ["Samsung","Logitech","Silverstone","HyperX"]

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
                funciones.ordenarProductos(
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

