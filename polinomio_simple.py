import numpy as np
import matplotlib.pyplot as plt

# Coeficientes de la función polinomial (por ejemplo, y = 2x^2 + 3x + 4)
coeficientes = [1, -2, -3, 1]
coeficientes1 = [ -5, 3, -4]

# Crear un objeto polinomial a partir de los coeficientes
polinomio = np.poly1d(coeficientes)
polinomio1 = np.poly1d(coeficientes1)
print(polinomio)
print(polinomio1)

# Definir un rango de valores x para evaluar la función polinomial
x = np.linspace(-20, 20, 100)

# Evaluar la función polinomial en el rango de valores x
y = polinomio(x)
print('x =' ,x[0], 'y =',y[0])

# Graficar la función polinomial
#plt.scatter(x,y,color='red', label='Datos originales')
plt.plot(x, y, label=f'Función polinomial: \n {polinomio}')

y= polinomio1(x)
print('x =' ,x[0], 'y =',y[0])
plt.plot(x, y, label=f'Función polinomial: \n {polinomio1}')

# Agregar etiquetas y título al gráfico
plt.xlabel('x')
plt.ylabel('y')
plt.title('Función polinomial')
plt.legend()

# Mostrar el gráfico
plt.show()