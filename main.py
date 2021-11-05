# Imports
from tkinter import *
from tkinter import ttk

# Where functions are made
def read_files():
    f = open("waka\\WakaNats{}".format(year.get()), "r")
    pass


# Setting up root
root = Tk()
root.title("Waka Ama New Zealand Club")
root.geometry("500x500")

# Variables
year = StringVar()
year.set("2017")

# Setting up frames
frame1 = ttk.Frame(root)
frame1.grid(row=0, column=0, sticky="NSEW")


# What's inside frame1?
# title_label = ttk.Label(frame1, text="Waka Ama New Zealand Club", justify="center", anchor="center").grid(row=1, column=0, sticky="EW")
analyse_label = ttk.Label(frame1, text="Folders available for analysing: ").grid(row=2, column=0)

button17 = ttk.Radiobutton(frame1, variable=year, value="2017", text="2017").grid(row=2, column=1)
button18 = ttk.Radiobutton(frame1, variable=year, value="2018", text="2018").grid(row=2, column=2)
analyse_button = ttk.Button(frame1, command=read_files).grid(row=3, column=1)

# Run everything
root.mainloop()