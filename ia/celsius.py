import tensorflow as tf
import numpy as np

# Datos de entrenamiento (Celsius y su equivalente en Fahrenheit)
celsius = np.array([-40.0, -10.0, 0.0, 8.0, 15.0, 22.0, 38.0], dtype=float)
fahrenheit = np.array([-40.0, 14.0, 32.0, 46.0, 59.0, 72.0, 100.0], dtype=float)

# Capa oculta con una sola neurona
capa_oculta = tf.keras.layers.Dense(units=1, input_shape=[1])

# Modelo secuencial con una capa oculta
modelo = tf.keras.Sequential([capa_oculta])

# Compilación del modelo
modelo.compile(loss='mean_squared_error',
                optimizer=tf.keras.optimizers.Adam(0.1))

# Entrenamiento del modelo
historia = modelo.fit(celsius, fahrenheit, epochs=500, verbose=False)
print("Modelo entrenado.")

# Predicción de la temperatura en Fahrenheit para un valor en Celsius
temperatura_celsius = np.array([15.0], dtype=float)
temperatura_fahrenheit = modelo.predict([temperatura_celsius])
print(f"{temperatura_celsius} grados Celsius equivale a {temperatura_fahrenheit[0][0]} grados Fahrenheit.")

# Evaluar el modelo
puntaje = modelo.evaluate(celsius, fahrenheit)
print("score:", historia.score())