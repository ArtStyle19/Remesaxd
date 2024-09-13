import math

def calcular_remesa_inversa_precisa(T):
    def ITF(R):
        return math.floor(0.00005 * R * 10) / 10

    def comision(R):
        if R <= 1000:
            return 5.00
        elif 1000 < R <= 10001:
            return 0.005 * R
        else:
            return 0.015 * R
 ## Busqueda Binaria
    low = 0  
    high = T  
    epsilon = 0.000001  

    while high - low > epsilon:
        R = (low + high) / 2
        C = comision(R)
        total = math.floor((R + ITF(R) + C) *10 ) /10

        if total > T:
            high = R
        elif total < T:
            low = R
        else:
            return R
    
    return R

# Ejemplo de entradas
entradas = [5025.20, 2311.60, 8888.20]

# Calcular las remesas correspondientes
remesas = [calcular_remesa_inversa_precisa(T) for T in entradas]

# Mostrar resultados
for i in range(len(entradas)):
    print(f"Total: {entradas[i]}, Remesa Calculada: {math.floor(remesas[i] * 10) / 10}")
