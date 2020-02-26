require(sp)
require(rgdal)
require(raster)
require(randomForest)




imagery <- brick("H:/2017_3_inch_samples/proprietary_stack/roi_samples/segmentation_o13912_sw_9bandstack.tif")

training <- readOGR("H:/2017_3_inch_samples/proprietary_stack/roi_samples/ROIS.shp", "ROIS")

#training <- shapefile("H:/2017_3_inch_samples/proprietary_stack/roi_samples/ROIS.shp")
roi_data <- extract(imagery, training, df = TRUE)

#roi_data$lc <- as.character(roi_data$)
#roi_data$lc <- as.factor(training$CLASS_ID[roi_data$ID])
roi_data$desc <- as.factor(training$Class_Name[roi_data$ID])



set.seed(1234567890)
colnames(roi_data) <- c('ID', 'b1', 'b2', 'b3', 'b4','b5', 'b6', 'b7','b8', 'b9', 'lc', 'desc')

write.csv(roi_data, file = "H:/2017_3_inch_samples/proprietary_stack/roi_samples/sample_data_training11.csv")


intable <- read.csv("H:/2017_3_inch_samples/proprietary_stack/roi_samples/sample_data_training10.csv")

myrf <- randomForest(desc ~ b1+b2+b3+b4+b5+b6+b7+b8, data = intable, keep.forest = TRUE, importance = TRUE)
#Matrix_var <- confusionMatrix

print(myrf)
saveRDS(myrf, file="H:/2017_3_inch_samples/proprietary_stack/roi_samples/RandomForestData6.rds")
varImpPlot(myrf)
rm(myrf)




rf <- readRDS("H:/2017_3_inch_samples/proprietary_stack/roi_samples/RandomForestData6.rds")


names(image_class) <- c("b1", "b2","b3","b4","b5","b6","b7","b8", "b9")
image_class <- imagery

predict(image_class, myrf, filename="H:/2017_3_inch_samples/image_classification/test11.tif", type = "response", index=1, na.rm=TRUE, progress="window", overwrite=TRUE)

