import psutil as pu
print(pu.cpu_count(logical=True))