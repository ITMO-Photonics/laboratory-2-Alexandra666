import numpy as np
import matplotlib.pyplot as plt
g=9.8
Nsteps=50
t=np.linspace(0.,5.,Nsteps+1)
y=np.empty.like(t)
v=np.empty.like(t)
h=5/(Nsteps+1)
v[0]=0
for i in range (Nsteps):
    v[i+1]=v[i]-g*h
y[0]=int(input('High of a ball'))
for i in range (Nsteps):
    y[i+1]=y[i]+h*v[i]
plt.plot(t,y,'k.')
