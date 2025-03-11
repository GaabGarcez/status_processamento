import psutil
import time

while True:
    cpu_usage = psutil.cpu_percent(interval=1)  # Percentual de uso da CPU
    ram_usage = psutil.virtual_memory().percent  # Percentual de uso da RAM
    
    print(f"Percentual CPU: {cpu_usage}%")
    print(f"Percentual de RAM: {ram_usage}%")
    
    time.sleep(2)  # Atualiza a cada 0.5 segundo
