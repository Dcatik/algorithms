import time
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return -(x**2) + 3*x
def df(x):
    return -2*x + 3

N = 20    #iters
xx = 0    #start point
lmd = 0.1 #step

x_plt = np.arange(-5, 5, 0.1)
f_plt = [f(x) for x in x_plt]

plt.ion()
fig, ax = plt.subplots()
ax.grid(True)

ax.plot(x_plt, f_plt) #function view
point = ax.scatter(xx, f(xx), c = 'red') #red point

mn = 100
for i in range(N):
    #lmd = 1/(1.5*i if i != 0 else 1)
    lmd = 1/(min(i+1, mn))
    xx = xx - lmd*np.sign(df(xx)) # change xx

    point.set_offsets([xx, f(xx)]) #new point view

    #redrawing
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.02)

plt.ioff()
print(xx)
ax.scatter(xx, f(xx), c = 'blue')
plt.show()