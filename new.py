

# IMPORTS #

from tkinter import *
from tkinter import ttk
from os import walk
import os

# IMPORTS #


# HERE IS WHERE CLASSES ARE MADE #

class Regional:
    def __init__(self, name, points):
        self.name = name
        self.points = points
    
    """def add_points(self, position):
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
            self.points += 1"""


# HERE IS WHERE CLASSES END #


# HERE IS WHERE FUNCTIONS ARE MADE #

def show_results(clubs):
    """This function prints the results of all the races, including the final points of the regional associations"""
    
    finalResults = Toplevel(root)
    finalResults.title("Club Points")

    results = [ [k,v] for k, v in clubs.items() ]
    results.sort(key = lambda x: x[1])
    results_listbox = Listbox(finalResults, width=40, height=60)

    for x in results:
        if x[[0][0]] == "":
            continue
        
        adding_student = "{}".format(x)
        results_listbox.insert(0, adding_student)
    
    results_listbox.grid(row=0, column=0)
    print(results)

def add_points(year, finalRace):
    """This function adds the points for all the regional associations in the current year and prints the results"""
    
    clubs = {}

    for race in finalRace:
        currentRace = open("WakaNats{}\{}".format(year, race), "r")

        for club in currentRace:
            waka = club.strip().split(",")

            score = 0

            if waka[0] == "1":
                score = 8
            elif waka[0] == "2":
                score = 7
            elif waka[0] == "3":
                score = 6
            elif waka[0] == "4":
                score = 5
            elif waka[0] == "5":
                score = 4
            elif waka[0] == "6":
                score = 3
            elif waka[0] == "7":
                score = 2
            elif waka[0] != "":
                score = 0
            else:
                score = 1
            
            if waka[5] not in clubs:
                clubs[waka[5]] = score
            else:
                clubs[waka[5]] = clubs.get(waka[5]) + score
            
        currentRace.close()
    show_results(clubs)

def read_files():
    """This function finds the files to be read with the keyword: 'final' and prints how many there are"""

    # These variables are initialized to prepare the rest of the function
    files = []
    keyword = "final"

    # Prepares the files to be read inside the folders depending on the year fetched
    path = "WakaNats{}".format(year.get())
    dirs = os.listdir(path)

    # Loops through all the files from the directory, and checks if the keyword is found
    for file in dirs:
        if keyword in file.lower():
            files.append(file)
        else: pass

    # Changes the results to show how many files there are in the folder with the keyword
    results_text.set(f"There are {len(files)} files about the finals in the year {year.get()}")

def anaylyse_files():
    """This functions analyses all the files with the keyword: 'final' and shows all the points for each Regional Association"""

    """ 
    # Initializes the variable used for the rest of the function
    files = []
    keyword = "final"
    totalCount = 0

    # Prepares to find all the files that needs to be found inside the directory
    path = "WakaNats{}".format(year.get())
    dirs = os.listdir(path)

    # Loops through all the files in the directory and adds it to the list if it has the keyword in it
    for file in dirs:
        if keyword in file.lower():
            files.append(file)
        else: pass
    
    # Loops through all the files inside the list and opens it up
    for play in files:
        f = open("{}\\{}".format(path, play), "r")

        lineCount = 0

        for line in f.readlines():  # Reads every line in each file
            totalCount += 1

            if lineCount == 0:      # Checks if the line count is the very first line
                lineCount += 1      # Ignores that line and continues on
                continue

            else:
                pass
    """
    
    races = []
    currentYear = year.get()

    for root, dirs, files in walk("WakaNats{}".format(currentYear)):
        races.extend(files)
        break

    finalRaces = []

    FINAL_NAMES = ["Final"]

    for race in races:
        if "Final" in race:
            finalRaces.append(race)
    
    print(finalRaces)
    add_points(currentYear, finalRaces)
    

# HERE IS WHERE FUNCTOINS END #


# HERE IS WHERE THE ACTUAL PROGRAM BEGINS #

years = []

for root, dirs, files in walk("."):
    years.extend(dirs)
    break

## SETTING UP THE ROOT ##
root = Tk()
root.title("Waka Ama New Zealand Club")

## SETTING UP THE VARIABLES
year = StringVar()
results_text = StringVar()
file_read_text = StringVar()
error_text = StringVar()

## SETTING UP THE FRAMES
folderFrame = ttk.LabelFrame(root, text="Available Folders")
folderFrame.grid(row=0, column=0, padx=20, pady=20)

resultFrame = ttk.LabelFrame(root, text="Results")
resultFrame.grid(row=0, column=1, padx=20, pady=20)

## WHAT'S INSIDE THE FOLDER FRAME?
available = ttk.Label(folderFrame, text="These are the available files to analyse", justify="center").grid(row=1, columnspan=2)
option2017 = ttk.Radiobutton(folderFrame, text="2017", variable=year, value="2017").grid(row=2, column=0)
option2018 = ttk.Radiobutton(folderFrame, text="2018", variable=year, value="2018").grid(row=3, column=0)

checkButton = ttk.Button(folderFrame, text="Check files", command=read_files).grid(row=4, column=0, columnspan=3)
analyseButton = ttk.Button(folderFrame, text="Analyze", command=anaylyse_files).grid(row=5, column=0, columnspan=3)

## WHAT'S INSIDE THE RESULT FRAME?
results = ttk.Label(resultFrame, textvariable=results_text, justify="center")
results_text.set("The results of your query will be found here!")
results.grid(row=0, column=0)

fileRead = ttk.Label(resultFrame, textvariable=file_read_text, justify="center").grid(row=1, column=0)

# HERE IS WHERE THE ACTUAL PROGRAM ENDS #

root.mainloop()