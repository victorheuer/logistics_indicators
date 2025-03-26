# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 2025

@author: Victor Diogho Heuer de Carvalho
@instituition: Federal University of Alagoas
@email: victor.carvalho@delmiro.ufal.br

This script converts monthly data to a xlsx file.
"""

import pandas as pd

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
tolerancies = [0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015, 0.015]
divergences_19 = [-0.04, 0.01, 0.07, -0.0002, 0.02, -0.0002, 0.01, 0.01, -0.01, 0.01, 0.01, -0.003]
divergences_20 = [0.01, -0.001, 0.002, -0.01, -0.01, 0.0004, -0.01, -0.008, 0.02, 0.01, -0.003, 0.01]
divergences_21 = [0.007, 0.008, 0.01, 0.01, 0.012, 0.01, 0.006, 0.001, 0.009, 0.005, 0.001, 0.006]

# Criar um DataFrame do pandas
df = pd.DataFrame({
    'Months': months,
    'Tolerances': tolerancies,
    'Div. 2019': divergences_19,
    'Div. 2020': divergences_20,
    'Div. 2021': divergences_21
})

# Salvar o DataFrame em um arquivo XLSX
df.to_excel('data_months_accuracy_divergences.xlsx', index=False)
print("file created successfully!")