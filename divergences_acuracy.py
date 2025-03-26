# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 2025

@author: Victor Diogho Heuer de Carvalho
@instituition: Federal University of Alagoas
@email: victor.carvalho@delmiro.ufal.br

This script uses monthly data to plot divergence 
curves associated to stock accuracy metrics.
"""
import matplotlib.pyplot as plt
import os

# Data

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
tolerances = [0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015]
divergences_19 = [-0.04, 0.01, 0.07, -0.0002, 0.02, -0.0002, 0.01, 0.01, -0.01, 0.01, 0.01, -0.003]
divergences_20 = [0.01, -0.001, 0.002, -0.01, -0.01, 0.0004, -0.01, -0.008, 0.02, 0.01, -0.003, 0.01]
divergences_21 = [0.007, 0.008, 0.01, 0.01, 0.012, 0.01, 0.006, 0.001, 0.009, 0.005, 0.001, 0.006]


# Plotting curves
plt.figure(figsize=(10, 6))
plt.plot(months, tolerances, label = "Tolerance", color = 'black')
plt.plot(months, divergences_19, label='2019', color = 'red', linestyle=':', marker='*')
plt.plot(months, divergences_20, label='2020', color = 'blue', linestyle='--', marker='s')
plt.plot(months, divergences_21, label='2021', color = 'green', linestyle='-.', marker='^')


# Graph setup
plt.xlabel("")
plt.ylabel('Divergence (%)')
plt.title("")
plt.xticks(months)
plt.grid(True)
plt.legend()

# Saving PNG
file_name = "Divergences_Accuracy.png"
plt.savefig(file_name, format='png', dpi=300, bbox_inches='tight')
print(f"File saved in: {os.path.abspath(file_name)}")

# Showing Graph
plt.show()