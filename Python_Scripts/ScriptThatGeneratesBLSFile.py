import sys, string, os 


"""Crawl_space = r"E:\2016_ClarkCounty_imageryclassification\classifiedImagery\corrected_input\Tiff_Output"
Imagery_List = []

for root, dirs, files in os.walk(Crawl_space):
    for filename in files:
        #print filename[:-12]
        Imagery_List.append(filename[:-12])"""






inputPath =r"E:\LiDAR_factor\Classified_output"


outFile = open(inputPath + '\\' + 'Image_convert.bls', "w")
outFile.write("PortInput1\tPortInput2\n")

OutputImages = r'E:/LiDAR_factor/Classified_output'
resrepo_county_images = r'R:/Image_ClarkCounty/2016/ClarkCounty_Collection'


OutputImages_List = []
for root, dirs, files in os.walk(OutputImages):
    for filename in files:
        if filename[-4:] == '.tif':
           
            real_root = OutputImages
           
            line = '"{wsPace}/{Imagefiles}"'.format(wsPace = real_root, Imagefiles = filename)
            lineComplete = line
            
            OutputImages_List.append(lineComplete)
        
            #outFile.write(lineComplete)
#outFile.close()
Resrepo_list = []
for root, dirs, files in os.walk(resrepo_county_images):
    for filename in files:
        if filename[-4:] == ".tif" and 'jpg' not in root:
            Last_root = root[-3:]
            First_root = root[:-4]
            realRoot = First_root + '/' + Last_root
            Resrepo_list.append(realRoot + '/' + filename)


FinalList = []

for i in range(0, len(Resrepo_list)):
    for x in range(0, len(OutputImages_List)):
        if Resrepo_list[i].split('/')[-1][:6] == OutputImages_List[x].split('/')[-1][:6]:
            FinalList.append(Resrepo_list[i])
FinalList.sort()
OutputImages_List.sort()
for i in range(0, len(FinalList)):
    line = FinalList[i] + '\t' + OutputImages_List[i] +'\n'
    outFile.write(line)
outFile.close()
