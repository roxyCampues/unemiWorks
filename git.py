import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Usar backend "Agg" para evitar abrir ventanas en Codespaces
matplotlib.use('Agg')  

# Interpolación de Newton (diferencias divididas)
def calcular_diferencias_divididas(valores_x, valores_y):
    num_puntos = len(valores_x)
    coeficientes = np.copy(valores_y)

    for i in range(1, num_puntos):
        for j in range(num_puntos - 1, i - 1, -1):
            coeficientes[j] = (coeficientes[j] - coeficientes[j - 1]) / (valores_x[j] - valores_x[j - i])

    return coeficientes

def interpolacion_newton(valores_x, coeficientes, valor_x):
    num_puntos = len(valores_x)
    valor_interpolado = coeficientes[-1]

    for i in range(num_puntos - 2, -1, -1):
        valor_interpolado = valor_interpolado * (valor_x - valores_x[i]) + coeficientes[i]

    return valor_interpolado

# Interpolación Inversa de Newton
def interpolacion_newton_inversa(valores_x, valores_y, valor_y):
    coeficientes_newton = calcular_diferencias_divididas(valores_y, valores_x)
    num_puntos = len(valores_x)
    valor_interpolado_x = coeficientes_newton[0]
    termino_producto = 1

    for i in range(1, num_puntos):
        termino_producto *= (valor_y - valores_y[i - 1])
        valor_interpolado_x += coeficientes_newton[i] * termino_producto

    return valor_interpolado_x

# Graficar Interpolaciones Directas
def graficar_interpolacion_newton(valores_x, valores_y, valor_x, y_newton):
    x_vals = np.linspace(min(valores_x), max(valores_x), 100)
    coeficientes_newton = calcular_diferencias_divididas(valores_x, valores_y)
    y_vals_newton = [interpolacion_newton(valores_x, coeficientes_newton, x) for x in x_vals]

    # Graficar
    plt.scatter(valores_x, valores_y, color='red', label='Puntos originales')
    plt.plot(x_vals, y_vals_newton, label='Interpolación de Newton')

    # Punto interpolado
    plt.scatter(valor_x, y_newton, color='green', label=f'Newton en x={valor_x}')

    plt.title('Interpolación Directa de Newton')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)

    # Guardar el gráfico en un archivo
    plt.savefig('grafico_interpolacion_directa_newton.png')
    plt.close()

# Graficar Interpolación Inversa
def graficar_interpolacion_inversa_newton(valores_x, valores_y, valor_y, x_interpolado):
    y_vals = np.linspace(min(valores_y), max(valores_y), 100)
    x_vals = [interpolacion_newton_inversa(valores_x, valores_y, y) for y in y_vals]

    plt.scatter(valores_y, valores_x, color='red', label='Puntos originales')
    plt.plot(y_vals, x_vals, label='Interpolación Inversa de Newton')
    plt.scatter(valor_y, x_interpolado, color='blue', label=f'Interpolación inversa en y={valor_y}')

    plt.title('Interpolación Inversa de Newton')
    plt.xlabel('y')
    plt.ylabel('x')
    plt.legend()
    plt.grid(True)

    # Guardar el gráfico en un archivo
    plt.savefig('grafico_interpolacion_inversa_newton.png')
    plt.close()

# Datos del ejercicio
valores_x = [1, 2, 3]
valores_y = [2, 3, 5]

# Interpolación directa para x = 2.5
valor_x = 2.5
coeficientes_newton = calcular_diferencias_divididas(valores_x, valores_y)
y_newton = interpolacion_newton(valores_x, coeficientes_newton, valor_x)

print(f"Valor de y para x = {valor_x} usando Newton: {y_newton:.4f}")

# Graficar interpolación directa de Newton
graficar_interpolacion_newton(valores_x, valores_y, valor_x, y_newton)

# Interpolación inversa para y = 4
valor_y_inversa = 4
x_interpolado_inversa = interpolacion_newton_inversa(valores_x, valores_y, valor_y_inversa)
print(f"Valor de x para y = {valor_y_inversa} usando interpolación inversa de Newton: {x_interpolado_inversa:.4f}")

# Graficar interpolación inversa de Newton
graficar_interpolacion_inversa_newton(valores_x, valores_y, valor_y_inversa, x_interpolado_inversa)