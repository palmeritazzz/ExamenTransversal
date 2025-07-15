productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def mostrar_stock(productos:str, stock:int):
    for i in productos:
        nombre_marca = productos[i][0]
        marca = input("Ingrese el nombre de la marca (Marque 1 para salir): ")
        if nombre_marca.lower() == marca.lower() or nombre_marca.upper == marca.upper():
            print("Elemento encontrado!")
            print(productos[i][0])
            for i in stock:
                print(f"Stock disponible:{stock[i][1]}")
        else:
            print("No se ha encontrado el elemento")
            break

def busqueda_precio(stock:int, productos:str):
    for i in stock:
        precio = stock[i][0]
        rangominimo = int(input("Ingrese el precio minimo: "))
        rangomaximo = int(input("Ingrese el rango maximo: "))
        if rangominimo >= precio and rangomaximo <= precio:
            print(productos)
        else:
            print("Rango de precios no valido")
            break
 
def menu():
    while True:

        print("\n*** MENU PRINCIPAL ***")
        print("\n[1] - Stock marca.")
        print("[2] - Busqueda por precio.")
        print("[3] - Actualizar precio.")
        print("[4] - Salir")

        try:
            opcion = int(input("Seleccione una opcion [1 - 4]: "))
        except ValueError:
            print("Debe seleccionar una opcion valida!!")
            continue

        if opcion == 1:
            while True:
                mostrar_stock(productos, stock)
        elif opcion == 2:
            busqueda_precio(stock, productos)
        elif opcion == 3:
            print("ok")
        elif opcion == 4:
            print("Programa finalizado.")
            break
        else:
            print("Debe ingresar una opcion valida [1 - 4]")

menu()
        
    