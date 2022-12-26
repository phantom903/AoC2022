import tkinter as tk

window = tk.Tk()
window.rowconfigure([0, 1, 2, 3, 4, 5], minsize = 20)
window.columnconfigure([x for x in range(40)], minsize = 16)
label1 = tk.Label(text = '', bg = 'black', fg = 'white')
label1.grid(row = 0, column = 0, sticky = 'nsew')
window.mainloop()