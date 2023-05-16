from collections import defaultdict

import numpy as np
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('2.txt', sep=' ', names=['minmax', 'char', 'pw'])
    df[['min', 'max']] = df['minmax'].str.split('-', expand=True)
    df['char'] = df['char'].str.rstrip(':')
    df['count'] = df.apply(lambda x: x['pw'].count(x['char']), axis=1)
    df['valid'] = df.apply(lambda x: int(x['min']) <= x['count'] <= int(x['max']), axis=1)
    print(df['valid'].sum())
