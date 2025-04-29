import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
fc = 3.5e9 
c = 3e8    
lambda_c = c / fc  
num_samples = 10000  

mean_delay_spread = 100e-9  
std_delay_spread = 30e-9  

delay_spread_samples = np.random.normal(mean_delay_spread, std_delay_spread, num_samples)

delay_spread_samples = np.clip(delay_spread_samples, 0, None)

plt.figure()
plt.hist(delay_spread_samples * 1e9, bins=50, edgecolor='black')
plt.title('Delay Spread UMi NLoS (3.5 GHz)')
plt.xlabel('Delay Spread (ns)')
plt.ylabel('Número de Amostras')
plt.grid(True)
plt.savefig('graficos/histograma_delay_spread.png')
plt.show()

