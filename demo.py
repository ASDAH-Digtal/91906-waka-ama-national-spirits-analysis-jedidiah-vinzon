import os

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

def total_points(reg_ass, position):
    reg_ass.add_points(position)

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

def error(line_count, file_name):
    f = open("waka\\WakaNats{}\\{}".format(2018, file_name), "r")
    lines = []

    for line in f.readlines():
        lines.append(line.strip())

    file_name = str(file_name)
    line_count = int(line_count)

    try:
        int(lines[line_count])
    except ValueError:
        print(f"### ERROR ###\nLine {line_count} of '{file_name}' begins with the string '{lines[line_count][0]}', not an integer\n>>> {lines[line_count]}\n")

def analyse_files():
    """Analyses all the files with the keyword: 'final'; and shows all the points for each Regional Association"""
    files = []
    reg_ass = []
    
    keyword = "final"

    line_count = 0
    total_count = 0

    path = "waka\\WakaNats{}".format(2018)
    dirs = os.listdir(path)

    for file in dirs:               # runs through all the files in the directory
        if keyword in file.lower(): # checks if all the files found have the keyword in it
            files.append(file)      # adds the files to the list called 'files'
        else: pass                  # otherwise, the loop passes the file

    for game in files:
        f = open("waka\\WakaNats2018\\{}".format(game), "r")    # opens the files found in the 'files' list and reads them

        line_count = 0

        for line in f.readlines():          # reads every line per file
            total_count += 1                # increments the total number of lines there are
                        
            if line_count == 0:             # if the line count is the very first line ...
                line_count += 1             # ignore that line and continue on by incrementing line_count by 1
            
            else:
                try:
                    line = str(line).replace(","," ")                   #JIC
                    if line[5] in reg_ass:                              # otherwise, if the sixth index of the line is inside the list called 'reg_ass' ...
                        try:
                            total_points(temp_obj, line[0])
                            print(f"{temp_obj.name}:{temp_obj.points}")
                        except:
                            error(line_count, game)
                
                    else:                                                                       # otherwise, if the regional association is not in the list
                        try:
                            temp_obj = Regional(line[5], 0)                                     # it's going to try and add that object into the class Regional 
                            temp_obj.add_points(int(line[0]))                                   # it's going to add points according to the position that it is in
                            reg_ass.append(temp_obj)                                            # and then it's going to add that object inside the list 'reg_ass'
                        
                            print(f"{total_count}: {line_count} >>> {line}{temp_obj}\n")        # this prints the total number of lines, the lines within the file and the line of the file it self

                            line_count += 1
                        except ValueError:
                            error(line_count, game)                                             # this checks if there is something wrong with the code, and then prints an error 

                except:
                    pass

analyse_files()