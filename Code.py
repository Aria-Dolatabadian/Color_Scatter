import numpy as np
import pandas as pd
from bokeh.plotting import figure, show
#Random array data
# N = 4000
# a = np.random.random(size=N) * 100
# b = np.random.random(size=N) * 100
# z = np.random.random(size=N) * 1.5
# #save array into csv
# x = np.savetxt("x.csv", a, delimiter=",")
# y = np.savetxt("y.csv", b, delimiter=",")
# z = np.savetxt("z.csv", z, delimiter=",")
#read csv
x = pd.read_csv('x.csv')
y = pd.read_csv('y.csv')
z = pd.read_csv('z.csv')

# #Convert csv to array
x = np.loadtxt('x.csv', delimiter=',')
y = np.loadtxt('y.csv', delimiter=',')
z = np.loadtxt('z.csv', delimiter=',')

colors = np.array([ [r, g, 150] for r, g in zip(50 + 2*x, 30 + 2*y) ], dtype="uint8")

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,xpan,help"

p = figure(tools=TOOLS)

p.scatter(x, y, radius=z,
          fill_color=colors, fill_alpha=0.6,
          line_color=None)

show(p)
