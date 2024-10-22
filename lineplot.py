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

# LINEPLOT TWO

# Plot a function on the Axes object instance 
ax.plot(x_vals, 2*(x_vals), color='pink')
ax.plot(x_vals, 3*(x_vals),linestyle='dashed')
ax.plot(x_vals, 4*(x_vals), linestyle='dashdot')
ax.plot(x_vals, 5*(x_vals), linestyle='dotted') 

# You can use shortcuts to define color & style
ax.plot(x_vals, 1.5*(x_vals), ':')

# Save figure as PNG in current directory
fig.savefig('lineplot2.png')
plt.close()

# LINEPLOT THREE

# Demo in customization 
plt.plot(x_vals, np.sin(x_vals), '-.m', label='sin(x)')
plt.xlim(-1,11)
plt.ylim(-1.5, 1.5) 
# Set axis to tight to fit your plot better
plt.axis('tight')
# other options: 'equal', 'image', etc.
# Add TITLES/LABELS
plt.title('A Sine Wave') 
plt.xlabel('x')
plt.ylabel('sin(x)')

# Add LEGEND
plt.legend()
plt.savefig('lineplot3.png')
