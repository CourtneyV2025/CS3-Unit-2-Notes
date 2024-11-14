import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import numpy as np  

sns.set_theme(style='white', palette='pastel') # seaborn's method to set its chart style 
# style:
# palette: deep, muted, bright, pastel, dark, colorblind 

# Matplotlib histogram 
# histograms show distribution of values
data = np.random.multivariate_normal([0, 0], [[5, 2], [2,2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])
for col in 'xy':
    plt.hist(data[col], density=True, alpha=0.5) 
plt.savefig('hist.png', bbox_inches='tight') 
plt.close()  

# KDE (kernal density estimation) gives a SMOOTH estimate 
# of distribution of values  
sns.kdeplot(data=data, fill=True); 
plt.savefig('sns-kdeplot.png', bbox_inches='tight')
plt.close()

# Load a built-in dataset 
iris = sns.load_dataset('iris')
print(iris.head()) 

# PAIR PLOT: visualize multi-dimensional data 
sns.pairplot(iris, hue='species', height=2.5) 
plt.savefig('sns-pairplot.png', bbox_inches='tight')
plt.close()

# Load another dataset
tips = sns.load_dataset('tips')
print(tips.head())
tips['tip_percent'] = 100 * tips['tip'] / tips['total_bill']
#FACET GRID: compare multiple dimensions
grid = sns.FacetGrid(tips, row='sex', col='time', margin_titles=True)
grid.map(plt.hist, "tip_percent", bins=np.linspace(0, 40, 15));
plt.savefig('sns-facetgrid.png', bbox_inches='tight')
plt.close()  

# CATEGORIAL PLOT: look at distrubution of parameter with bins defined by another paramete 
sns.catplot(x='day', y='total_bill', hue='sex', data=tips, kind='box')
plt.savefig('sns-catplot.png', bbox_inches='tight')
plt.close() 

sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
plt.savefig('sns-jointplot.png', bbox_inches='tight')
plt.close()  
