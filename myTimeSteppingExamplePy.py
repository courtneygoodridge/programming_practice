#### Initial State - starting position, heading angle, time step
import math
import matplotlib.pyplot as plt
import pandas as pd
# for some reason these modules are not importing and are causing errors as they aren't recognised further in the script
startpos_x = 0
startpos_y = 0
heading_angle = 5 # degrees of the heading offset
heading_angle = heading_angle * math.pi /180 # converting to degrees
samples = 5 # per second 
timestep = 1 / samples
speed = 10 # in metres per second

SimulationTime = 30 # in seconds
TotalSamples = SimulationTime * samples # number of samples allowed within the simulation time 


X = [0] * TotalSamples # x the rows length of number of samples
Y = [0] * TotalSamples # y the rows length of number of samples

#### Update loop

#this fails because TotalSamples is an integer, not a list, so is not iterable (python cannot loop through it)
for i in TotalSamples: 
    if i > 1: #unlike matlab and R, python is zero-indexed (the first index in an array is 0)

        # cos() and sin() are not functions in the python base language. Check out the numpy package, you'll be using that a lot.
        X[i] = X[i-1] + cos(heading_angle) * speed * timestep # the cosine of the heading angle mulitpled by speed multiplied by the timestep
        Y[i] = Y[i-1] + sin(heading_angle) * speed * timestep
            
#### Plotting

plt.plot(X, Y) 

 ### Dataframe and saving

df = pd.DataFrame({'X': X, 'Y': Y}, index=[0]) # creates dataframe from X and Y variables 

df.to_csv('myTimeSteppingExampleData.csv') # saves dataframe as an csv file


