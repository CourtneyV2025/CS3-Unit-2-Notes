import matplotlib.pyplot as plt 
import numpy as np

# Set style for charts 
plt.style.use('seaborn-v0_8-pastel') 
print(plt.style.available)

# Create sample set of data 
# Remember that X is for the independent variable 
x_vals = np.linspace(0, 10, 100)

# LINE PLOTS are good when graphing functions
plt.plot(x_vals, np.sin(x_vals))
plt.plot(x_vals, np.cos(x_vals)) 

# Show figure in the IDE
# plt.show() 

# Save figure as PNG in current directory 
plt.savefig('lineplots.png')

# Alternatively, set up a Figure OBJECT for the plot
fig = plt.figure()
ax = plt.axes() 

# Plot a function on the Axes object instance 
ax.plot(x_vals, 2*(x_vals), color='pink')

fig.savefig('lineplot2.png')


