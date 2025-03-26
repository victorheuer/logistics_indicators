# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 2025

@author: Victor Diogho Heuer de Carvalho
@instituition: Federal University of Alagoas
@email: victor.carvalho@delmiro.ufal.br

This script contains a function to ccalculate 
metrics avarages.
"""

def calculate_avarage(list_):
  """Calculates the average of a list of numbers."""

  if not list_:  # Check if the list is empty
    return 0  # Returns 0 if the list is empty

  sum_ = sum(list_)
  avarage = sum_ / len(list_)
  return avarage

# Numbers lists
accuracies = [0.9999, 0.9998, 0.9999, 0.9999, 0.9998, 0.9997, 
            0.9995, 1.0000, 0.9999, 0.9997, 0.9994, 0.9999,
            0.9995, 0.9998, 0.9994, 0.9997, 0.9997, 0.9995]

otd = [0.65, 0.60, 0.60, 0.58, 0.62, 0.63, 
       0.60, 0.74, 0.64, 0.62, 0.68, 0.68,
       0.72, 0.61, 0.63, 0.61, 0.68, 0.61]

otif = [0.53, 0.47, 0.44, 0.52, 0.54, 0.56, 
        0.52, 0.67, 0.59, 0.56, 0.63, 0.62,
        0.64, 0.58, 0.62, 0.60, 0.66, 0.52]

# Calculating avarages
avarage_acu = calculate_avarage(accuracies)
avarage_otd = calculate_avarage(otd)
avarage_otif = calculate_avarage(otif)

# Printing Results
print(f"Accuracies Avarage: {avarage_acu}")
print(f"OTD  Avarage: {avarage_otd}")
print(f"OTIF Avarage: {avarage_otif}")