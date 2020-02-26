library(randomForest)
library(raster)
library(rgdal)

training <- readOGR("E:/Imagery_ENVI_SupervisedTests/mosaick_stacked_imagery/Mosaic_output/shp/ROIs_sample.shp", "ROIs_sample")

imagery <- brick("E:/Imagery_ENVI_SupervisedTests/mosaick_stacked_imagery/Mosaic_output/imagery/band_4_mosaic.img")


roi_data <- extract(imagery, training, df=TRUE)

roi_data$lc <- as.factor(training$CLASS_ID[roi_data$ID])
roi_data$desc <- as.factor(training$CLASS_NAME[roi_data$ID])

set.seed(12)

colnames(roi_data) <- c('ID', 'b1', 'b2', 'b3', 'b4', 'b5')

rf <- randomForest(~b1, data=roi_data, importance=TRUE)
print(rf)

image_class <- imagery
names(image_class) <- c("b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8")
image_pred <- predict(image_class, model = rf, na.rm=T)

colors <- c(rgb(255, 0, 0, maxColorValue = 255),
            rgb(0, 0, 255, maxColorValue = 255),
            rgb(0,255,0, maxColorValue = 255))

plotRGB(imagery, r = 1, g = 2, b = 3, stretch = "lin")
plot(image_pred, col = colors)
