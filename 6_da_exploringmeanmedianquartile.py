import pandas as pd #useful for loading the dataset

# Load Dataset
dataset = pd.read_csv('Dataset.csv') #read the dataset
datasetwithNaN = dataset
print("DATASET",dataset)

# Load Summarize
print("Count:",dataset.shape)
print("MMM:",dataset.describe())

###Checking for NaN Values
dataset.isna().any() # checks if any column in null values 

### Filling NaN values with the Mean  
###Problem - New value becomes high coz of outlier (Large value scale)

Mean = dataset.price.fillna(dataset.price.mean())
print("MEAN",Mean)

### Solution - Filling NaN value with Median
Median = dataset.price.fillna(dataset.price.median())
print("MEDIAN",Median)

###Identifying and removing the outlier - Huge difference in value 
dataset.describe()

percentile = dataset.price.quantile(1.0) #100%
print("PERCENTILE",percentile)

datasetNoOutlier = dataset[dataset.price<percentile]
print("DNO",datasetNoOutlier)
