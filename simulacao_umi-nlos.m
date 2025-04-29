rng(42);
fc = 3.5e9;
c = 3e8; % Velocidade da luz
lambda_c = c / fc;
num_samples = 10000; 

mean_delay_spread = 100e-9; 
std_delay_spread = 30e-9;   


delay_spread_samples = mean_delay_spread + std_delay_spread * randn(num_samples,1);


delay_spread_samples = max(delay_spread_samples, 0);


figure;
histogram(delay_spread_samples * 1e9, 50, 'EdgeColor', 'black');
title('Delay Spread UMi NLoS (3.5 GHz)');
xlabel('Delay Spread (ns)');
ylabel('Número de Amostras');
grid on;

if ~exist('graficos', 'dir')
   mkdir('graficos')
end
saveas(gcf, 'graficos/histograma_delay_spread_matlab.png');
