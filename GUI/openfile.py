import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd  
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.title('face Recognition')
root.resizable(False, False)
root.geometry('300x150')


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )


# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
)

open_button.grid(row=1,column=1)


# run the application
root.mainloop()

