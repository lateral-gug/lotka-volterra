import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt

a,b,c,d = 1,1,1,1
p0 = [0.5,0.7]

def dpdt(p,t):
    return [p[0]*(a-b*p[1]),p[1]*(c*p[0]-d)]

tt = np.linspace(0,20,500)
pp = odeint(dpdt,p0,tt)

plt.plot(tt,pp[:,0],'kx',label='Prede')
plt.plot(tt,pp[:,1],'rx',label='Predatori')
plt.legend(shadow=True,loc='lower right')
plt.xlabel('t')
plt.ylabel('n')

plt.show()

