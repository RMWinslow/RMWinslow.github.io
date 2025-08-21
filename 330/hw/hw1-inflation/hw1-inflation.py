#%%

import pandas as pd
import numpy as np
import csv


#%% READ BEA 2.8.4 CSV (weird format)
with open('BEA2.8.4.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

years = rows[3][2:]
months = rows[4][2:]

# create a df with each year-month as a row
df = pd.DataFrame(rows[3][2:], columns=['Year',])
df['Month'] = rows[4][2:]

# extract_series_from_rows

for row in rows[5:]:
    if len(row) < 3: continue
    # Test if it's actually a data row. (First cell should be an integer and nothing else.)
    if not row[0].isdigit(): continue
    lineno = int(row[0]) 
    label = row[1].strip()
    series = [float(x) if x else np.nan for x in row[2:]]
    df[label] = series


df


#TODO: multindex so I can refer to data by line number?




#%%
