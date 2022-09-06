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

colormap = {"All Items": "#000", 
    "All items less food and energy": "#f00", 
    "Durables": "#742434", 
    "Nondurables": "#a2402b", 
    "Services": "#134a60", 
    "Food and beverages": "#ffbe50", 
    "Energy": "#fbaf82", 
    "Apparel": "#d9ae2f", 
    "Commodities": "#82a12b", 
    "Education": "#49d0a3", 
    "Communication": "#65a8c3", 
    "Housing": "#987fdc", 
    "Medical care": "#bd80ae", 
    "Recreation": "#f483cd", 
    "Transportation": "#f59080", 
    "Other goods and services": "#bdb7bf",}

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
    print(" "*8+"{name: "+f'"{title}",')
    print(" "*8+"color: "+f'"{colormap[title]}",')
    print("        data: [")
    for date, datum in zip(periods, series):
        print(" "*12+f"[{date}, {datum}],")
    print("        ]},")





#%%

import matplotlib.pyplot as plt

for title, series in data.items():
    print(title)
    plt.plot(series)
    #plt.show()

#plt.xlim(2012,2022)
#plt.ylim(50,150)
#plt.legend()