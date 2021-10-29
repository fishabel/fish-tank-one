# https://data.austintexas.gov/City-Government/Final-Report-of-the-Asian-American-Quality-of-Life/hc5t-p62z
setwd('/Users/abelng/Desktop/2021fall/CS699 Data Mining/Project Assignment')
library(dplyr)

a1 <- data.frame(read.csv('AAQoLsurveyclean.csv'))

# Inspect and replace blank cells with NA
a1[a1 ==''] <- NA

# Find out which columns need to be preprocessed
colsna = list()
for (i in 1:length(a1))
{
  if(sum(is.na(a1[,i])) > 0)
  {
    colsna <- append(colsna, colnames(a1)[i])
  }
}
colsna

# Replace the NA based on different value type, in order to make future normalization easier


