
import tkinter as t
from tkinter import ttk
import psutil as pu

win = t.Tk()
win.geometry("500x500")
# cpu
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

#ram
ramInfoLabel = ttk.Label(text="RAM INFO:")
ramInfoLabel.grid(row=10, column=0)

ramTotalLabel = ttk.Label(text="TOTAL:")
ramTotalLabel.grid(row=10, column=1, )


#swap

swapInfoLabel = ttk.Label(text="SWAP INFO:")
swapInfoLabel.grid(row=12, column=0)

swapTotalLabel = ttk.Label(text="TOTAL:")
swapTotalLabel.grid(row=12, column=1, )


win.mainloop()










# ДЗ: Сделть секцию сpu