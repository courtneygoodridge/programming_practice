import matplotlib.pyplot as plt
import pandas as pd 

data = pd.read_csv("myTimeSteppingExampleDataPy.csv")
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

"""

Data types 

Turples - sequence of python objects that remain unchanged. Turples also use parentheses.

Lists - sequence of python objects. Similar to turples except these can be changed over time, hence why they're needed to iterate across for loops. Lists use square brackets.

Dicitionaries - sequences that are indexed via "keys", as opposed to a range of numbers likes lists. Dictionary represents unordered key:value pairs, each seperated by commas. Main operations on dictionaries involving storing a value with a key, and extracting the value given the key.

Dataframes - Tabular data structure with labeled axes (rows and columns). When filled with data, rows equate to observations and columns as conditions.

"""

plt.plot(data[["X"]], data[["Y"]]) # unsure if this is how to access data columns in python

plt.show()
