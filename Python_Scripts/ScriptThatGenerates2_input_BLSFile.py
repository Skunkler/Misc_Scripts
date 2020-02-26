import os

inputPath =r"H:/Imagery_from_79/canopy_height/Commission_Error_Clean2.bls"


Input1_ws = r"E:/2016_ClarkCounty_imageryclassification/thematic_images"


Input2_ws = r'H:/Imagery_from_79/canopy_height/canopy_height_10_25_2017'
outFile = open(inputPath, "w")
outFile.write("PortInput1\tPortInput2\n")

Input1_List = []
Input2_List = []

match_list = []

for root, dirs, files in os.walk(Input2_ws):
    for filename in files: 
        if filename[-4::1] == ".img":
            print filename[:5]
            match_list.append(filename[:5])
            Input_Line = '"{Input1WorkSpace}/{Input1_file}"'.format(Input1WorkSpace = Input2_ws, Input1_file = filename)
            Input1_List.append(Input_Line)

            

for root, dirs, files in os.walk(Input1_ws):
    for FName in files:
        if FName[-4::1] == ".img" and FName[1:6] in match_list:
            print FName[1:6]
            Input_Line = '"{Input2WorkSpace}/{Input2_file}"'.format(Input2WorkSpace = Input1_ws, Input2_file = FName)
            Input2_List.append(Input_Line)




ListCount = len(Input1_List)

for i in range(0, ListCount):
    Input1 = Input1_List[i]
    Input2 = Input2_List[i]
  
    line = Input2 + '\t' + Input1 +'\n'

    outFile.write(line)
outFile.close()    





