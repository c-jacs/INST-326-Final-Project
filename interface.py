import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Enter a song you like: ")
entry = tk.Entry()
greeting.pack()
entry.pack()

song = entry.get()

window.mainloop()
