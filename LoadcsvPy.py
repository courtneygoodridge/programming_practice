import matplotlib.pyplot as plt
import csv
with open("myTimeSteppingExampleDataPy.csv") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = [r for r in reader]

plt.plot(data[["X"]], data[["Y"]]) # unsure if this is how to access data columns in python
plt.show()
