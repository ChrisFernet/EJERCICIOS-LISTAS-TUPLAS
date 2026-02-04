# tienda

def menu():
    print("=" * 40)
    print("Inventarios tienda CAMPUS")
    print("="*40)
    print("1. Agregar producto")
    print("2. Agregar lote de productos")
    print("3. Eliminar producto del inventario")
    print("4. Eliminar el producto más reciente")
    print("5. Ordenar productos alfabéticamente")
    print("6. Mostrar número total de productos")
    print("7. Salir")
    print("=" * 40)
    print("Seleccione una opción (1 - 7): ")

def leer_opcion():
    op=input()
    while(not op.isdigit() or int(op)<1 or int(op)>7):
        print("Opción no válida, digite un número del 1 al 7: ")
        input("Presione cualquier tecla para continuar...")
        print("\n\n")
        menu()
        op = input()

    return int(op)

def agregar_prod():
    producto = input("Escriba el producto que desea agregar: ")

    return producto.append

def main():
    productos = []
    menu()
    while ((opcion!=7)):

        opcion=leer_opcion()
        if opcion ==1:
            productos=agregar_prod(productos)
        elif opcion ==2:
            pass
        elif opcion ==3:
            pass
        elif opcion ==4:
            pass
        elif opcion ==5:
            pass
        elif opcion ==6:
            pass
        elif opcion ==7:
            print("\nGracias por usar el menú de inventarios de CAMPUS")

        input("Presione cualquier tecla para continuar....")
        print("\n\n")

main()