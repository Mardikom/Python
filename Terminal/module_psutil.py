import psutil

import psutil as pu

print(pu.cpu_count())
print(pu.cpu_percent(percpu=True))
print(pu.virtual_memory())
print(pu.virtual_memory()[0]/(1024*1024))
print(pu.sensors_battery())
# ДЗ: разобрать еще как минимум 4 любые функции модуля

