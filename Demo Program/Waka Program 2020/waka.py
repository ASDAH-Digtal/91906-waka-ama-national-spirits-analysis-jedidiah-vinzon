import tkinter as tk
from os import walk

def display_clubs(clubs):
    display = tk.Toplevel(root)
    display.title("Full Club Points")
    #display.iconbitmap("waka.ico")
    
    # Turn dict into list
    results = [ [k,v] for k, v in clubs.items() ]
    
    # Order list
    results.sort(key = lambda x: x[1])
    
    # Display list
    results_listbox = tk.Listbox(display, width = 38, height = 64, font = ("Arial", 8))
    
    # Adds each waka to the Listbox "results_listbox"
    for x in results:
        
        if(x[[0][0]] == ""):
            continue
        
        adding_student = "{}".format(x)
        results_listbox.insert(0, adding_student)
    
    results_listbox.grid(row = 0, column = 0)   
    print(results)
    
def calculate_scores(current_year, final_races):
    clubs = {}
    
    for race in final_races:
        current_race = open("{}/{}".format(current_year, race),"r")

        for club in current_race:
            waka = club.strip().split(",")
            
            score = 0
            
            if(waka[0] == "1"):
                score = 8
            elif(waka[0] == "2"):
                score = 7
            elif(waka[0] == "3"):
                score = 6
            elif(waka[0] == "4"):
                score = 5
            elif(waka[0] == "5"):
                score = 4
            elif(waka[0] == "6"):
                score = 3
            elif(waka[0] == "7"):
                score = 2
            elif(waka[0] != ""):
                score = 0
            else:
                score = 1
                
            if(waka[5] not in clubs):
                clubs[waka[5]] = score
            else:
                clubs[waka[5]] = clubs.get(waka[5]) + score
               
            
        current_race.close()
    
    display_clubs(clubs)

def display_files():
    races = []
    current_year = year_chosen.get()
    
    for root, dirs, files in walk("{}".format(current_year)):
        races.extend(files)
        break
    
    final_races = []
    
    FINAL_NAMES = ["Final"]
    
    for race in races:
        if("Final" in race):
            final_races.append(race)
    print(final_races)
    calculate_scores(current_year, final_races)
    
years = []

for root, dirs, files in walk("."):
    years.extend(dirs)
    break

BG_COLOUR = "#044C8C"
FG_COLOUR = "#FFFFFF"

root = tk.Tk()
root.title("Waka Ama Competition")
#root.iconbitmap("waka.ico")
root.configure(bg = BG_COLOUR)

waka_title = tk.Label(text="Waka Ama\nCompetition", font = ("Arial", 42), bg = BG_COLOUR, fg = FG_COLOUR)
waka_title.grid(row = 0, column = 0, columnspan =2)

message = tk.Label(root, text = "The Nga Kaihow o Aotearoa, Waka Ama New Zealand hold their annual Spirit Nationals.\nChoose either 2017 or 2018 to see the rankings of each Club.\nPoints are determined by the final races.\nIf they come in 1st place, they recieve 8 points.\nIf they come in 2nd, they receieve 7 points and so on. Teams that come in 8th or more receive just one point.", bg = BG_COLOUR, fg = FG_COLOUR)
message.grid(row = 1, column = 0, columnspan = 2)

year_chosen = tk.StringVar()
year_chosen.set("Choose a year")

year_options = tk.OptionMenu(root, year_chosen, *years)
year_options.configure(bg = BG_COLOUR, fg = FG_COLOUR)
year_options["menu"].config(bg = BG_COLOUR, fg = FG_COLOUR)
year_options.grid(row = 2, column = 0, columnspan =2)

button = tk.Button(root, text = "Display files", command = display_files, bg = BG_COLOUR, fg = FG_COLOUR)
button.grid(row = 3, column = 0, columnspan =2)

gap_label = tk.Label(text = "", bg = BG_COLOUR, fg = FG_COLOUR)
gap_label.grid(row = 4, column = 0, columnspan = 2)

root.mainloop()