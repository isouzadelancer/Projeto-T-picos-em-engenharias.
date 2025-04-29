rng(42);

% Constantes físicas
fc = 3e9;  % Frequência da portadora (3 GHz)
c = 3e8;   % Velocidade da luz (m/s)
lambda_c = c / fc;  % Comprimento de onda (m)

% Número de amostras
num_samples = 10000;

% Parâmetros do espalhamento de atraso
mean_delay_spread = 100e-9;  % Média (100 ns)
std_delay_spread = 30e-9;    % Desvio padrão (30 ns)

% Geração do delay spread com distribuição normal
delay_spread_samples = mean_delay_spread + std_delay_spread * randn(num_samples,1);

% Evitar atrasos negativos
delay_spread_samples = max(delay_spread_samples, 0);

% Plot do histograma do delay spread
figure;
histogram(delay_spread_samples * 1e9, 50, 'EdgeColor', 'black');
title('Delay Spread UMi NLoS (3 GHz)');
xlabel('Delay Spread (ns)');
ylabel('Número de Amostras');
grid on;

% Verificar se a pasta graficos existe e salvar
if ~exist('graficos', 'dir')
   mkdir('graficos')
end
saveas(gcf, 'graficos/histograma_delay_spread_matlab.png');
