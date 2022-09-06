#%% Construct Time Labels for Highcharts Series
INITIALYEAR = 2000
FINALYEAR = 2021
INITIALMONTH = 1-1
FINALMONTH = 9-1

periods = []
for year in range(INITIALYEAR,FINALYEAR+1):
    for month in  range(0,12):
        print(f"{year}-{month}")
        periods.append(f"Date.UTC({year}, {month}, 15)")
periods = periods[INITIALMONTH:FINALMONTH-11]
dataLength = len(periods)


#%% Colors for lines

colormap = {"All Items": "#f00", 
    "All items less food and energy": "#f00", 
    "Durables": "#f00", 
    "Nondurables": "#f00", 
    "Services": "#f00", 
    "Food and beverages": "#f00", 
    "Energy": "#f00", 
    "Apparel": "#f00", 
    "Commodities": "#f00", 
    "Education": "#f00", 
    "Communication": "#f00", 
    "Housing": "#f00", 
    "Medical care": "#f00", 
    "Recreation": "#f00", 
    "Transportation": "#f00", 
    "Other goods and services": "#f00",}

# %% Pull data from CPI download
SOURCE = "C-CPI-U.csv"
data = dict()
with open(SOURCE,'r') as f:
    for line in f.readlines()[4:]:
        line = line.split(',')
        if len(line) > 5:
            title = line[1]
            #print(len(line))
            #print([value for value in line[2:2+dataLength]])
            series = [float(value) for value in line[2:2+dataLength]]
            data[title] = series

#%%Format data for highcharts
for title in colormap:
    series = data[title]
    print(" "*12+"{ name: "+f'"{title}",')
    print("            data: [")
    for date, datum in zip(periods, series):
        print(" "*16+f"[{date}, {datum}],")
    print("            ]},")





#%%

import matplotlib.pyplot as plt

for title, series in data.items():
    print(title)
    plt.plot(series)
    #plt.show()

#plt.xlim(2012,2022)
#plt.ylim(50,150)
#plt.legend()