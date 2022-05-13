import tkinter as t
from tkinter import ttk
import psutil as pu
win = t.Tk()
menu = t.Menu(win)
win.geometry("350x300")
win.config(menu = menu)
win.title("CPU and RAM info")
# print(win.bindtags())
# MENU FUNCTIONS

def hide():
    win.bind_class('Tk',"<Enter>", show_win)
    win.bind_class('Tk',"<Leave>", hide_win)

def hide_win(event):
    print(event,event.widget)
    win.geometry("350x0")

def show_win(event):
    print(event,event.widget)
    win.geometry("350x300")

def fixWin():
    if win.attributes("-alpha") == 1:
        win.attributes("-alpha", 0.9)
        win.attributes("-topmost", 1)
    elif win.attributes("-alpha") != 1:
        win.attributes("-alpha", 1)
        win.attributes("-topmost", 0)
        
################################################################################
# MENU

mode_menu = t.Menu(menu)
fixed_menu = t.Menu(menu)

menu.add_cascade(label="Mode", menu=mode_menu)

mode_menu.add_command(label="Hide", command = hide)
mode_menu.add_command(label="Not hide", command = None)
mode_menu.add_command(label="Minimal", command = None)
mode_menu.add_command(label="Fixed", command = fixWin)





################################################################################
# SECTION 1
'''
frame1 = ttk.Frame(win)

button_exit  = ttk.Button(frame1, text = "Exit")
box = ttk.Combobox(frame1,values=["Hide", "Not hide", "Minimal"], state='readonly')
box.current(1)

buttonFixed = ttk.Button(frame1, text="Fixed")


button_exit.grid(row=0,column=0, columnspan=2)
box.grid(row=1, column=0) 
buttonFixed.grid(row=1, column=1)
'''

################################################################################
# SECTION 2

frame2 = ttk.Frame(win)
win.columnconfigure(0,minsize=270)

cpuInfoLabel = ttk.Label(frame2, text="CPU INFO:")
cpuInfoLabel.grid(row=0, column=0)

progressbars = []
progressbarsLabels = []
def bars_interface():
    for x in range(8):
        progressbars.append(ttk.Progressbar(frame2, value = 45, length=5))
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

################################################################################
# SECTION 3

frame3 = ttk.Frame(win)

ramInfoLabel = ttk.Label(frame3, text="RAM INFO:")
ramProgressbar = ttk.Progressbar(frame3, value = 45)
memoryLabel = ttk.Label(frame3)
totalMemoryLabel = ttk.Label(frame3)
avaliableMemoryLabel = ttk.Label(frame3)
usedMemoryLabel = ttk.Label(frame3)

ramInfoLabel.grid(row=9, column=0)
ramProgressbar.grid(row = 10, column = 0, stick = 'we')
memoryLabel.grid(row = 10, column = 1, padx = 12)
totalMemoryLabel.grid(row = 11, column = 0,sticky='w')
avaliableMemoryLabel.grid(row = 12, column = 0,sticky='w')
usedMemoryLabel.grid(row = 13, column = 0,sticky='w')


def bar_config_ram():
    memory = pu.virtual_memory()
    totalMemoryLabel.config(text=f"Total memory: {memory.total / (1024*1024)} MB")
    avaliableMemoryLabel.config(text=f"Avaliable memory: {round(memory.available / (1024*1024),1)} MB")
    usedMemoryLabel.config(text=f"Used memory: {round(memory.used / (1024*1024),1)} MB")
    ramProgressbar.config(value = memory.percent)
    memoryLabel.config(text=f"{memory.percent}%")
    win.after(1000, bar_config_ram)
    
bar_config_ram()

################################################################################
# FRAMES CONFIGURATION

#frame1.grid(row=0, column=0, padx=15, pady=15,sticky='we')
frame3.grid(row=2, column=0, padx=15,sticky='we')
frame2.grid(row=1, column=0, padx=15,sticky='we')
#frame1.columnconfigure(0,minsize=270)
frame2.columnconfigure(0,minsize=270)
frame3.columnconfigure(0,minsize=270)

win.mainloop()