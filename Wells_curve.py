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
from matplotlib.widgets import Slider, Button

#Set variables
h = 1.4 # height in m
mua = 18*10**(-6) # viscosity of air in kg/(m*s)
rho = 997 # density of water in kg/m^3
g = 9.81
D = 0.000000002
RH = 0.95

def calculate(h, mua, rho, g, D, RH):
    fracts = (9*h*mua)/(2*rho*g)
    fracte = (D*(1-RH))**(-1)
    
    Rsol = ((9*h*mua*D*(1-RH))/(2*rho*g))**(1/4)
    tsol = (fracts) * (Rsol**(-2))
    
    R = np.linspace(4*(10**(-6)), 0.0003, 300)
    ts = fracts * (R**(-2));
    te = (R**2)*fracte;
    
    idealt = np.zeros(len(R))+(2*g*h)**(1/2)/g
    
    return R, Rsol, ts, te, tsol, idealt

results = calculate(h, mua, rho, g, D, RH)
R = results[0]
Rsol = results[1]
ts = results[2]
te = results[3]
tsol = results[4]
idealt = results[5]
print(tsol)

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

plt.subplots_adjust(bottom=0.25)

axh = plt.axes([0.19, 0.15, 0.65, 0.03], facecolor="lightgoldenrodyellow")
h_slider = Slider(
    ax = axh,
    label="Initial height [m]",
    valmin=0.01,
    valmax=5,
    valinit=1.8)

axmua = plt.axes([0.19, 0.1, 0.65, 0.03], facecolor="lightgoldenrodyellow")
mua_slider = Slider(
    ax = axmua,
    label="Air viscosity[kg/(m*s)]",
    valmin=15*10**(-6),    # I chose this range of viscosity because this is how
    valmax=20*10**(-6), # it can vary with extremely low and high temperatures.
    valinit=18*10**(-6)) # This is approximately the viscosity at 20º.

axRH = plt.axes([0.19, 0.05, 0.65, 0.03], facecolor="lightgoldenrodyellow")
RH_slider = Slider(
    ax = axRH,
    label="Relative humidity",
    valmin=0,
    valmax=0.99,
    valinit=0.4)

def update(val):
    h = h_slider.val
    mua = mua_slider.val
    RH = RH_slider.val
    rho = 997 # density of water in kg/m^3
    g = 9.81
    D = 0.000000002
    
    results = calculate(h, mua, rho, g, D, RH)
    R = results[0]
    Rsol = results[1]
    ts = results[2]
    te = results[3]
    tsol = results[4]
    idealt = results[5]
    
    
    
h_slider.on_changed(update)
mua_slider.on_changed(update)
RH_slider.on_changed(update)


