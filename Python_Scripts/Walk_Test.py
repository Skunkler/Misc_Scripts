#This script was written by Warren Kunkler on 1/6/2016 in support of the project to rewrite the TFW files
#for the 2015 clark county imagery so that they may be used in AutoCAD

import os

def FindFile(BaseWS):                                               #when running this program pass the base work space starting with r"" 
                                                                    #through the parameter of FindFile        
    
    for root, dirs, files in os.walk(BaseWS):                       #looping through all directories
        for f in files:                                             #looping through the list of all files 
            if f[-4::1] == '.tfw':                                  #separate out just the files that end in ".tfw"
                outFile_List = []                                   #initialize outFile_List
                x = f[:-4]                                          #get the first part of the filename important for later
                input_path = root + '\\' + str(f)                   #input file path set to read mode
                readFile = open(input_path, 'r')
                input_Outpath = root + "\\" + str(x) + ".tfw"       #cast x as a string and concatenate ".tfw" to it otherwise you'll get an error
                for line in readFile:                               #for each line in the input path files, append each line to the outFile_List
                    outFile_List.append(line)
            

                outFile = open(input_Outpath, "w")                  #break out of previous for loop and set outFile to overwrite the old tfw files
                for element in outFile_List:                        #iterate through outFile_List and write each element to the new file
                    outFile.write(element)                          #note each element within the list already has a '\n' return at the end of it
                outFile.close()                                     #close outFile after all elements are written to it
                readFile.close()                                    #close readFile
                                                                    



