import os

def replace():
    files = []

    keyword = "final"

    path1 = "waka\\WakaNats2017"
    path2 = "waka\\WakaNats2018"

    dirs1 = os.listdir(path1)
    dirs2 = os.listdir(path2)

    for file in dirs1:
        if keyword in file.lower():
            file.append(file)
        else: pass
    
    for games in files:
        f = open("{}\\{}".format(path1, files), "a")

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
        
        # lines_in_file = f.readlines()       # puts all the lines inside the file into variable lines_in_file

        line_count = 0

        for entries in str(f.readlines()).split(","):
            if entries == "": pass
            else: print(entries)

        #print(str(f.readlines()).split(","))

# analyse_files()

"""asd = "asdfasdfkashafasdsda,asfkhdflhfasdf,adf,a,s,,,asdfasdfasdf,,,asd,fasdfhsa,,,asdf"
asdf = asd.replace(","," ")
print(asdf)

jkl = asd.split(",")
print(jkl)

for entries in jkl:
    if entries == "": pass
    else: print(entries)"""

