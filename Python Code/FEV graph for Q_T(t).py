import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Data = pd.read_csv(r'C:\Users\macha\Documents\Uni\Year 3\Project in Maths\Ouse Data\2015 Stage and Flow Data.csv')
time = Data['Day']
height = Data['Viking Stage']
Flow = Data['Viking Flow']

time_increment = time[1]-time[0]


t = np.linspace(0, 4.989583333, 475)  
Q = Flow 

Qup = 504.14   
Qdown = 394.10  


Q_up = 504   
Q_down = 392


# Find the first intersection with the red line
red_intersections = np.where(Q >= Q_up)[0]
if len(red_intersections) > 0:
    t_up_1 = t[red_intersections[0]]
    Q_up_1 = Q[red_intersections[0]]
    print(f"First red intersection: t={t_up_1}, Q={Q_up_1}")

# Find the last intersection with the blue line
blue_intersections = np.where(Q >= Q_down)[0]
if len(blue_intersections) > 0:
    t_down_2 = t[blue_intersections[-1]]
    Q_down_2 = Q[blue_intersections[-1]]
    print(f"Second blue intersection: t={t_down_2}, Q={Q_down_2}")

# Plot the data points
plt.plot(t, Q, 'k-')

# Plot the threshold lines
plt.axhline(y=Qup, color='red', linestyle='--', label=r'$Q_{T_{up}}$')
plt.axhline(y=Qdown, color='blue', linestyle='--', label=r'$Q_{T_{down}}$')

# Draw the connecting line
if len(red_intersections) > 0 and len(blue_intersections) > 0:
    plt.plot([t_up_1, t_down_2], [Q_up_1, Q_down_2], color='green', linestyle='-', linewidth=2, label='$Q_T(t)$')

plt.xlabel('t [day]', size = 15)
plt.ylabel('Q(t) [m³/s]', size = 15)
plt.legend()

if len(red_intersections) > 0 and len(blue_intersections) > 0:
    m = (Q_down_2 - Q_up_1) / (t_down_2 - t_up_1)
    c = Q_up_1 - m * t_up_1
    print(f"Equation of the connecting line: Q(t) = {m:.4f} * t + {c:.4f}")
    
def qt1(t):
    return -46.2490 * t + 552.1974    
    
time1 = []
flow = []
Q_T = []
for i, t in enumerate(time):
    qt1_value = qt1(t)  
    if Flow[i] >= qt1_value:
        flow.append(Flow[i])
        time1.append(t-3*time_increment)
        Q_T.append(qt1_value)
          

time1 = np.array(time1)
flow = np.array(flow)
Q_T = np.array(Q_T)

plt.gca().spines['left'].set_color('black')   
plt.gca().spines['bottom'].set_color('black') 
plt.gca().spines['right'].set_color('black')   
plt.gca().spines['top'].set_color('black')  

plt.fill_between(time1,flow,Q_T, where=flow>=Q_T, facecolor ='cornflowerblue')

    
plt.text(5.3,Qdown,'$Q_{T_{down}}$', size = 15)
plt.text(5.3,Qup,'$Q_{T_{up}}$', size = 15)
    
plt.text(0.8,230,'$Q_T(t)$ = ' '- 46.2490$* t$' + ' + 552.1974'   '  $\Rightarrow$  ' + '$FEV$ ≈ '+ '9.11' +'Mm$^3$', size=15)


