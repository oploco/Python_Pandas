import pandas as pd
import sys


#create_new_column_from_substring_in_another_column
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

data = r"""
date,col_1
2000-01-03,1
2000-01-04,3
2000-01-05,5
"""

df = pd.read_csv(StringIO(data),
                 index_col=['date'],
                 parse_dates=True
                 )

assert isinstance(df.index, pd.core.indexes.datetimes.DatetimeIndex)
print(df)