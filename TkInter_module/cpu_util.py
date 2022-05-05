from calendar import c
from ipaddress import collapse_addresses
import tkinter as t
from tkinter import ttk
import psutil as pu

win = t.Tk()
win.geometry("500x500")

progressbars = []

cpuInfoLabel = ttk.Label(text="CPU INFO:")
cpuInfoLabel.grid(row=0, column=0)

cpuTotalLabel = ttk.Label(text="TOTAL:")
cpuTotalLabel.grid(row=0, column=1, )

def bars_interface():
    for x in range(8):
        progressbars.append(ttk.Progressbar(value = 45, length=200))

    for index, bar in enumerate(progressbars):
        bar.grid(row = index+1, column = 0)

def bars_config_cpu():
    cores = pu.cpu_percent(percpu=True)

    for index, core in enumerate(cores):
        progressbars[index].config(value = core)

    win.after(1000, bars_config_cpu)



bars_interface()
bars_config_cpu()
print(progressbars)




win.mainloop()










# ДЗ: Сделть секцию сpu