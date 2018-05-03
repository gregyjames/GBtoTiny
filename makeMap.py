import matplotlib.pyplot as plt
import matplotlib as mpl
from tinydb import TinyDB

db1 = TinyDB("Pacific.json")
phages = db1.table('phage')
genes1 = db1.table('genes')
bounds = []

for gene in genes1:
  bounds.append(int(gene["location_start"]))

size = 0

for phage in phages:
  size = phage["size"]
  
# Make a figure and axes with dimensions as desired.
fig = plt.figure(figsize=(30000, 3))
ax2 = fig.add_axes([0.05, 0.475, 0.9, 0.15])

# The second example illustrates the use of a ListedColormap, a
# BoundaryNorm, and extended ends to show the "over" and "under"
# value colors.
cmap = mpl.colors.ListedColormap(['r', 'g', 'b', 'c'])
cmap.set_over('0.25')
cmap.set_under('0.75')

# If a ListedColormap is used, the length of the bounds array must be
# one greater than the length of the color list.  The bounds must be
# monotonically increasing.

norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
cb2 = mpl.colorbar.ColorbarBase(ax2, cmap=cmap,
                                norm=norm,
                                # to use 'extend', you must
                                # specify two extra boundaries:
                                boundaries=[0] + bounds + [13],
                                extend='both',
                                ticks=bounds,  # optional
                                spacing='proportional',
                                orientation='horizontal')
cb2.set_label('Discrete intervals, some other units')


plt.savefig('myfig9j.png')