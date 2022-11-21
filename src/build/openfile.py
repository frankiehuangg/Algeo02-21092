import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

def select_file():
	filetypes = ( 
		("Text files", "*.txt*"),
		("all files", "*.*")
	)

	filename = fd.askopenfilename(
		initialdir='../../',
		title='Choose file',
		filetypes=filetypes
	)

def select_dir():
	filepath = fd.askdirectory(
		initialdir="../../",
		title='Choose directory'
	)