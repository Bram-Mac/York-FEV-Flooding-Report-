import matplotlib.pyplot as plt
import numpy as np

FEV = 9110000

fig = plt.figure(figsize=(10, 7)) 
ax = fig.add_subplot(111, projection='3d') 

plt.rcParams['axes.edgecolor'] = 'white'

ax.grid(False)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.xaxis.pane.set_edgecolor('w')
ax.yaxis.pane.set_edgecolor('w')
ax.zaxis.pane.set_edgecolor('w')

sl = (FEV/2)**0.5 # Side Length
print(sl)


# Define lines
a = [sl, sl]
b = [sl, sl]
c = [2, 0]

d = [sl, 0]
e = [sl, sl]
f = [0, 0]

g = [sl, sl]
h = [sl, 0]
i = [0, 0]

ax.plot(a, b, c, '--', color='k', linewidth = 2)
ax.plot(d, e, f, '--', color='k', linewidth = 2)
ax.plot(g, h, i, '--', color='k', linewidth = 2)

# Define main shape
x = [sl, sl, sl, 0, 0, 0, sl, sl, 0, 0, 0, 0]
y = [sl, 0, 0, 0, 0, sl, sl, 0, 0, 0, sl, sl]
z = [2, 2, 0, 0, 2, 2, 2, 2, 2, 0, 0, 2]

ax.plot(x, y, z, color='k', linewidth = 2)

ax.set_xticks(np.linspace(0, 2000, 5))  
ax.set_yticks(np.linspace(0, 2000, 5))  
ax.set_zticks(np.linspace(0, 2, 2))       

ax.set_xlim(0, sl) 
ax.set_ylim(0, sl) 
ax.set_zlim(0,10)  

ax.view_init(elev=20, azim=-135)
