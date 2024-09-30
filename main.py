# importing libraries "as" alias
import numpy as pd 
import pandas as pd 

# *** Pandas' SERIES OBJECT ***
# Series are 1D arrys of indexed data

# Create Series from a list/array
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data.values) # looks like a list
print(data.index) # range computed for indices
# Access Series data by index 
print("Getting one values from Series:", data[1])
print("Getting multiple values also shows indicies and data type:")
print(data[0:3]) 
print()
print()
# Series are like arrays but with EXPLICIT indexing 
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
print(data)

# Series are like arrays but with EXPLICIT indexing 
grades = pd.Series([9, 10, 11, 12], index = ['freshaman','sophmore', 'junior', 'senior'])
print(grades)
# Access Series date by index 
print("Seniors are in grade", grades['senior']) 

print()
# Can also create a Series from a dictionary 
cookies_dict = {'double choclate': 5,
                'chocolate chip': 10, 
                'oatmeal raisin': 10,
                'snickerdoodle': 0, 
                } 
cookies = pd.Series(cookies_dict)
print(cookies) # Dict keys become indices of the Series
# Access item by index 
print("Rating of snickerdoodle cookies: ", cookies['snickerdoodle'])