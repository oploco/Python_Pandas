import io
import time
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation
import pandas as pd


BUFFER_LEN = 64
DATA_FILENAME = "zbe_mediciones_Sonometro1.csv"

try:
    #df = pd.read_csv(io.StringIO(data))
    df= pd.read_csv(DATA_FILENAME)
    print(df)
    print(df['fechaF'], df['cana'])

    df.set_index('fechaF', inplace=True)
    df.plot()

    plt.title("Zonas de bajas emisiones: Mediciones de Sonómetros")
    plt.xlabel("fecha / s")
    plt.ylabel("valor / #")
    plt.scatter(df['fechaF'], df['val'])
except ValueError:
    print(f"W: {time.time()} :: EXCEPTION!", data)


plt.show()
plt.close()