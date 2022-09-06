#%% Construct Time Labels for Highcharts Series
INITIALYEAR = 2000
FINALYEAR = 2021
INITIALMONTH = 1
FINALMONTH = 9

periods = []
for year in range(INITIALYEAR,FINALYEAR+1):
    for month in  range(1,12+1):
        periods.append(f"Date.UTC({year}, {month}, 15)")
periods = periods[INITIALMONTH-1:FINALMONTH-12]
dataLength = len(periods)

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
#for title, series in data.items():
series = data["Communication"]
title = "Communication"
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