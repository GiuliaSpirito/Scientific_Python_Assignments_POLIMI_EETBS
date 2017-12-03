import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Share of each component in the total heating load #U
labels=["wall","roof","door"]
HeatingLoadValues_Opaque= [1149.2,1240,92.5]
cols= ["r","b","g"]
plt.pie(HeatingLoadValues_Opaque,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0),autopct='%1.1f%%') 
plt.title("Heating load (opaque)") 

# Share of each component in the total cooling load #
CoolingLoadValues_Opaque= [547.5,514.6,43]
fig2= plt.figure()
plt.pie(CoolingLoadValues_Opaque,labels=labels,colors=cols,startangle=90,explode=(0.1,0,0),autopct='%1.1f%%') 
plt.title("Cooling load (opaque)") 

# Effect of changing the U value of the external wall on the overall heating load (opaque) #

U_heating_Opaque= 0.438
DeltaT_Heating= 24.8

fig3= plt.figure()
Area_wall= 105.8
x= np.arange(0.438,0.900,0.05) 

x_series= pd.Series(x)

def HeatingLoad_calculator(x):
    Q_wall= x*DeltaT_Heating*Area_wall
    y= Q_wall+1240+92.5
    return y
    
y_series= x_series.apply(HeatingLoad_calculator)         
plt.plot(x_series,y_series)

plt.xlabel("Uvalue_Wall [W/(Km^2)]")   
plt.ylabel("Overall heating load Q[W]")
plt.title("Variation of Q depending on U_wall") 

