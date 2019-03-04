#!/usr/bin/env python3
import numpy as np
import pandas as pd
# http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

s1 = pd.Series([10, 20, 30])
s2 = pd.Series(['hi', 'foo', 'bar'])
print(s1)
print(s2)

df = pd.DataFrame({
    'number': s1,
    'word': s2
})
print(df)
print(df['number'])
print(df['word'] == 'foo')
print(df[df['word'] == 'foo'])
