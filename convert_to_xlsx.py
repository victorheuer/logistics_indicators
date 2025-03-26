# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 2025

@author: Victor Diogho Heuer de Carvalho
@instituition: Federal University of Alagoas
@email: victor.carvalho@delmiro.ufal.br

This script converts all monthly data to a xlsx file.
"""

import pandas as pd

months = ['Jan/2021', 'Feb/2021', 'Mar/2021', 'Apr/2021', 'May/2021', 
         'Jun/2021', 'Jul/2021', 'Aug/2021', 'Sep/2021', 'Oct/2021', 
         'Nov/2021', 'Dec/2021', 'Jan/2022', 'Feb/2022', 'Mar/2022',
         'Apr/2022', 'May/2022', 'Jun/2022']

accuracy = [0.9999, 0.9998, 0.9999, 0.9999, 0.9998, 0.9997, 
             0.9995, 1.0000, 0.9999, 0.9997, 0.9994, 0.9999,
             0.9995, 0.9998, 0.9994, 0.9997, 0.9997, 0.9995]

otd = [0.65, 0.60, 0.60, 0.58, 0.62, 0.63, 
       0.60, 0.74, 0.64, 0.62, 0.68, 0.68,
       0.72, 0.61, 0.63, 0.61, 0.68, 0.61]

otif = [0.53, 0.47, 0.44, 0.52, 0.54, 0.56, 
        0.52, 0.67, 0.59, 0.56, 0.63, 0.62,
        0.64, 0.58, 0.62, 0.60, 0.66, 0.52]

# Create a pandas DataFrame with the data from the lists
df = pd.DataFrame({
    'Month': months,
    'Accuracy': accuracy,
    'OTD': otd,
    'OTIF': otif
})

# Save the DataFrame to an XLSX file
df.to_excel('all_data.xlsx', index=False)
print("File created successfully!")