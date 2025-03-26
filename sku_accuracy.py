# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 2025

@author: Victor Diogho Heuer de Carvalho
@instituition: Federal University of Alagoas
@email: victor.carvalho@delmiro.ufal.br

This script plots monthly data related to SKU Accuracies, 
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
accuracies = [0.9999, 0.9998, 0.9999, 0.9999, 0.9998, 0.9997, 0.9995, 1.0000, 0.9999, 0.9997, 0.9994, 0.9999]

months = ['Jan/2022', 'Feb/2022', 'Mar/2022', 'Apr/2022', 'May/2022', 'Jun/2022']
accuracies= [0.9995, 0.9998, 0.9994, 0.9997, 0.9997, 0.9995]
'''
months = ['Jan/2021', 'Feb/2021', 'Mar/2021', 'Apr/2021', 'May/2021', 
        'Jun/2021', 'Jul/2021', 'Aug/2021', 'Sep/2021', 'Oct/2021', 
        'Nov/2021', 'Dec/2021', 'Jan/2022', 'Feb/2022', 'Mar/2022',
        'Apr/2022', 'May/2022', 'Jun/2022']

accuracies = [0.9999, 0.9998, 0.9999, 0.9999, 0.9998, 0.9997, 
             0.9995, 1.0000, 0.9999, 0.9997, 0.9994, 0.9999,
             0.9995, 0.9998, 0.9994, 0.9997, 0.9997, 0.9995]

# Calculate the trendline equation
z = np.polyfit(range(len(months)), accuracies, 1)
p = np.poly1d(z)

# Prints the slope of the trendline
slope = z[0]
print(f'Inclinação da linha de tendência: {slope:.2e}')

# Plot of monthly accuracies
plt.figure(figsize=(10, 6))
plt.plot(months, accuracies, marker='o', label='Accuracies')
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.grid(True)

# Average accuracy line
avarage_accuracy = np.mean(accuracies)
plt.axhline(y=avarage_accuracy, color='black', linestyle='--', label='Average Accuracy')

# Add trendline to chart
plt.plot(months, p(range(len(months))), color='red', linestyle='-.', label='Tendency line')

# Saving the legend
legend = plt.legend()

# X-axis tick rotation
plt.xticks(rotation = 90)

# Saving PNG
file_name = "SKU_Accuracies.png"
plt.savefig(file_name, format='png', dpi=300, bbox_inches='tight', bbox_extra_artists=[legend])
print(f"File saved in: {os.path.abspath(file_name)}")

#Showing Graphs
plt.legend()
plt.show()