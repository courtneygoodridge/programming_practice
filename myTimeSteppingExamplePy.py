#### Initial State - starting position, heading angle, time step
import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy

def TimeStep(heading_angle, samples, timestep, speed, SimutlationTime): # now timestep is a function, user can input any parameters and plot the results.
startpos_x = 0
startpos_y = 0
heading_angle = heading_angle # 5 # degrees of the heading offset
heading_angle = heading_angle * math.pi /180 # converting to degrees
samples = samples # 5 # per second 
timestep = timestep / samples # 1
speed = speed # 10 # in metres per second

SimulationTime = SimulationTime # 30 # in seconds
TotalSamples = SimulationTime * samples # number of samples allowed within the simulation time 


X = [0] * TotalSamples # x the rows length of number of samples
Y = [0] * TotalSamples # y the rows length of number of samples

#### Update loop

for i in range(TotalSamples): # iterates over a range of 0 up to total samples (150)
        if i > 0:
                X[i] = X[i-1] + numpy.cos(heading_angle) * speed * timestep # the cosine of the heading angle mulitpled by speed multiplied by the timestep
                Y[i] = Y[i-1] + numpy.sin(heading_angle) * speed * timestep
            
#### Plotting

plt.plot(X, Y)
plt.show()

### Dataframe and saving

df = pd.DataFrame({'X': X, 'Y': Y}) # creates dataframe from X and Y variables 

df.to_csv('myTimeSteppingExampleDataPy.csv', sep =',') # saves dataframe as an csv file

return



