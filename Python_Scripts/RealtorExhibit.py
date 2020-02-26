mapList = arcpy.GetParameterAsText(0)

mainTitle = arcpy.GetParameterAsText(1)

subTitle = arcpy.GetParameterAsText(2)

taxAccount = arcpy.GetParameterAsText(3)


thisMap = arcpy.mapping.MapDocument("Current")

myDF = arcpy.mapping.ListDataFrames(thisMap)[0]
myLayers = arcpy.mapping.ListLayers(myDF)

for lyr in myLayers:
    arcpy.AddWarning(lyr)
    if lyr.name == "Parcels":
        arcpy.AddWarning("Got it!")

myElements = arcpy.mapping.ListLayoutElements(thisMap, "TEXT_ELEMENT")




for element in myElements:
    if element.name == "Main Title":
        element.text = mainTitle
    elif element.name == "SubTitle":
        element.text = subTitle

    arcpy.RefreshActiveView()


"""if "Parcel Map" in mapList:
    arcpy.AddWarning("Creating the Parcel Map...")

if "Water Utility Map" in mapList:
    arcpy.AddWarning("Creating the Water Map...")

if "Sewer Utility Map" in mapList:
    arcpy.AddWarning("Creating Sewer Map...")

if "Storm Water Utility Map" in mapList:
    arcpy.AddWarning("Creating the Storm Water Map...")"""
    


if "Parcel Map" in mapList:
    arcpy.AddWarning("Creating the Parcel Map...")
    for lyr in myLayers:
        if lyr.name == "Parcels Group":
            lyr.visible = "True"
        if lyr.name == "Storm Water Utility Group":
            lyr.visible = "False"
        if lyr.name == "Water Utility Group":
            lyr.name = "False"
        if lyr.name == "Sewer Utility Group":
            lyr.name = "False"
        if lyr.name == "Physical Features Group":
            lyr.name = "False"
        if lyr.name == "Base Group":
            lyr.name = "True"
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC



elif "Storm Water Utility Map" in mapList:
    arcpy.AddWarning("Creating the storm water map...")
    for lyr in myLayers:
        if lyr.name == "Parcels Group":
            lyr.visible = "False"
        if lyr.name == "Storm Water Utility Group":
            lyr.visible = "True"
        if lyr.name == "Water Utility Group":
            lyr.name = "False"
        if lyr.name == "Sewer Utility Group":
            lyr.name = "False"
        if lyr.name == "Physical Features Group":
            lyr.name = "False"
        if lyr.name == "Base Group":
            lyr.name = "True"
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC


elif "Water Utility Map" in mapList:
    arcpy.AddWarning("Creating sewer map...")
    for lyr in myLayers:
        if lyr.name == "Parcels Group":
            lyr.visible = "False"
        if lyr.name == "Storm Water Utility Group":
            lyr.visible = "False"
        if lyr.name == "Water Utility Group":
            lyr.name = "True"
        if lyr.name == "Sewer Utility Group":
            lyr.name = "False"
        if lyr.name == "Physical Features Group":
            lyr.name = "False"
        if lyr.name == "Base Group":
            lyr.name = "True"
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC



if "Sewer Utility Map" in mapList:
    arcpy.AddWarning("Creating Sewer Map...")
    for lyr in myLayers:
        if lyr.name == "Parcels Group":
            lyr.visible = "False"
        if lyr.name == "Storm Water Utility Group":
            lyr.visible = "False"
        if lyr.name == "Water Utility Group":
            lyr.name = "False"
        if lyr.name == "Sewer Utility Group":
            lyr.name = "True"
        if lyr.name == "Physical Features Group":
            lyr.name = "False"
        if lyr.name == "Base Group":
            lyr.name = "True"
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC





arcpy.AddWarning("Outputting the parcel map...")
arcpy.mapping.ExportToPDF(thisMap, r"E:\ArcGIS_Tutorials\ArcPy_Tutorial\EsriPress\GISTPython\MyExercises\Parcel_Map_" + mainTitle)
