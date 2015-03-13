library(caret)
library(randomForest)
options (warn=-1)
setwd('E:/Project/feature')
rawdata <- read.csv('ProcessedData.csv', header = TRUE, sep = ',')

data <- rawdata;

for(i in c(2:ncol(rawdata)-1)) {data[,i] = as.numeric(as.character(rawdata[,i]))}

featuresnames <- colnames(data)[-(1:1)]
features <- data[featuresnames]

set.seed(5188)
xdata <- createDataPartition(y=features$classe, p=3/4, list=FALSE )
training <- features[xdata,]
testing <- features[-xdata,]

rf_model  <- randomForest(classe ~ ., training, ntree=500, mtry=32)

training_pred <- predict(rf_model, training) 
print(confusionMatrix(training_pred, training$classe))

testing_pred <- predict(rf_model, testing) 
print(confusionMatrix(testing_pred, testing$classe))