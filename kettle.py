import numpy as np 
import matplotlib.pyplot as plt

#Here we define the variables
volume = int(input("Volume (m^3): "))
InitialTemp = 27
Density = int(input("Density (kg/m^3): "))
Power = int(input("Power (W): "))
SHC = int(input("SHC: "))
Time = int(input("Time (seconds): "))

timeList = []
[timeList.append(i) for i in range(0, Time + 1)]

TempList = []

[TempList.append("{:.2f}".format(InitialTemp + (Power * timeList[j])/(Density * volume * SHC))) for j in range(0, len(timeList) - 1)]


plt.plot(TempList)
plt.ylabel('Temperature (°C)')
plt.xlabel('time (seconds)')
plt.show()
