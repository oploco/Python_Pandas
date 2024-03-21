import pandas as pd
import sys
import matplotlib.pyplot as plt


#create_new_column_from_substring_in_another_column
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

fruit_price = r"""product,price
au-apple-1,2.5
au-apple-2,5.356
au-peach-1,4.99
au-peach-2,3.99
au-grape-2,3.99
"""

df = pd.read_csv(StringIO(fruit_price))
df['Is Apple'] = df['product'].apply(lambda x: 'Y' if 'apple' in x else 'N')

print(df)

df.plot()
plt.xlabel('Product')
plt.ylabel('Price')
plt.yscale('mercator')
plt.scatter(df['product'],df['price'])
plt.show()