import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

g=9.8
Nsteps=50
t=np.linspace(0.,5.,Nsteps+1)
#y=np.empty_like(t)
#v=np.empty_like(t)
h=t[1]-t[0]

r = np.array([5.,5.])
v = np.array([0.,0.])

fig, ax = plt.subplots()

circle, = ax.plot([], [], 'bo', ms=10)

def init():
    ax.set_xlim([0., 10.])
    ax.set_ylim([-130., 100.])
    return circle,

def updatefig(frame):
    v[1] = v[1]-g*h
    r[1] = r[1]+h*v[1]
    circle.set_xdata(r[0])
    circle.set_ydata(r[1])
    return circle,

anim = animation.FuncAnimation(fig, updatefig, frames=Nsteps, init_func=init, interval=10, blit=True, repeat=False)
plt.show()
