import pandas as pd
import io

weather = r"""city,weather
sydney,rain
melbourne,sunny
brisbane,sunny
"""

city = r"""city,state,pob
sydney,nsw,1000
brisbane,qld,2000
perth,sa,3000
"""

df_1 = pd.read_csv(io.StringIO(weather))
df_2 = pd.read_csv(io.StringIO(city))

print("> {join}:".format(join="inner join"))
df = pd.merge(left=df_1, right=df_2, on='city', how='inner')
print(df)
print("\n")

print("> {join}:".format(join="outer join"))
df = pd.merge(left=df_1, right=df_2, on='city', how='outer')
print(df)
print("\n")

print("> {join}:".format(join="left outer join"))
df = pd.merge(left=df_1, right=df_2, on='city', how='left')
print(df)
print("\n")

print("> {join}:".format(join="right outer join"))
df = pd.merge(left=df_1, right=df_2, on='city', how='right')
print(df)