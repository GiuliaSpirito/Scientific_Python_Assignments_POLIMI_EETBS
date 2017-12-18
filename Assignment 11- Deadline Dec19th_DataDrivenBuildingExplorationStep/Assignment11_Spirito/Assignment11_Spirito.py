import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

DataFolderPath = "C:/Users/giugi/Desktop/University//4 anno_MAG\EETBS/Assignments/Assignment11_Spirito/Data"
ConsumptionFileName= "consumption_5545.csv"
ConsumptionFilePath = DataFolderPath+"/"+ConsumptionFileName

DF_consumption = pd.read_csv(ConsumptionFilePath, sep= ",", index_col=0)
previousIndex= DF_consumption.index  
ParsedIndex= pd.to_datetime(previousIndex)   #we converted them into real dates (=datetype)
DF_consumption.index= ParsedIndex     # we assigned the new parsed index to the Consumption DataFrame


#Let's import Weather Data as we did for AC consumptions
weatherSourceFileName= "Austin_weather_2014.csv"
weatherSourceFilePath= DataFolderPath+"/"+weatherSourceFileName
DF_weatherSource= pd.read_csv(weatherSourceFilePath, sep=";", index_col=0)   
DF_weatherSource.index
previousIndex= DF_weatherSource.index         
NewParsedIndex= pd.to_datetime(previousIndex)   
DF_weatherSource.index= NewParsedIndex
# Let's take only temperature column
series_temperature = DF_weatherSource["temperature"]
DF_temperature = DF_weatherSource[["temperature"]]  #let's convert it in a DataFrame of just one column

#Let's do the same for irradiation
irradianceSourceFileName= "irradiance_2014_gen.csv"
irradianceSourceFilePath= DataFolderPath+"/"+irradianceSourceFileName
DF_irradianceSource= pd.read_csv(irradianceSourceFilePath, sep=";", index_col=1)   
DF_irradianceSource.head(5)
previousIndex_irradiance= DF_irradianceSource.index         
NewParsedIndex_irradiance= pd.to_datetime(previousIndex_irradiance)   
DF_irradianceSource.index= NewParsedIndex_irradiance
# Let's take only PV_generation column, which we can refer to irradiance
DF_irradiance= DF_irradianceSource[["gen"]]
#Let's put all the negative values equal to zero 
DF_irradiance[DF_irradianceSource["gen"]<0]=0

#Let's put Consumption_DF,Temperature_DF and Irradiance_DF in a unique DataFrame: DF_joined
DF_joined = DF_consumption.join([DF_temperature,DF_irradiance])
DF_joined.dropna()


# Let's take datas from June 1st to June 3rd
DF_myChosenDates = DF_joined["2014-06-01 00:00:00":"2014-06-03 23:00:00"]

#plot with same axis x and with different scale for axis y

fig,ax1 = plt.subplots()
ax1.plot(DF_myChosenDates.index,DF_myChosenDates.iloc[:,0], color= 'b')
ax1.set_xlabel("Time")
ax1.set_ylabel("AC power [W]", color='b')
ax1.tick_params('y', colors= 'b')

ax2= ax1.twinx()
ax2.plot(DF_myChosenDates.index,DF_myChosenDates.iloc[:,1], color= 'r')
ax2.set_ylabel("Temperature",color= 'r')
ax2.tick_params('y', colors= 'r')

ax3= ax2.twinx()
ax3.plot(DF_myChosenDates.index,DF_myChosenDates.iloc[:,2], color= 'g')
ax3.set_ylabel("Iraddiance",color= 'g')
ax3.tick_params('y', colors= 'g')
plt.show()