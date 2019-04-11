import numpy as np
import matplotlib.pyplot as plt

N = 5
eggs_received = (100000, 150000, 100000, 50000, 150000)
year = (2014, 2015, 2016, 2017, 2018)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, eggs_received, width, color='r', yerr=year)

eggs_hatched = (80000, 120000, 90000, 40000, 140000)
year = (2014, 2015, 2016, 2017, 2018)
rects2 = ax.bar(ind + width, eggs_hatched, width, color='y', yerr=year)

# add some text for labels, title and axes ticks
ax.set_ylabel('Value (thousands)')
ax.set_title('Rainbow Trout Received and Hatched')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('2014', '2015', '2016', '2017', '2018'))

ax.legend((rects1[0], rects2[0]), ('Received Eggs', 'Hatched Eggs'))
ax.legend = 'left'


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1*height,
                '%d' % int(height),
                ha='left', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()