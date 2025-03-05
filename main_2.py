import psutil
import time
import GPUtil

while True:
    cpu_usage = psutil.cpu_percent(interval=1)  # Percentual de uso da CPU
    ram_usage = psutil.virtual_memory().percent  # Percentual de uso da RAM
    
    # Obtendo informações das GPUs
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        gpu_usage = gpu.load * 100  # gpu.load retorna um valor entre 0 e 1
        print(f"GPU {gpu.id} - Uso: {gpu_usage:.2f}%")
    
    print(f"Percentual CPU: {cpu_usage}%")
    print(f"Percentual de RAM: {ram_usage}%")
    
    time.sleep(0.5)  # Atualiza a cada 0.5 segundo
