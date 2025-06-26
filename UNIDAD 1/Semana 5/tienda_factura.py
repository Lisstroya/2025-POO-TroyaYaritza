# Programa: Factura electronica para una tienda
# Este programa permite ingresar el nombre de un producto, su precio unitario y cantidad comprada.
# Luego calcula el total a pagar y muestra un resumen de la compra.
# Utiliza tipos de datos: string, float, int y boolean.

# Solicita información del producto
nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario del producto ($): "))
cantidad_comprada = int(input("Ingrese la cantidad comprada: "))

# Calcula el total a pagar
total_pagar = precio_unitario * cantidad_comprada

# Booleano para verificar si la compra supera cierto valor
compra_grande = total_pagar > 20.00

# Mostrar resultados de los datos ingresados
print("\n--- Factura ---")
print("Producto:", nombre_producto)
print("Cantidad:", cantidad_comprada)
print("Precio Unitario: $", precio_unitario)
print("Total a Pagar: $", total_pagar)

# Comentario adicional según el total a pagar
if compra_grande:
    print("Gracias por tu compra. ¡Vuelve pronto, te esperamos!")
else:
    print("Muchas gracias por tu compra, lindo dia.")
