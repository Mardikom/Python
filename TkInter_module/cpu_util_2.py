
import tkinter as t
from tkinter import ttk
import psutil as pu
win = t.Tk()
win.geometry("500x500")


# SECTION 1
style = ttk.Style()
style.configure("TButton")



frame1 = ttk.Frame(win)

button_exit  = ttk.Button(frame1, text = "Exit")
box = ttk.Combobox(frame1, height = 12,values=["Hide", "Not hide", "Minimal"], state='readonly')
box.current(1)

buttonFixed = ttk.Button(frame1, text="Fixed")

frame1.pack()
button_exit.grid(row=0,column=0, columnspan=2, sticky="we")
box.grid(row=1, column=0, sticky="ns") 
buttonFixed.grid(row=1, column=1)

# SECTION 2

frame2 = ttk.Frame(win)
frame2.columnconfigure(0,minsize=270)

cpuInfoLabel = ttk.Label(frame2, text="CPU INFO:")
cpuTotalLabel = ttk.Label(frame2, text="TOTAL:")
cpuInfoLabel.grid(row=0, column=0)
cpuTotalLabel.grid(row=0, column=1)

progressbars = []
progressbarsLabels = []
def bars_interface():
    for x in range(8):
        progressbars.append(ttk.Progressbar(frame2, value = 45))
        progressbarsLabels.append(ttk.Label(frame2))
    for index, bar in enumerate(progressbars):
        bar.grid(row = index+1, column = 0, stick = 'we')
        progressbarsLabels[index].grid(row = index+1, column = 1, padx = 12)

def bars_config_cpu():
    cores = pu.cpu_percent(percpu=True)

    for index, core in enumerate(cores):
        progressbars[index].config(value = core)
        progressbarsLabels[index].config(text=f"{core}%")
    win.after(1000, bars_config_cpu)


bars_interface()
bars_config_cpu()
print(progressbars)


frame2.pack()

win.mainloop()