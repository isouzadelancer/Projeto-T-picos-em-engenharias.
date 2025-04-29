import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Constantes físicas
fc = 3e9  # Frequência da portadora (3 GHz)
c = 3e8   # Velocidade da luz (m/s)
lambda_c = c / fc  # Comprimento de onda (m)

# Número de amostras
num_samples = 10000

# Parâmetros de espalhamento de atraso
mean_delay_spread = 100e-9  # Média do delay spread (100 ns)
std_delay_spread = 30e-9    # Desvio padrão do delay spread (30 ns)

# Geração do delay spread com distribuição normal
delay_spread_samples = np.random.normal(mean_delay_spread, std_delay_spread, num_samples)
delay_spread_samples = np.clip(delay_spread_samples, 0, None)  # Garantir valores não negativos

# Plot do histograma do delay spread
plt.figure()
plt.hist(delay_spread_samples * 1e9, bins=50, edgecolor='black')
plt.title('Delay Spread UMi NLoS (3 GHz)')
plt.xlabel('Delay Spread (ns)')
plt.ylabel('Número de Amostras')
plt.grid(True)
plt.savefig('graficos/histograma_delay_spread.png')
plt.show()
