import sys, string, os, time, datetime, shutil, traceback, arcpy
from arcpy import env

env.workspace = r"S:\muddy_virgin\Imagery_20161219\DMI16101-FLIGHT_DATE-1219-2016\6-INCH-4BAND-16BIT-ORTHOPHOTOS"
ws = env.workspace


arcpy.env.overwriteOutput = True
arcpy.env.pyramid = "None"
arcpy.env.rasterStatistics = "None"

fcs = arcpy.ListRasters("","")

for fc in fcs:
    OrigName = fc[:-4]
    NameLength = len(fc)
    name = ""
    if NameLength == 9:
        name = fc[0] + "0" + fc[1:]
        
    elif NameLength == 8:
        name = fc[0] + "00" + fc[1:]
        
    else:
        name = fc
        
    #PyrFile = ws + '\\' + OrigName + '.rrd'
    #StatFile = ws + '\\' +  OrigName + '.aux'
    TfwFile = ws + '\\' + OrigName + '.tfw'
    tifFile = ws + '\\' + OrigName + '.tif'

    tilename = name[:-4]
    
    #NewPyrFile = tilename + '.rrd'
    #NewStatFile = tilename + '.aux'
    NewTfwFile = tilename + '.tfw'
    NewtifFile = tilename + '.tif'

    newPath = r"S:\muddy_virgin\Imagery_20161219\DMI16101-FLIGHT_DATE-1219-2016\6-INCH-4BAND-16BIT-ORTHOPHOTOS-CorrectedName"
    
    
    shutil.copy(tifFile, newPath + '\\' + NewtifFile)
    #shutil.copy(PyrFile, newPath + NewPyrFile)
    #shutil.copy(StatFile, newPath + NewStatFile)
    shutil.copy(TfwFile, newPath + '\\' + NewTfwFile)

    print "process complete for " + fc

    
