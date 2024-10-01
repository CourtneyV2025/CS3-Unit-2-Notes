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
cookies_dict = {'double chocolate': 5,
                'chocolate chip': 10, 
                'oatmeal raisin': 10,
                'snickerdoodle': 0, 
                } 
cookies = pd.Series(cookies_dict)
print(cookies) # Dict keys become indices of the Series
# Access item by index 
print("Rating of snickerdoodle cookies: ", cookies['snickerdoodle'])

# DataFrame is like a 2D array or specialized dictionary 
cookies_df = pd.DataFrame(cookies, columns=['rating'])
print(cookies_df) 
print()
# Add a column to our DataFrame 
cookies_df['allergens'] = [True, True, True, False] 
print(cookies_df) 

# Another way to add a column 
cookies_df['sweetness'] = { 'double chocolate': 10,
                  'chocolate chip': 8,
                  'oatmeal raisin': 6,
                  'snickerdoodle': 7,
                  'gingerbread': 8 }
print(cookies_df)

# *** DATA SELECTION ***
data = pd.Series(['C', 'O', 'C', 'O'], index=[0, 6, 7, 27])

# Indexing uses the explicit index 
print(data[27]) 

print(data[6:27]) # not getting expected output 

# Instead, use the LOC attribute to get a slice that uses explicit indices 
print(data.loc[6:27]) # includes item at index 27 too!c

# Not as common, iLOC uses implicit indices 
print(data.iloc[0:6]) # doesn't include second item 