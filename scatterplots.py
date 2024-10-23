import matplotlib.pyplot as plt 
import numpy as np 
from sklearn.datasets import load_iris



plt.style.use('seaborn-v0_8-pastel')

# Generate data points
rng = np.random.default_rng(0)
x = rng.normal(size=100)
y = rng.normal(size=100)
colors = rng.random(100)
sizes = 1000 * rng.random(100)

# Scatterplot functions
# alpha sets the opacity of the point
plt.scatter(x, y, c=colors, s=sizes, alpha=0.3)
plt.colorbar(); # show color scale

# Save figure 
plt.savefig('scatterplot.png') 
plt.close()

# Scatterplot from Iris data 
iris = load_iris()
features = iris.data.T # Transposes the data (switch) 
plt.scatter(features[0], features[1], alpha=0.4,
            s=100*features[3], c=iris.target, cmap='viridis') 
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.colorbar()
plt.savefig('iris-scatter.png') 

# 4 different properties observed 
# 1. length (position on x axis)
# 2. width (position on the yaxis) 
# 3. petal width (dot size) 
# 4. species (color)