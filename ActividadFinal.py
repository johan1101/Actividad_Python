# Construido por: Maria Casanova - Johan Ordoñez


# Metodo para agregar un producto al inventario
def agregarP(nombre, codigo, precio, cantidad):
   
    nuevo_producto = (nombre, codigo, precio, cantidad)
    inventario.append(nuevo_producto)
    print("Producto registrado exitosamente")


# Metodo para actualizar la cantidad de un producto especifico
def actualizarStock(codigo, cantidad):
    encontrado = False
    for producto in inventario:
        if producto[1] == codigo:
            nuevoStock = list(producto)
            inventario.remove(producto)
            nuevoStock[3] = cantidad
            inventario.append(tuple(nuevoStock))
            encontrado = True
            print("")
            print("Stock actualizado con exito")
            print("")

    if encontrado == False:
        print("")
        print("No se encontro ningún producto con el codigo ingresado")
        print("")


# Metodo para dar el costo total del inventario
def costoTotal():
    total = 0
    for producto in inventario:
        total = total + (producto[2] * producto[3])
    print("")
    print("El costo total del inventario es de $", total)
    print("")


# Metodo para listar todos los productos del inventario
def listarProductos():
    print("-------------------------------------------------")
    print("                 INVENTARIO :)")
    print("-------------------------------------------------")
    print("")
    for producto in inventario:
        print(f"Nombre: {producto[0]}, Código: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}")
    print("")


# Metodo utilizado para buscar un producto con el código especificado
def buscarProducto():
    encontrado = False
    print("")
    print("Ingrese el código del producto a buscar")
    print("")
    codigoProducto = int(input())
    print("")
    for producto in inventario:
        if producto[1] == codigoProducto:
                encontrado = True
                print(f"Nombre: {producto[0]}, Código: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}")

    if encontrado == False:
        print("No se encontro ningún producto con ese código")
    print("")


# Metodo que da la bienvenida al programa 
def bienvenida():
    print("")
    print("----------------------------------")
    print("Bienvenido joven")
    print("----------------------------------")
    print("")


# Metodo que muestras las opciones del programa 
def opciones():
    print("----------------------------------")
    print("Seleccione una de las opciones")
    print("")
    print("1. Agregar un nuevo producto")
    print("2. Actualizar el stock de un producto")
    print("3. Obtener el valor total del inventario")
    print("4. Buscar producto")
    print("5. listar productos registrados")
    print("6. Salir del programa")
    print("")


# La tupla de los productos tendra la siguiente estructuras
Producto = (str, int, float, int)

# Se crea un inventario de tipo list para almacenar los productos
inventario = []

# Se establecen productos para ser agregados al inventario
p1 = ("Mesas", 1111, 20.000, 100)
p2 = ("Sillas", 2222, 10.000, 23)
p3 = ("Cortinas", 3333, 5.000, 62)
p4 = ("Sobremesas", 4444, 7.000, 45)
p5 = ("Centros de mesa", 5555, 9.000, 47)

# Se agregan los productos al inventario
inventario.append(p1)
inventario.append(p2)
inventario.append(p3)
inventario.append(p4)
inventario.append(p5)

# Se llama al metodo de bienvenida
bienvenida()

# Se utiliza while para repetir las opciones del programa hasta que se ingrese el valor 6
while True:

    # Se llama al metodo para mostrar las opciones del programa
    opciones()

    # Utilizado para capturar un error en caso de que se ingrese un valor no numerico
    try:
        # Se recibe la opcion del usuario y se transforma a entero
        opcionIngresada = int(input())
    except:
        print("")

    # Utilizado para capturar un error en caso de que se ingrese un valor no numerico
    try:
        # Permite el control de las opciones
        match opcionIngresada:
            
            # El caso se utiliza para agregar un nuevo producto
            case 1:
                print("")
                nom=input("Digite el nombre del producto\n")
                print("")
                cod=int(input("Digite el codigo  del producto \n"))
                print("")
                pre=float(input("Digite el precio  del producto \n"))
                print("")
                cant=int(input("Digite la cantidad  del producto \n"))
                print("")
                agregarP(nom, cod, pre, cant)

            # El caso 2 se utiliza para actualizar el stock de un producto
            case 2:
                print("Ingrese el codigo del producto que desea actualizar")
                codigo = int(input())
                print("")
                print("Ingrese la nueva cantidad del stock que tendra el producto")
                stock = int(input())
                actualizarStock(codigo, stock)

            # El caso 3 se utiliza para obtener el costo total del inventario
            case 3:
                costoTotal()

            # El caso 4 busca un producto de acuerdo al código ingresado por el usuario
            case 4:
                buscarProducto()

            # El caso 5 lista los productos existentes en el inventario
            case 5:
                listarProductos()

            # Finaliza el programa con un mensaje :)
            case 6:
                print("---------------------------")
                print("Hasta luego joven, vuelva pronto :)")
                print("")
                break

            # Se utiliza en caso de que el usuario ingrese un valor no valido dentro de las opciones
            case _:
                print("")
                print("Por favor, ingrese un valor valido")
                print("")
    except:
        print("")
        print("Por favor, ingrese un valor valido")
        print("")