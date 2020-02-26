import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = r"L:\Lidar\_ClarkCounty_2016\Vendor_Products\DEM\QL1"


azimuth = 315
altitude = 45
modelShadows = "SHADOWS"
zFactor = 1


arcpy.CheckOutExtension("Spatial")

rasters = arcpy.ListRasters("*", "*")
for raster in rasters:
    print "Processing for " + raster[:4]
    outHillShade = Hillshade(raster, azimuth, altitude, modelShadows, zFactor)
    outHillShade.save(r"L:\Lidar\_ClarkCounty_2016\SNWA\Working\tiles\grid_BE_hillshade\\" + raster)
    print "Processing for " + raster[:4] + " complete!"
    
