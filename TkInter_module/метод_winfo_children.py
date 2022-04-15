import tkinter as t

win = t.Tk()

for x in range(10):
        for y in range(10):
            label = t.Label(width=6, height=3, bg="grey", relief= "ridge")
            label.grid(row=x, column=y)


for x in win.winfo_children():
    x.destroy()

print(widgets)
win.mainloop()