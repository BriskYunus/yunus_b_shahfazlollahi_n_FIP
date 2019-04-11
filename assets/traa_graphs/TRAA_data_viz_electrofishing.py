import csv
import numpy as np
import matplotlib.pyplot as plt

Years = [2016, 2017, 2018]
Komoka = [15, 14, 23]
Oxbow = [10, 18, 12]
Dingman = [13, 15, 14]


plt.plot(Years, Komoka, color='orange')
plt.plot(Years, Oxbow, color='blue')
plt.plot(Years, Dingman, color='g')
plt.ylabel("Number of Fish Caught")
plt.xlabel("Years")
plt.title("Rainbow Trout Caught")
plt.gca().legend(('Komoka','Oxbow', 'Dingman'))
plt.show()