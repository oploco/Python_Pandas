import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Datos ficticios para ilustrar la relación inversa entre temperatura y cantidad de piratas
temperatura = np.array([20, 23, 24, 25, 26]).reshape(-1, 1)  # Ejemplo de temperatura (en grados Celsius)
cantidad_piratas = np.array([50, 40, 30, 20, 10])  # Ejemplo de cantidad de piratas

# Grado del polinomio
grado_polinomio = 2

# Generar características polinomiales
poly_features = PolynomialFeatures(degree=grado_polinomio)
print(poly_features)

X_poly = poly_features.fit_transform(temperatura)

# Ajustar el modelo de regresión lineal a las características polinomiales
modelo = LinearRegression()
modelo.fit(X_poly, cantidad_piratas)

# Predecir con el modelo entrenado
temperatura_prediccion = np.linspace(temperatura.min(), temperatura.max(), 100).reshape(-1, 1)
X_poly_prediccion = poly_features.transform(temperatura_prediccion)
prediccion = modelo.predict(X_poly_prediccion)



# Graficar los datos originales y la predicción
plt.scatter(temperatura, cantidad_piratas, color='blue', label='Datos originales')
plt.plot(temperatura_prediccion, prediccion, color='red', label=f'Predicción polinomial (grado {grado_polinomio})')

modelolineal = LinearRegression()
modelolineal.fit(temperatura, cantidad_piratas)
prediccion_piratas = modelolineal.predict(temperatura)

plt.plot(temperatura,prediccion_piratas, color='green', label='Regresión lineal')

# Cargar la imagen de fondo
imagen_fondo = plt.imread('C:\\Users\\Mañanas\\pictures\\fondo_pirata.jpg')
plt.imshow(imagen_fondo, extent=[np.min(temperatura), np.max(temperatura), np.min(cantidad_piratas), np.max(cantidad_piratas)], aspect='auto', alpha=0.3)


# Agregar etiquetas y título
plt.title('Correlación entre temperatura y cantidad de piratas')
plt.xlabel('Cantidad de piratas')
plt.ylabel('Temperatura (°C)')


# Mostrar la leyenda
plt.legend()

# Mostrar el scatter plot con la línea de regresión
plt.show()


# Función para generar el gráfico
def generar_grafico(temperatura, cantidad_piratas, iteracion):
    plt.scatter(temperatura[:iteracion], cantidad_piratas[:iteracion], color='blue', label='Datos originales')
    plt.plot(temperatura, cantidad_piratas, color='red', label='Predicción polinomial')
    plt.title(f'Gráfico de Temperatura vs Cantidad de Piratas (Iteración {iteracion})')
    plt.xlabel('Temperatura')
    plt.ylabel('Cantidad de Piratas')
    plt.legend()
    plt.grid(True)

# Crear una lista para almacenar las imágenes generadas
imagenes = []

# Generar y guardar cada iteración del gráfico en la lista de imágenes
for i in range(len(temperatura) + 1):
    plt.figure()
    generar_grafico(temperatura, cantidad_piratas, i)
    # Convertir el gráfico actual a una imagen y añadirla a la lista
    imagen = plt.gcf()
    imagenes.append(imagen)
    plt.close()

# Guardar las imágenes en un archivo GIF
imageio.mimsave('grafico_animado.gif', imagenes)