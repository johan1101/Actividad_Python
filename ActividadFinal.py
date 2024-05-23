def agregarP(nombre, codigo, precio, cantidad):
   
    nuevo_producto = (nombre, codigo, precio, cantidad)
    inventario.append(nuevo_producto)


#PASO 1
Producto = (str, int, float, int)

# PASO 2
inventario = []

p1 = ("Mesas", 1111, 20.000, 100)
p2 = ("Sillas", 2222, 10.000, 23)
p3 = ("Cortinas", 3333, 5.000, 62)
p4 = ("Sobremesas", 4444, 7.000, 45)
p5 = ("Centros de mesa", 5555, 9.000, 47)

inventario.append(p1)
inventario.append(p2)
inventario.append(p3)
inventario.append(p4)
inventario.append(p5)

print("Ingresa tus productos")

nom=input("Digite el nombre del producto\n")
cod=int(input("Digite el codigo  del producto \n"))
pre=float(input("Digite el precio  del producto \n"))
cant=int(input("Digite la cantidad  del producto \n"))

agregarP(nom, cod, pre, cant)

print("-------------------------------------------------")
print("                 INVENTARIO")
print("-------------------------------------------------")
for producto in inventario:
    print(f"Nombre: {producto[0]}, Código: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}")