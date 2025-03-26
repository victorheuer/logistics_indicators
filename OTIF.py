# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 2025

@author: Victor Diogho Heuer de Carvalho
@instituition: Federal University of Alagoas
@email: victor.carvalho@delmiro.ufal.br

This script plots monthly data related to OTIFs, 
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
otif = [0.53, 0.47, 0.44, 0.52, 0.54, 0.56, 0.52, 0.67, 0.59, 0.56, 0.63, 0.62]

months = ['Jan/2022', 'Feb/2022', 'Mar/2022', 'Apr/2022', 'May/2022', 'Jun/2022']
otif = [0.64, 0.58, 0.62, 0.60, 0.66, 0.52]
'''
months = ['Jan/2021', 'Feb/2021', 'Mar/2021', 'Apr/2021', 'May/2021', 
        'Jun/2021', 'Jul/2021', 'Aug/2021', 'Sep/2021', 'Oct/2021', 
        'Nov/2021', 'Dec/2021', 'Jan/2022', 'Feb/2022', 'Mar/2022',
        'Apr/2022', 'May/2022', 'Jun/2022']
otif = [0.53, 0.47, 0.44, 0.52, 0.54, 0.56, 
        0.52, 0.67, 0.59, 0.56, 0.63, 0.62,
        0.64, 0.58, 0.62, 0.60, 0.66, 0.52]

# Calculate the trendline equation
z = np.polyfit(range(len(months)), otif, 1)
p = np.poly1d(z)

# Prints the slope of the trendline
slope = z[0]
print(f'Inclinação da linha de tendência: {slope:.2e}')

# Plot of monthly OTIFs
plt.figure(figsize=(10, 6))
plt.plot(months, otif, marker='o', label='On time in full')
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.grid(True)

# Average line of OTIFs
avarage_otif = np.mean(otif)
plt.axhline(y=avarage_otif, color='black', linestyle='--', label='Average On time in full')

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