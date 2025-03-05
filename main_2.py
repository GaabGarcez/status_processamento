import psutil
import time
import pynvml

# Inicializa a NVML (NVIDIA Management Library)
pynvml.nvmlInit()
gpu_count = pynvml.nvmlDeviceGetCount()

while True:
    cpu_usage = psutil.cpu_percent(interval=1)  # Percentual de uso da CPU
    ram_usage = psutil.virtual_memory().percent  # Percentual de uso da RAM

    # Itera por cada GPU disponível
    for i in range(gpu_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        util = pynvml.nvmlDeviceGetUtilizationRates(handle)
        print(f"GPU {i} - Uso: {util.gpu}% - Memória: {util.memory}%")
    
    print(f"Percentual CPU: {cpu_usage}%")
    print(f"Percentual de RAM: {ram_usage}%")
    print('-' * 40)
    
    time.sleep(0.5)  # Atualiza a cada 0.5 segundo
