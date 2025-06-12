# Programación Tradicional - Cálculo del promedio semanal del clima

def obtener_temperaturas():
    # Datos sobre las temperaturas durante los 7 dias de la semana
    return [27, 25, 23, 29, 26, 30, 31]

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def mostrar_resultados(temperaturas, promedio):
    print("Programación Tradicional")
    print("Temperaturas:", temperaturas)
    print(f"Promedio semanal: {promedio:.2f} °C")

# Lógica principal
temps = obtener_temperaturas()
prom = calcular_promedio(temps)
mostrar_resultados(temps, prom)