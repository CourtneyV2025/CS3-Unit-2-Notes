import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('seaborn-v0_8-pastel') 

# Generate data
rng = np.random.default_rng(50)
data = rng.normal(size=1000)

# HISTOGRAM shows FREQUENCY 
plt.hist(data)

plt.savefig('histogram.png') 
plt.close()

plt.hist(data, bins=30, density=True, alpha=0.5,
         histtype='stepfilled', color='pink',
         edgecolor='none');
plt.savefig('hist-custom.png')
plt.close() 

# HEXAGONAL binnings 
mean = [0,0] 
cov = [[1,1], [1,2]]
x, y = rng.multivariate_normal(mean, cov, 10000).T 
plt.hexbin(x, y, gridsize=1) 
cb = plt.colorbar(label='count in bin') 
plt.savefig('hexbin.png')




