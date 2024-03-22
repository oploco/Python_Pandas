import io
import time
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.animation
import pandas as pd
import matplotlib.dates as mdates

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
    fig, ax = plt.subplots(figsize=(15, 6))
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=25, horizontalalignment='right')

    # plt.figure(figsize=(15, 6))
    ax.set_title("Zonas de bajas emisiones: Mediciones de Sonómetros")

    print(df.loc[df['val'].idxmax()])
    print(df.loc[df['val'].idxmax()]['fechaF'],df.loc[df['val'].idxmax()]['val'])
    print("loc  ",df.loc[df['val'].idxmax()].iloc[2],df.loc[df['val'].idxmax()].iloc[0])

    maxValue=df.loc[df['val'].idxmax()].iloc[0]
    maxValueDate = df.loc[df['val'].idxmax()].iloc[2]

    #max
    plt.annotate("max= {}\nfecha= {}".format(str(maxValue),str(maxValueDate.strftime("%d/%m/%Y"))),
                 xy=(maxValueDate,maxValue),
                 xytext=(maxValueDate,maxValue-3),
                 arrowprops=dict(facecolor='black', shrink=5),
                 horizontalalignment='left',verticalalignment='top'
                 )

    ax.scatter(df['fechaF'], df['val'], s=df['val'], c=df['cana'], alpha=0.8)
    #df.plot(kind='bar',x='fechaF',y ='cana')

    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

    print("legend     ",ax.get_legend())

    ax.set_xlabel("fecha")
    ax.set_ylabel("valor")

    date_formatter = mdates.DateFormatter('%d-%m-%Y')
    # Set the major tick formatter to use your date formatter.
    ax.xaxis.set_major_formatter(date_formatter)

    ax.grid(True)


except ValueError:
    print(f"W: {time.time()} :: EXCEPTION!", df)

plt.show()
plt.close()