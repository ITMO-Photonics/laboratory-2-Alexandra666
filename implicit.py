import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

g=9.8
Nsteps=500
#t=np.linspace(0.,5.,Nsteps+1)
#y=np.empty_like(t)
#v=np.empty_like(t)
#h=t[1]-t[0]
h=0.05
r = np.array([25.,25.])
v = np.array([5.,0.])

fig, ax = plt.subplots()

circle, = ax.plot([], [], 'bo', ms=10)

def init():
    ax.set_xlim([0., 50.])
    ax.set_ylim([0., 50.])
    return circle,

def updatefig(frame):
    v[1] = v[1]-g*h
    r[1] = r[1]+h*v[1]    
    if r[1]<=0.:    
        v[1]=-v[1]

    v[0] = v[0]-0*h
    r[0] = r[0]+h*v[0]
    if r[0]<=0. or r[0]>=50.:
        v[0]=-v[0]

    circle.set_xdata(r[0])
    circle.set_ydata(r[1])
    return circle,

anim = animation.FuncAnimation(fig, updatefig, frames=200000, init_func=init, interval=0.01, blit=True, repeat=False)
plt.show()
