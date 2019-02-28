import matplotlib.pyplot as plt
import csv
with open("myTimeSteppingExampleDataPy.csv") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = [r for r in reader]
    
#since you haven't read in the header you cannot access

print (data)

"""
the following line throws the error:
TypeError: list indices must be integers or slices, not list

This is because you have read in the data as a list of lists. 
So, the first row would be accessed data[0]. 
The first item of the first row would be data[0][0] 

Look up the difference between lists, dictionaries, and dataframes.

In this example, you probably want a dataframe. Use pandas to load the csv.
"""


plt.plot(data[["X"]], data[["Y"]]) # unsure if this is how to access data columns in python

plt.show()
