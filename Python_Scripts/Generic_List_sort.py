import shutil, os

ws_1 = r"H:\Imagery_from_79\canopy_height\Book1.csv"

ReadFile = open(ws_1, "r")

readlines = ReadFile.readlines()

Gen_List = []

for line in readlines:
    #print line
    Gen_List.append(line[:-1])
    

ws_2 = r"H:\Imagery_from_79\canopy_height\canopy_height"
Output = r"H:\Imagery_from_79\canopy_height\Canopy_height_prod"
for root, dirs, files in os.walk(ws_2):
    for filename in files:
        if filename[-4:] == ".img" and filename[:5] in Gen_List or filename[-4:] == ".rrd" and filename[:5] in Gen_List:
            #print root + '\\' + filename + '\t' + Output + '\\' + filename
            shutil.copyfile(root + '\\' + filename, Output + '\\' + filename)
            
