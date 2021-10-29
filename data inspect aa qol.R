# https://data.austintexas.gov/City-Government/Final-Report-of-the-Asian-American-Quality-of-Life/hc5t-p62z
setwd('/Users/abelng/Desktop/2021fall/CS699 Data Mining/Project Assignment')
library(dplyr)
testdata <- data.frame(read.csv('Final_Report_of_the_Asian_American_Quality_of_Life__AAQoL_.csv'))
testclean <- na.omit(testdata)
testcleanfinal <- testclean[,1:93]
testattributes <- c("Age","Gender","Ethnicity","Marital.Status","Education.Completed","Household.Size",
                    "Income","US.Born","Duration.of.Residency","Primary.Language","English.Speaking",
                    "English.Difficulties","Familiarity.with.America","Familiarity.with.Ethnic.Origin",
                    "Present.Health","Present.Mental.Health","Present.Oral.Health","Regular.Exercise",
                    "Heart.Disease","Cancer","Kidney.Problem","Health.Insurance","Dental.Insurance",
                    "Unmet.Health.Need","Unmet.Dental.Needs","Close.Friend","Quality.of.Life")
employment <- c("Full.Time.Employment","Part.Time.Employment","Self.Employed.Full.Time",
                "Self.Employed.Part.Time","Student","Homemaker","Retired","Disabled","Unemployed",
                "Other.Employment.Description")

a1 <- select(testcleanfinal,testattributes)

# Add the class attribute Life.Quality
a1 <- a1 %>%
  mutate(Life.Quality = case_when(Quality.of.Life>=9 ~ 'Great',
                                  Quality.of.Life>=7 ~ 'Good',
                                  TRUE ~ 'Fair'))
a1 <- a1 %>%
  mutate(Life.Quality.Simp = case_when(Quality.of.Life>=8 ~ 'Great',
                                  TRUE ~ 'Fair'))


write.csv(a1,"/Users/abelng/Desktop/2021fall/CS699 Data Mining/Project Assignment/AAQoLsurveyclean.csv", row.names = FALSE)
