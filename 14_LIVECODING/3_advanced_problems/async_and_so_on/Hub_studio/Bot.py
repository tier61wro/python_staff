from tkinter import ttk
import tkinter as tk
import time




root = tk.Tk()

root.geometry('300x300+150+150')

def sleep_funk():
    time.sleep(5)
    lab['text'] = 'после сна'


btn = ttk.Button(root, text='Run', command=sleep_funk)
btn.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

lab = ttk.Label(root, text='текст для нажатия')
lab.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

root.mainloop()