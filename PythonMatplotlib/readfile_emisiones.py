import io
import time
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation
import pandas as pd

BUFFER_LEN = 64
DATA_FILENAME = "zbe_mediciones_Sonometro1.csv"

try:
    # df = pd.read_csv(io.StringIO(data))
    df = pd.read_csv(DATA_FILENAME,
                     parse_dates=['fechaF'],
                     usecols=['val', 'fechaF', 'cana'])

    print("impersion df", df)

    df.head()
    # df['fecha'] = pd.to_datetime(df['fechaF'])
    df.set_index(df['fechaF'])

    plt.style.use('ggplot')

    plt.figure(figsize=(15, 6))
    plt.title("Zonas de bajas emisiones: Mediciones de Sonómetros")

    plt.subplot(131)
    plt.bar(df['fechaF'], df['val'])

    plt.subplot(132)
    plt.scatter(df['fechaF'], df['val'], s=df['val'], c=df['cana'], alpha=0.5)
    plt.legend(df['cana'])
    plt.grid(True)

    plt.xlabel("fecha")
    plt.ylabel("valor")
    plt.legend(df['cana'])

    plt.subplot(133)
    plt.plot(df['fechaF'], df['val'])

except ValueError:
    print(f"W: {time.time()} :: EXCEPTION!", df)

plt.show()
plt.close()