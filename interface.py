""""""
import tkinter as tk

def enter_song():
    """
    Creates a window with a text box for the user to enter a song they like,
    and saves that song to a variable to be used in the song recommendation program
    """
    window = tk.Tk()
    greeting = tk.Label(text="Enter a song you like: ")
    entry = tk.Entry()
    greeting.pack()
    entry.pack()

    song = entry.get()

    window.mainloop()
