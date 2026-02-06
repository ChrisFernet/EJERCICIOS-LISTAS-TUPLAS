# tienda

def menu():
    print("=" * 40)
    print("      Inventarios tienda CAMPUS      ")
    print("="*40)
    print("1. Agregar producto")
    print("2. Agregar lote de productos")
    print("3. Eliminar producto del inventario")
    print("4. Eliminar el producto más reciente")
    print("5. Ordenar productos alfabéticamente")
    print("6. Mostrar número total de productos")
    print("7. Salir")
    print("=" * 40)
    print("\nSeleccione una opción (1 - 7): ")

def leer_opcion():
    op=input()
    while(not op.isdigit() or int(op)<1 or int(op)>7):
        print("Opción no válida, digite un número del 1 al 7: ")
        input("Presione cualquier tecla para continuar...")
        print("\n\n")
        menu()
        op = input()

    return int(op)

def agregar_prod(lista):
    productos = input("Escriba el producto que desee agregar: ")
    producto = productos.strip()
    if producto != "":
        lista_productos = productos.strip()   
        lista.append(lista_productos) 
        print(f"Lista actual: {lista}")
    else: 
        print("Producto inválido. Presione cualquier tecla para continuar.")
    return lista

def agregar_lote(lista):
    productos = input("Escriba el lote de productos que desee agregar separados por comas: ")
    lista_productos = productos.strip()  
    lista_productos = productos.split(",")
    lista.extend(lista_productos) 
    print(f"Lista actual: {lista}")

    return lista

def eliminar_prod(lista):
    prod = input("Escriba el producto que desee eliminar: ")
    producto = prod.strip()   
    lista.remove(producto) 
    print(f"Lista actual: {lista}")
    return lista

def main():
    productos_lista = []
    opcion = 0
    while ((opcion!=7)):
        menu()
        opcion=leer_opcion()

        if opcion ==1:
            productos_lista = agregar_prod(productos_lista)
        elif opcion ==2:
            productos_lista = agregar_lote(productos_lista) 
        elif opcion ==3:
            eliminar_prod(productos_lista)
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
