# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 2025

@author: Victor Diogho Heuer de Carvalho
@instituition: Federal University of Alagoas
@email: victor.carvalho@delmiro.ufal.br

This script plots monthly data related to OTDs, 
calculates the trends and plots trendlines.
"""

import matplotlib.pyplot as plt
import numpy as np
import os

# Data
'''
months = ['Jan/2021', 'Feb/2021', 'Mar/2021', 'Apr/2021', 'May/2021', 
        'Jun/2021', 'Jul/2021', 'Aug/2021', 'Sep/2021', 'Oct/2021', 
        'Nov/2021', 'Dec/2021']
otd = [0.65, 0.60, 0.60, 0.58, 0.62, 0.63, 0.60, 0.74, 0.64, 0.62, 0.68, 0.68]

months = ['Jan/2022', 'Feb/2022', 'Mar/2022', 'Apr/2022', 'May/2022', 'Jun/2022']
otd = [0.72, 0.61, 0.63, 0.61, 0.68, 0.61]
'''
months = ['Jan/2021', 'Feb/2021', 'Mar/2021', 'Apr/2021', 'May/2021', 
        'Jun/2021', 'Jul/2021', 'Aug/2021', 'Sep/2021', 'Oct/2021', 
        'Nov/2021', 'Dec/2021', 'Jan/2022', 'Feb/2022', 'Mar/2022',
        'Apr/2022', 'May/2022', 'Jun/2022']
otd = [0.65, 0.60, 0.60, 0.58, 0.62, 0.63, 
       0.60, 0.74, 0.64, 0.62, 0.68, 0.68,
       0.72, 0.61, 0.63, 0.61, 0.68, 0.61]

# Calculate the trendline equation
z = np.polyfit(range(len(months)), otd, 1)
p = np.poly1d(z)

# Prints the slope of the trendline
slope = z[0]
print(f'Trendline slope: {slope:.2e}')

# Plot of monthly OTDs
plt.figure(figsize=(10, 6))
plt.plot(months, otd, marker='o', label='On time delivery')
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.grid(True)

# Average OTDs line
avarage_otd = np.mean(otd)
plt.axhline(y=avarage_otd, color='black', linestyle='--', label='Average On time delivery')

# Add trendline to chart
plt.plot(months, p(range(len(months))), color='red', linestyle='-.', label='Tendency line')

# Saving the legend
legend = plt.legend()

# X-axis tick rotation
plt.xticks(rotation = 90)

# Saving PNG
file_name = "OTIFs.png"
plt.savefig(file_name, format='png', dpi=300, bbox_inches='tight', bbox_extra_artists=[legend])
print(f"File saved in: {os.path.abspath(file_name)}")

# Showing Graph
plt.legend()
plt.show()