import os

input_path = raw_input("Please enter a directory: ")

for root, dirs, files in os.walk(input_path):
    subdir = root + '\\OutTest'
    for filename in files:
        
            
        if filename[-4:] == '.tfw':

            ReadFile = open(root + '\\' + filename, 'r')
            list_input = []
            readlines = ReadFile.readlines()

            
            
            for i in readlines:
                list_input.append(i)

            ReadFile.close()
            outfile = open(root + '\\' + filename, 'w')

            

            for i in list_input:
                outfile.write(i)
            outfile.close
