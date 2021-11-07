import os

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

f = open("waka\\WakaNats2017\\001-Heat 1-01.lif", "r")
for line in f.readlines():
    line = str(line.split(","))
    line = line.strip()
    
    print(line)