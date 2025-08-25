#%%
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import seaborn as sns

#%% Recession shading Function
import os
from fredapi import Fred
fred = Fred(api_key = os.getenv('FRED_API_KEY'))
def shade_recessions(ax):
    xlims = ax.get_xlim()
    recessions = fred.get_series('USREC')
    ax.fill_between(recessions.index, 
                    0, 1, where=recessions==1, 
                    alpha=0.1, color='gray', 
                    transform=ax.get_xaxis_transform())
    ax.set_xlim(xlims)


#%% READ BEA 2.8.4 CSV (weird format)
with open('BEA2.8.4.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

# create a df with each year-month as a row
df = pd.DataFrame(rows[3][2:], columns=['year',])
df['month'] = rows[4][2:]
# df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month']+'-1', format='%Y-%b-%d')
df['date'] = pd.to_datetime(df['year'].astype(str) + '-' + df['month'], format='%Y-%b')
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



#%% PROBLEM 1: Plot PCE and PCE excluding food and energy

df['π_pce'] = df['Personal consumption expenditures (PCE)'].pct_change(periods=12) * 100
df['π_pce_core'] = df['PCE excluding food and energy4'].pct_change(periods=12) * 100

sns.set_style("whitegrid")
plt.figure(figsize=(10, 5))

sns.lineplot(data=df, x=df.index, y='π_pce', label='Headline PCE')
sns.lineplot(data=df, x=df.index, y='π_pce_core', label='Core PCE, excl. food and energy', linestyle='--')

plt.title('12-Month Inflation Rate, based on PCE Price Index')
plt.ylabel('% Change in Prices')
shade_recessions(plt.gca())

plt.grid(True)
plt.tight_layout()
plt.savefig('HW1_Q1_PCE_pct_change.png')






# %% PROBLEM 2: Predict Headline PCE using Headline and Core PCE
# Restrict data to June 1995-2024 during the month of June
df2 = df[(df.index.month == 6) & (df.index.year >= 1995)].copy()
df2 = df2[['π_pce', 'π_pce_core']].dropna()
df2['π_pce_next'] = df2['π_pce'].shift(-1)

def MSE(y_true, y_pred):
    return ((y_true - y_pred)**2).mean()

print("Mean Squared Error of Naive Forecasts:")
print("Using Headline PCE: ", MSE(df2['π_pce_next'], df2['π_pce']))
print("Using Core PCE:     ", MSE(df2['π_pce_next'], df2['π_pce_core']))






#%% PROBLEM 3: 3-month and 6-month core PCE Inflation, annualized
def annualized_pct_change(col, M):
    pc_change = df[col].pct_change(periods=M)
    annualized = (1 + pc_change) ** (12 / M) - 1
    return annualized * 100
df['π_pce_core_6m'] = annualized_pct_change('PCE excluding food and energy4', 6)
df['π_pce_core_3m'] = annualized_pct_change('PCE excluding food and energy4', 3)
df['π_pce_core_1m'] = annualized_pct_change('PCE excluding food and energy4', 1)
# df.plot(y=['π_pce_core','π_pce_core_6m', 'π_pce_core_3m'], figsize=(10,5))
# df['PCE excluding food and energy4'].plot(secondary_y=True, linestyle='--', color='gray', alpha=0.5)
# df['Personal consumption expenditures (PCE)'].plot(secondary_y=True, linestyle='--', color='gray', alpha=0.5)

df3 = df.copy()
# df3 = df[(df.index.month.isin([3,6,9,12])) & (df.index.year >= 1995)].copy()


plt.figure(figsize=(10, 5))

# plt.plot(df.index, df['π_pce'], label='Headline PCE')
sns.lineplot(data=df3, x=df3.index, y='π_pce_core', 
             label='12 Month change', marker=None)
sns.lineplot(data=df3, x=df3.index, y='π_pce_core_6m', 
             label='6 Month change, annualized rate', marker='o', markevery=(5,6))
sns.lineplot(data=df3, x=df3.index, y='π_pce_core_3m',
             label='3 Month change, annualized rate',  marker='.', markevery=(2,3))
# sns.lineplot(data=df3, x=df3.index, y='π_pce_core_1m',
#              label='1 Month change, annualized rate',  marker='.', )

plt.title('Core PCE Inflation',)
# plt.suptitle('Core PCE Inflation at Different Frequencies',
#              fontsize=16, fontweight='bold', y=0.98)
# plt.title('Annualized Rates', 
#           fontsize=12, color='gray', pad=20)
plt.ylabel('% Change in Prices')
shade_recessions(plt.gca())

plt.grid(True)
plt.tight_layout()


plt.xlim(pd.Timestamp('2020-01-01'),pd.Timestamp('2025-07-01'),)
plt.savefig('HW1_Q1_annualized_core_inflation.png')

# %%
