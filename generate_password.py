import random
import tkinter as tk
def generate_password(symbols=6):
    symbols_list = []
    for i in range(symbols):
        num = random.randint(1, 3)
        if num == 1:
            symbols_list.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        elif num == 2:
            symbols_list.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        elif num == 3:
            symbols_list.append(random.choice('0123456789'))
    password = ''.join(str(symb) for symb in symbols_list)
    text.delete(0, tk.END)
    text.insert(tk.END, password)
number_of_symbols = 8
win = tk.Tk()
win.title('Password')
win.geometry('1200x1000')
win.config(bg = 'black')
text = tk.Entry(font = ('arial', 150, 'bold'), width = number_of_symbols + 1, bg = 'black', fg = 'white', borderwidth = 15)
text.pack(expand = 1)
button = tk.Button(win, text = 'Generate', height = 1, width = 10, bg = 'black', fg = 'red', font = ('arial', 100, 'bold'), borderwidth = 0, command = lambda: generate_password(number_of_symbols))
button.pack(expand = 1)
# button = tk.Button('<Button-1>', )
win.mainloop()