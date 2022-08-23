import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

'''
z = 0

if y != 0 :
    x = r12 / 2 - π2*r12
    L4 : y = sqrt(3)/2 * r12
    L5 : y = - sqrt(3)/2 * r12

if y = 0:
    ξ = x / r12
    π2 = m2 / (m1 + m2)
    f(ξ,π2) = (1 - π2)*(ξ + π2)/pow( abs(ξ + π2) , 3 ) + π2 * (ξ + π2 -1) / pow( abs(ξ + π2 - 1) , 3 ) - ξ
    f(ξ,π2) = 0

    using bisection method
'''

'''
Sun vs Earth

Sun mass = m1 = 1.9884 * 10e30 kg
Earth mass = m2 = 5.9724 * 10e24 kg

r12 = 1AU = 149597870.700 m 

from wikipedia
'''

def f(ξ,π2):
    return (1 - π2) * (ξ + π2) / pow( abs(ξ + π2) , 3) + π2 * (ξ + π2 - 1) / pow( abs(ξ + π2 - 1) , 3) - ξ

def bm(ξ1,ξ2,π2,r12,d_lim=1.0e-8):
    d = pow((ξ2 - ξ1),2)
    while d > d_lim:
        ξmid = (ξ1 + ξ2) / 2.0
        fmid = f(ξmid,π2)
        if (fmid>0.0):
            ξ2 = ξmid
        else:
            ξ1 = ξmid
        d = pow((ξ2 - ξ1),2)
        x = (ξ1 + ξ2)/2 * r12
    return x

m1 = 1.9884 * 10e30   # Sun
m2 = 5.9724 * 10e24   # Earth
# m1 = 5.974 * 10e24
# m2 = 7.348 * 10e22  # moon
π2 = m2 / (m1 + m2)

r12 = 149597870.700   # 1AU
# r12 = 3.844 * 10e5  # Earth to moon

θ = 0

# m2 position
m2_x = r12 * np.cos(θ)
m2_y = r12 * np.sin(θ)

# Lagrangian point solve
L1 = (
    bm(1,0,π2,r12)*np.cos(θ),
    bm(1,0,π2,r12)*np.sin(θ)
)
L2 = (
    bm(2,1,π2,r12)*np.cos(θ),
    bm(2,1,π2,r12)*np.sin(θ)
)
L3 = (
    bm(0,-2,π2,r12)*np.cos(θ),
    bm(0,-2,π2,r12)*np.sin(θ)
)
L4 = (
    (r12 / 2 - π2*r12), 
    (np.sqrt(3) / 2 * r12)
)
L5 = (
    (r12 / 2 - π2*r12), 
    (-np.sqrt(3) / 2 * r12)
)
l4 = (
    (r12*np.cos(np.pi/3 + θ)),
    (r12*np.sin(np.pi/3 + θ))
)
l5 = (
    (r12*np.cos(-np.pi/3 + θ)),
    (r12*np.sin(-np.pi/3 + θ))
)

# Lagrangian Point output
print("##################################################")
print("\n")
print("Lagrangian Point")
print("\n")
print(f"L1 point : {L1}")
print(f"L2 point : {L2}")
print(f"L3 point : {L3}")
print(f"L4 point : {L4}")
print(f"L5 point : {L5}")
print("\n")
print(f"m2 position : {m2_x,m2_y}")
print("##################################################")
print(l4)
print(l5)

# orbit 2D model
orbit = patches.Circle(xy=(0.0,0.0), radius=r12,fill=False,linestyle = '--',color='black')
m1 = patches.Circle(xy=(0.0,0.0),radius=r12/2*10e-2,color='orangered',label='m1')
fig, ax = plt.subplots(figsize=(6, 6),)
ax.add_patch(orbit)
ax.add_patch(m1)
ax.autoscale()

ax.plot(m2_x,m2_y,'o',color='forestgreen',label="m2",zorder=1)

# Lagrangian Point
ax.plot(L1[0],L1[1],'D',color='red',label="L1",zorder=0)
ax.plot(L2[0],L2[1],'D',color='yellow', label="L2",zorder=0)
ax.plot(L3[0],L3[1],'D',color='orange',label="L3")
ax.plot(L4[0],L4[1],'D',color='magenta',label="L4")
ax.plot(L5[0],L5[1],'D',color='navy',label="L5")

# plt setting
ax.set_title('Lagrangian Point')
ax.set_xlabel('x-position [km]')
ax.set_ylabel('y-position [km]')
ax.legend()

plt.show()