#%% 
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(dpi=200)

labels_1 = ['Employee Compensation', 'Net Taxes', 'Net Operating Surplus', 'Consumption of Fixed Capital', ]
sizes_1 = [11.4594, 1.4594, 5.0878, 3.4356]
colors_1 = ['#e00','#dd0','#0c0','#00e',]

labels_2 = ['Wages and salaries', 'Supplements to wages and salaries',
    'Net Taxes', 
    'Net interest', 'Business current transfer payments', 'Proprietors income', 'Rental income', 'Corporate profits', 
    'Private Consumption of Fixed Capital', 'Government Consumption of Fixed Capital']
sizes_2 = [9.3353, 2.1242,
    1.4594,
    0.7935,0.1623,1.5989,0.6921,1.8544,
    2.8486,0.5869,
    ]
colors_2 = ['#f00','#d00',
    '#ff0',
    '#0f0','#0d0','#0c0','#0a0','#090',
    '#00d','#00f',
    ]


size = 0.3
vals = np.array([[60., 32.], [37., 40.], [29., 10.]])

'''
ax.pie(vals.sum(axis=1), radius=1, 
       wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(vals.flatten(), radius=1-size, 
       wedgeprops=dict(width=size, edgecolor='w'))'''

ax.pie(sizes_2, colors=colors_2,  radius=1, )
ax.pie(sizes_1, colors=colors_1,  radius=1-size, )
#autopct='%1.1f%%'


ax.set(aspect="equal")
plt.show()

# %%
'''
    Gross domestic income	21.4422
Compensation of employees, paid	11.4594
  Wages and salaries	9.3353
      To persons	9.3164
      To the rest of the world	0.0189
  Supplements to wages and salaries	2.1242
Taxes on production and imports	1.5323
Less: Subsidies\1\	0.0730
Taxes less subsidies	1.4594
Net operating surplus	5.0878
  Private enterprises	5.1011
    Net interest and miscellaneous payments, domestic industries	0.7935
    Business current transfer payments (net)	0.1623
    Proprietors' income with inventory valuation and capital consumption adjustments	1.5989
    Rental income of persons with capital consumption adjustment	0.6921
    Corporate profits with inventory valuation and capital consumption adjustments, domestic industries	1.8544
      Taxes on corporate income	0.3022
      Profits after tax with inventory valuation and capital consumption adjustments	1.5522
        Net dividends	0.9201
        Undistributed corporate profits with inventory valuation and capital consumption adjustments	0.6321
  Current surplus of government enterprises\1\	-0.0133
Consumption of fixed capital	3.4356
  Private	2.8486
  Government	0.5869
'''