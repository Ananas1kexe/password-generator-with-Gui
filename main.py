import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
import string

def generate():
    try:
        length = int(entry.get())
        
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        label.config(text=f'Your password: {password}')
        
    except ValueError:
        label.config(text='Please enter a vaild number')

window = tk.Tk()
window.geometry("300x400")
window.title('Password generate')


text = tk.Label(window, text='Enter number of password')
text.pack()

entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)



btn = ttk.Button(text="Generate", command=generate)
btn.pack(anchor=NW, padx=6, pady=6)

label = ttk.Label(window, text='')
label.pack(anchor=NW, padx=6, pady=6)



window.mainloop()