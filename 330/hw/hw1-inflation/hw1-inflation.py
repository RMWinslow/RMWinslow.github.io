#%%
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns


#%% READ BEA 2.8.4 CSV (weird format)
with open('BEA2.8.4.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

# create a df with each year-month as a row
df = pd.DataFrame(rows[3][2:], columns=['year',])
df['month'] = rows[4][2:]
# df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month']+'-1', format='%Y-%b-%d')
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month']+'-2', format='%Y-%b-%d')
df = df.set_index('date')

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

#%% PROBLEM 1: Plot PCE and PCE excluding food and energy

df['Headline PCE'] = df['Personal consumption expenditures (PCE)'].pct_change(periods=12) * 100
df['Core PCE, excl. food and energy'] = df['PCE excluding food and energy4'].pct_change(periods=12) * 100

df[['Headline PCE','Core PCE, excl. food and energy']].plot(
    title='12-Month Inflation Rate, based on PCE Price Index', 
    figsize=(10,5)
    )
plt.ylabel('% Change in Prices')
plt.grid(True)
plt.savefig('HW1_Q1_PCE_pct_change.png')

## %% Seaborn Equivalent.
sns.set_style("whitegrid")
plt.figure(figsize=(10, 5))
sns.lineplot(data=df[['Headline PCE', 'Core PCE, excl. food and energy']])

plt.title('12-Month Inflation Rate, based on PCE Price Index')
plt.ylabel('% Change')
plt.tight_layout()

plt.savefig('HW1_Q1_PCE_pct_change.png')






# %%
