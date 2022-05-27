import tkinter as t
from tkinter import ttk
import psutil as pu

win = t.Tk()
win.title("CPU and RAM info")
win.resizable(False, False)

def start():
    destroy_all()
    win.geometry("350x300")
    set_menu()
    section2_interface()
    section3_interface()
    cpu_ram_proccess()

################################################################################
# MENU FUNCTIONS

def hide():
    win.bind_class('Tk',"<Enter>", show_win)
    win.bind_class('Tk',"<Leave>", hide_win)

def notHide():
    win.geometry("350x300")
    win.unbind_class('Tk',"<Enter>")
    win.unbind_class('Tk',"<Leave>")


def hide_win(event):
    print(event,event.widget)
    win.geometry("350x2")

def show_win(event):
    print(event,event.widget)
    win.geometry("350x300")

def fixWin():
    if win.attributes("-alpha") == 1:
        win.attributes("-alpha", 0.5)
        win.attributes("-topmost", 1)
    elif win.attributes("-alpha") != 1:
        win.attributes("-alpha", 1)
        win.attributes("-topmost", 0)


################################################################################
# DESTROY ALL WIDGETS FUNCTION
def destroy_all():
    for x in win.winfo_children():
        x.destroy()
    
################################################################################
# MENU

def set_menu():
    menu = t.Menu(win)
    mode_menu = t.Menu(menu,tearoff=0)

    menu.add_cascade(label="Mode", menu=mode_menu)

    menu.add_command(label= 'Fixed', command=fixWin)

    mode_menu.add_command(label="Hide", command = hide)
    mode_menu.add_command(label="Not hide", command = notHide)
    mode_menu.add_command(label="Minimal", command = set_minimal_win)

    win.config(menu = menu)

################################################################################
# SECTION 2

def section2_interface():
    global progressbars, progressbarsLabels
    frame2 = ttk.Frame(win)
    win.columnconfigure(0,minsize=270)

    cpuInfoLabel = ttk.Label(frame2, text="CPU INFO:")
    cpuInfoLabel.grid(row=0, column=0)

    progressbars = []
    progressbarsLabels = []

    for x in range(pu.cpu_count(logical=True)):
        progressbars.append(ttk.Progressbar(frame2, value = 45, length=5))
        progressbarsLabels.append(ttk.Label(frame2))
    for index, bar in enumerate(progressbars):
        bar.grid(row = index+1, column = 0, stick = 'we')
        progressbarsLabels[index].grid(row = index+1, column = 1, padx = 12)
    frame2.grid(row=1, column=0, padx=15,sticky='we')
    frame2.columnconfigure(0,minsize=270)


################################################################################
# SECTION 3
def section3_interface():
    global ramProgressbar, totalMemoryLabel, avaliableMemoryLabel, usedMemoryLabel, memoryLabel
    frame3 = ttk.Frame(win)
    win.columnconfigure(1,minsize=270)

    ramInfoLabel = ttk.Label(frame3, text="RAM INFO:")
    ramProgressbar = ttk.Progressbar(frame3, value = 45, length=5)
    memoryLabel = ttk.Label(frame3)
    totalMemoryLabel = ttk.Label(frame3)
    avaliableMemoryLabel = ttk.Label(frame3)
    usedMemoryLabel = ttk.Label(frame3)

    ramInfoLabel.grid(row=0, column=0)
    ramProgressbar.grid(row = 1, column = 0, stick = 'we')
    memoryLabel.grid(row = 1, column = 1, padx = 12)
    totalMemoryLabel.grid(row = 2, column = 0)
    avaliableMemoryLabel.grid(row = 4, column = 0)
    usedMemoryLabel.grid(row = 3, column = 0)
    frame3.grid(row=2, column=0, padx=15,sticky='we')
    frame3.columnconfigure(0,minsize=270)
   


################################################################################
# Recursion function

def cpu_ram_proccess():
    global recursion
    memory = pu.virtual_memory()
    cores = pu.cpu_percent(percpu=True)
    for index, core in enumerate(cores):
        progressbars[index].config(value = core)
        progressbarsLabels[index].config(text=f"{core}%")
    totalMemoryLabel.config(text=f"Total memory: {memory.total / (1024*1024)} MB")
    avaliableMemoryLabel.config(text=f"Avaliable memory: {round(memory.available / (1024*1024),1)} MB")
    usedMemoryLabel.config(text=f"Used memory: {round(memory.used / (1024*1024),1)} MB")
    ramProgressbar.config(value = memory.percent)
    memoryLabel.config(text=f"{memory.percent}%")
    recursion = win.after(1000, cpu_ram_proccess)
    

################################################################################
# MINIMAL WIN
def set_minimal_win():
    global ramInfoLabel, ramProgressbar, memoryLabel, cpuInfoLabel
    
    win.after_cancel(recursion)
    destroy_all()

    win.geometry("540x60")

    set_menuMinimal()

    ramInfoLabel = ttk.Label(text="RAM INFO:")
    ramInfoLabel.grid(row=0, column=0)
    ramProgressbar = ttk.Progressbar(value = 45, length=5)
    ramProgressbar.grid(row = 1, column = 0, stick = 'we')
    cpuInfoLabel = ttk.Label(text="CPU INFO:")
    cpuInfoLabel.grid(row=0, column=1)
    cpuProgressbar = ttk.Progressbar(value = 45, length=5)
    cpuProgressbar.grid(row = 1, column = 1, stick = 'we')

    cpu_ram_proccess_min()

def mainWin():
    win.after_cancel(recursion)
    start()


def set_menuMinimal():
    menuMinimal = t.Menu(win)
    
    menuMinimal.add_command(label= 'Main Win', command=mainWin)
    menuMinimal.add_command(label= 'Fixed', command=fixWin)

    win.config(menu = menuMinimal)

def cpu_ram_proccess_min():
    global recursion
    memory = pu.virtual_memory()
    ramProgressbar.config(value = memory.percent)
    ramInfoLabel.config(text=f"RAM:{memory.percent}%")
    cpuInfoLabel.config(text=f"CPU:{pu.cpu_percent()}%")
    recursion = win.after(1000, cpu_ram_proccess_min)


start()
win.mainloop()