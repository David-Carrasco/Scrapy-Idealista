PATH.DATA <- 'data/sample_retiro.csv'

#Loading dataset
dataset <- read.csv(PATH.DATA, header = T, na.strings = '', 
                    fileEncoding="iso-8859-1", 
                    colClasses = c('integer', 'integer', 'character', 'integer', 'character'))

#Descriptive Analysis
hist(dataset$price, breaks = 30)
