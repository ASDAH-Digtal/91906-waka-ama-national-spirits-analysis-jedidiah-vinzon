# Imports
from tkinter import *
from tkinter import ttk
import time
import os

# Where classes are made
class Player:
    def __init__(self, place, id, team_name, regional_association):
        self.place = place
        self.id = id
        self.team_name = team_name
        self.regional_association = regional_association


# Where functions are made
def read_files():
    files = []
    keyword = "final"

    path = "waka\\WakaNats{}".format(year.get())
    dirs = os.listdir(path)

    for file in dirs:
        if keyword in file.lower():
            file_read_text.set("Reading: {}".format(str(file)))
            files.append(file)
        else: pass
    
    number_of_files = len(files)
    results_text.set("There are {} files about the finals in the year {}".format(number_of_files, year.get()))

def analyse_files():
    files = []
    keyword = "final"

    path = "waka\\WakaNats{}".format(year.get())
    dirs = os.listdir(path)

    for file in dirs:
        
        # file_read.configure(text="Reading: {}".format(str(file)))
        if keyword in file.lower():
            files.append(file)
        else: pass
    
    # number_of_files = len(files)
    # results_text.set("There are {} files about the finals in the year {}".format(number_of_files, year.get()))

    for game in files:
        f = open(game, "r")
        pass

# Setting up root
root = Tk()
root.title("Waka Ama New Zealand Club")

# title_label = ttk.Label(root, text="Waka Ama New Zealand Club").grid(row=0, column=0)

# Variables
year = StringVar()
results_text = StringVar()
file_read_text = StringVar()

# Setting up frames
frame1 = ttk.LabelFrame(root, text="Available Folders")
frame1.grid(row=0, column=0, padx=20, pady=20)

frame2 = ttk.LabelFrame(root, text="Results")
frame2.grid(row=0, column=1, padx=20, pady=20)

# What's inside frame1?
label1 = ttk.Label(frame1, text="These are the available files to analyse", justify="center").grid(row=1, columnspan=2)
option_2017 = ttk.Radiobutton(frame1, text="2017", variable=year, value="2017").grid(row=2, column=0)
option_2018 = ttk.Radiobutton(frame1, text="2018", variable=year, value="2018").grid(row=3, column=0)

check_button = ttk.Button(frame1, text="Check files", command=read_files).grid(row=4, column=0, columnspan=3)
analyse_button = ttk.Button(frame1, text="Analyse", command=analyse_files).grid(row=5, column=0, columnspan=3)

# What's inside frame2?
results = ttk.Label(frame2, textvariable=results_text, justify="center")
results_text.set("The results of your query will be found here!")
results.grid(row=0, column=0)

file_read = ttk.Label(frame2, textvariable=file_read_text, justify="center").grid(row=1, column=0)
# Run everything
root.mainloop()