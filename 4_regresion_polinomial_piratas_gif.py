import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import imageio
import os
from sklearn.metrics import mean_squared_error

# Datos ficticios para ilustrar la relación inversa entre temperatura y cantidad de piratas
temperatura = np.array([20, 23, 24, 25, 26]).reshape(-1, 1)  # Ejemplo de temperatura (en grados Celsius)
cantidad_piratas = np.array([50, 40, 30, 20, 10])  # Ejemplo de cantidad de piratas

# Función para generar el gráfico
def generar_grafico(temperatura, cantidad_piratas, iteracion):
    plt.scatter(temperatura[:iteracion], cantidad_piratas[:iteracion], color='blue', label='Datos originales')
    plt.plot(temperatura_prediccion, prediccion, color='red', label=f'Predicción polinomial (grado {grado_polinomio})')
    plt.plot(temperatura, prediccion_piratas, color='green', label='Regresión lineal')

    # Cargar la imagen de fondo
    imagen_fondo = plt.imread('C:\\Users\\Mañanas\\pictures\\fondo_pirata.jpg')
    plt.imshow(imagen_fondo,
               extent=[np.min(temperatura), np.max(temperatura), np.min(cantidad_piratas), np.max(cantidad_piratas)],
               aspect='auto', alpha=0.2)
    # Agregar etiquetas y título
    plt.title(f'Correlación entre temperatura y cantidad de piratas(Iteración {iteracion})')
    plt.xlabel('Cantidad de piratas')
    plt.ylabel('Temperatura (°C)')
    plt.text(0.5, -0.5, f'RMSE: {rmse:.2f}', ha='center')

    plt.legend()
    plt.grid(True)

    #plt.show()




# Grado del polinomio
grado_polinomio = 2

# Generar características polinomiales
poly_features = PolynomialFeatures(degree=grado_polinomio)
print(type(poly_features))

X_poly = poly_features.fit_transform(temperatura)
print(X_poly)

# Ajustar el modelo de regresión lineal a las características polinomiales
modelo = LinearRegression()
modelo.fit(X_poly, cantidad_piratas)

# Predecir con el modelo entrenado
temperatura_prediccion = np.linspace(temperatura.min(), temperatura.max(), 100).reshape(-1, 1)
X_poly_prediccion = poly_features.transform(temperatura_prediccion)
prediccion = modelo.predict(X_poly_prediccion)

modelolineal = LinearRegression()
modelolineal.fit(temperatura, cantidad_piratas)
prediccion_piratas = modelolineal.predict(temperatura)

# Calculamos el RMSE
rmse = np.sqrt(mean_squared_error(cantidad_piratas, prediccion_piratas))
print("RMSE:", rmse)

###
# Crear una carpeta temporal para almacenar las imágenes
if not os.path.exists('temp_imgs'):
    os.makedirs('temp_imgs')

# Generar y guardar cada iteración del gráfico como una imagen temporal
for i in range(len(temperatura) + 1):
    plt.figure()
    generar_grafico(temperatura, cantidad_piratas, i)
    plt.savefig(f'temp_imgs/iteracion_{i}.png')
    plt.close()

# Leer las imágenes temporales y guardarlas en un archivo GIF
imagenes = []
for filename in sorted(os.listdir('temp_imgs')):
    imagen_path = os.path.join('temp_imgs', filename)
    imagenes.append(imageio.imread(imagen_path))

# Guardar las imágenes en un archivo GIF
imageio.mimsave('grafico_animado.gif', imagenes)

"""
# Eliminar la carpeta temporal de imágenes
for filename in os.listdir('temp_imgs'):
    file_path = os.path.join('temp_imgs', filename)
    os.remove(file_path)
os.rmdir('temp_imgs')
"""
###





