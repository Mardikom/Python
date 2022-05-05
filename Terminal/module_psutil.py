


import psutil as pu

# print(pu.cpu_count())
# print(pu.cpu_percent(percpu=True))
# print(pu.virtual_memory())
# print(pu.virtual_memory()[0]/(1024*1024))
# print(pu.sensors_battery())
# ДЗ: разобрать еще как минимум 4 любые функции модуля

print("\033[1;32;40mSwap memory:", pu.swap_memory()[0]/(1024*1024))# показывает сколько памяти в свапе
print("Users:", pu.users()[0][0])# показывает пользователей
for x in pu.disk_partitions():
    print(x)
print("Drive format: ", pu.disk_partitions()[0][2])# показывает инфу про накопитель
print("SSD speed: ",  pu.disk_io_counters()[4]/(1024*1024)) # показывает скорость скорость и количество записаных/прочитаных мб