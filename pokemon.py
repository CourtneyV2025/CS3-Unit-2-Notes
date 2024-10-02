import numpy as np 
import pandas as pd 

# Load CSV file data into DataFrame 
pokemon = pd.read_csv('pokemon_data.csv')

print(pokemon) # displays first 5 rows and last 5 rows 
print(pokemon.columns) # see column labels

# Access one column (Series) of data
print(pokemon ['Type 1']) 
# Shorthand way of referencing a column 
print(pokemon.HP) 

# Create new column for Attack/Sp. Atk ratio
pokemon['Attack Ratio'] = pokemon['Attack'] / pokemon['Sp. Atk'] 
print(pokemon['Attack Ratio'])

# You can replace the standard indices (0...end)
# with strings from one column! 
poke = pokemon.set_index('Name') 

# Access a specific "cell" (ROW, COL)
print(poke.loc['Pikachu', 'Type 1']) 

# Access a range of ROWS 
print(poke.loc[['Bulbasaur', 'Squirtle', 'Charmander']])

# If you want to print every row in a certain way 
for  index, row in poke.iterrows():
    print(index, "-", row['Type 1'])
