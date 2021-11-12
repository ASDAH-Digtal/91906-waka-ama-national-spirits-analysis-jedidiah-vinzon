import os

race = {
    "race_number": "",
    "race_type": "",
    "race_heat": "",
    "race_title": ""
}

"""class Race:
    def __init__(self, race_number, race_type, race_heat, race_title):
        self.race_number = race_number
        self.race_type = race_type
        self.race_heat = race_heat
        self.race_title = race_title

class Team:
    def __init__(self, place, team_id, team_name, regional_association):
        self.place = place
        self.team_id = team_id
        self.team_name = team_name
        self.regional_association = regional_association
"""

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



def main():
    files = []
    keyword = "final"

    path = "waka\\WakaNats2017"
    dirs = os.listdir(path)

    for file in dirs:
        if keyword in file.lower():
            files.append(file)
        else: pass
    
    number_of_files = len(files)
    print(files)
    print(number_of_files)

count = 0
reg_ass = []

f = open("waka\\WakaNats2017\\001-Heat 1-01.lif", "r")
for line in f.readlines():
    if count == 0:
        pass
    else:
        if line[5] in reg_ass:
            pass
        else:
            temp_obj = Regional(line[5], 0)
            temp_obj.add_points(int(line[0]))
            reg_ass.append(temp_obj)

    print(line, reg_ass)
    count += 1