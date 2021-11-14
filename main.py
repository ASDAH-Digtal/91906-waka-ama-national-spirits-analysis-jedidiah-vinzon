# Imports
from tkinter import *
from tkinter import ttk
import time
import os

# Where classes are made
class Regional:
    def __init__(self, name, points):
        self.name = name
        self.points = points
    
    def add_points(self, position):
        if position == 1:
            self.points += 8
        elif position == 2:
            self.points += 7
        elif position == 3:
            self.points += 6
        elif position == 4:
            self.points += 5
        elif position == 5:
            self.points += 4
        elif position == 6:
            self.points += 3
        elif position == 7:
            self.points += 2
        else:
            self.points += 1

    def print_obj(self):
        print(self.name, self.points)


# Where functions are made
def read_files():
    """Finds the files to be read with the keyword: 'final'; and prints how many there are"""
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
    """Analyses all the files with the keyword: 'final'; and shows all the points for each Regional Association"""
    files = []
    reg_ass = []
    keyword = "final"
    count = 0

    path = "waka\\WakaNats{}".format(year.get())
    dirs = os.listdir(path)

    for file in dirs:               # runs through all the files in the directory
        if keyword in file.lower(): # checks if all the files found have the keyword in it
            files.append(file)      # adds the files to the list called 'files'
        else: pass                  # otherwise, the loop passes the file

    for game in files:
        f = open(game, "r")

        for line in f.readlines():
            if count == 0:
                pass
            else:
                if line[5] in reg_ass:
                    pass
                else:
                    temp_obj = Regional(line[5], 0)
                    temp_obj.add_points(int[line[0]])
                    reg_ass.append(temp_obj)
            
            count += 1

# Setting up root
root = Tk()
root.title("Waka Ama New Zealand Club")

# title_label = ttk.Label(root, text="Waka Ama New Zealand Club").grid(row=0, column=0)

# Variables
year = StringVar()
results_text = StringVar()
file_read_text = StringVar()
error_text = StringVar()

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