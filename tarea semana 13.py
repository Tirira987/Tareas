def calcularTotal(precio, cantidad):
    total = precio * cantidad
    return total
print("Bienvenido")

while True:
    Precio = input("Ingrese el precio del producto:")
    Cantidad = input("Ingrese la cantidad:")
    precio = float(Precio)
    cantidad = int(Cantidad)
    
    if precio > 0 and cantidad > 0:
        break
    else:
        print("Datos incorrectos, intente nuevamente")
resultado = calcularTotal(precio, cantidad)
print("El total de la compra es:",resultado)