#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:38:09 2021

@author: Jaimew
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:16:30 2021

@author: Jaimew
"""
import numpy as np
import matplotlib.pyplot as plt

#Set variables
h = 1.4 # height in m
mua = 18*10**(-6) # viscosity of air in kg/(m*s)
rho = 997 # density of water in kg/m^3
g = 9.81
D = 0.000000002
RH = 0.95

## Calculate
fracts = (9*h*mua)/(2*rho*g)
fracte = (D*(1-RH))**(-1)

Rsol = ((9*h*mua*D*(1-RH))/(2*rho*g))**(1/4)
tsol = (fracts) * (Rsol**(-2))

R = np.linspace(4*(10**(-6)), 0.0003, 300)
ts = fracts * (R**(-2));
te = (R**2)*fracte;

# Ideal particle
idealt = np.zeros(len(R))+(2*g*h)**(1/2)/g

## Plot

R = R*10**6
plt.plot(np.extract(R/10**6 <= Rsol, R), np.extract(ts >= tsol, ts), "r--", linewidth = 1.5, label="_nolegend_")
plt.plot(np.extract(R/10**6 >= Rsol, R), np.extract(ts <= tsol, ts), "r-", linewidth = 1.5)
plt.plot(np.extract(R/10**6 >= Rsol, R), np.extract(te >= tsol, te), "b--", linewidth = 1.5, label="_nolegend_")
plt.plot(np.extract(R/10**6 <= Rsol, R), np.extract(te <= tsol, te), "b-", linewidth = 1.5)
plt.plot(R, idealt, "y:")

plt.gca().invert_yaxis()
plt.gca().xaxis.tick_top()


plt.gca().set_xlabel("Droplet radius(μm)")
plt.gca().set_ylabel("Time (s)")

plt.xlim((0, 300))
plt.ylim((10, 0))

plt.legend(["Settling curve", "Evaportaion curve", "Ideal particle"])
# legend("","Settling curve", "", "Evaporation curve", "Ideal particle", "Location","southeast")
