import pandas as pd
from dateutil.relativedelta import relativedelta, FR, MO

list_of_dicts = [
    {
        'date': '2024-03-20',
        'weather': 'cloudy'
    },
    {
        'date': '2018-03-02',
        'weather': 'sunny'
    },
    {
        'date': '2018-03-03'
    },
    {
        'date': '2018-03-04',
        'weather': 'rain'
    }
]
df = pd.DataFrame(list_of_dicts)

#df.set_index(df['date'])
df['date'] = pd.to_datetime(df['date'])
df['last_friday'] = df['date'].apply(lambda x: x + relativedelta(weekday=FR(-1)))
df['last_monday'] = df['date'].apply(lambda x: x + relativedelta(weekday=MO(-1)))
print(df)