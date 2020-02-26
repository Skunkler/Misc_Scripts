import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
DataFrame1 = "Layers"
df = arcpy.mapping.ListDataFrames(mxd, DataFrame1)[0]
#source_layer =  arcpy.mapping.Layer(r"H:\LVVVEG_2012\gis\layer_files\pool_12329.lyr")
source_layer =  arcpy.mapping.Layer(r"E:\2016_ClarkCounty_imageryclassification\Poly_17801_cleanedFinal.lyr")
#source_layer =  arcpy.mapping.Layer(r"H:\LVVVEG_2012\gis\layer_files\pool_12329_filter2.lyr")
for lyr in arcpy.mapping.ListLayers(mxd):
    x = lyr.name
    pool = x[0:1]
    if pool == "P":

        arcpy.mapping.UpdateLayer(df, lyr, source_layer, True)
arcpy.RefreshTOC()
arcpy.RefreshActiveView()
del lyr, mxd
