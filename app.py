#boggle matrix analysis main app

import tkinter as tk

def init_board():
    master = tk.Tk()
    
    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e4 = tk.Entry(master)
    e5 = tk.Entry(master)
    e6 = tk.Entry(master)
    e7 = tk.Entry(master)
    e8 = tk.Entry(master)
    e9 = tk.Entry(master)

    e1.grid(row=0, column=0)
    e2.grid(row=0, column=1)
    e3.grid(row=0, column=2)

    e4.grid(row=1, column=0)
    e5.grid(row=1, column=1)
    e6.grid(row=1, column=2)

    e7.grid(row=2, column=0)
    e8.grid(row=2, column=1)
    e9.grid(row=2, column=2)

    tk.mainloop()

init_board()
