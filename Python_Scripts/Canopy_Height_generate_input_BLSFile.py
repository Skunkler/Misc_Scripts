import os

inputPath =r"E:/2016_ClarkCounty_imageryclassification/LAS_POINTS_Process/LiDAR_products/book_139_test/Book_140.bls"


Input1_ws = r"E:/2016_ClarkCounty_imageryclassification/LAS_POINTS_Process/LiDAR_products/book_139_test/book_140_products"


Input2_ws = r'E:/2016_ClarkCounty_imageryclassification/comission_cleaned_error'





outFile = open(inputPath, "w")
outFile.write("PortInput1\tPortInput2\tPortInput3\n")

Input1_List = []
Input2_List = []

match_list = []

for root, dirs, files in os.walk(Input1_ws):
    for filename in files: 
        if filename[-4:] == ".tif":
           
            match_list.append(filename[:5])
            
            Input_Line = '"{Input1WorkSpace}/{Input1_file}"'.format(Input1WorkSpace = Input1_ws, Input1_file = filename)
            Input1_List.append(Input_Line)

            

for root, dirs, files in os.walk(Input2_ws):
    for FName in files:
        if FName[-4:] == ".img" and FName[:5] in match_list:
            Input_Line = '"{Input2WorkSpace}/{Input2_file}"'.format(Input2WorkSpace = Input2_ws, Input2_file = FName)
            Input2_List.append(Input_Line)



ListCount = len(Input1_List)

for i in range(0, ListCount):
    Input1 = Input1_List[i]
    Input2 = Input2_List[i]

  
    line = Input1 + '\t' + Input2 +'\n'

    outFile.write(line)
outFile.close()





