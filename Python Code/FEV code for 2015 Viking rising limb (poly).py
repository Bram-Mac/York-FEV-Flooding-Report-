
ht = 4.57

p = [-381.71514, 12824.94386, -187271.92939, 1552352.23483,
     -7990127.78084, 26151800.13352, -53159626.22415,
     61366729.01755, -30805740.47068] # 8

#You do not have to change the following.
import matplotlib.pyplot as plt
import pandas as pd
import bisect
import numpy as np
fig, ax = plt.subplots()

Data = pd.read_csv(r'C:\Users\macha\Documents\Uni\Year 3\Project in Maths\Ouse Data\2015 Stage and Flow Data.csv')
time = Data['Day']
height = Data['Viking Stage']
Flow = Data['Viking Flow']

plt.rcParams["figure.figsize"] = [10,8]
plt.rcParams['axes.edgecolor']='white'
ax.spines['left'].set_position(('center'))
ax.spines['bottom'].set_position(('center'))
ax.spines['left'].set_color('black')
ax.spines['bottom'].set_color('black')

time_increment = (time[1]-time[0])*24*3600

number_of_days = round((len(time)*(time[1]-time[0])))

def scale(x):
    return ((x-min(x))/(max(x)-min(x)))
scaledtime=scale(time)
scaledheight=scale(height)
scaledFlow=scale(Flow)

def Q(x):
    return np.polyval(p, x)  # Use polynomial function for discharge

qt = Q(ht)     
    
RCFlow = []
for i in height:
    RCFlow.append(Q(i))

RCscaledFlow = []
for i in RCFlow:
    RCscaledFlow.append((i-min(RCFlow))/(max(RCFlow)-min(RCFlow)))

negheight = -(scaledheight)
negday = -(scaledtime)


ax.plot(negheight,RCscaledFlow,'black',linewidth=2)
ax.plot([0,-1],[0,1],'cornflowerblue',linestyle='--',marker='',linewidth=2)
ax.plot(scaledtime, scaledFlow,'black',linewidth=2)
ax.plot(negheight, negday,'black',linewidth=2)

scaledht = (ht-min(height))/(max(height)-min(height))
scaledqt = (qt-min(RCFlow))/(max(RCFlow)-min(RCFlow))

QT=[]
for i in RCscaledFlow:
    i = scaledqt
    QT.append(i)

SF=np.array(scaledFlow)
e=np.array(QT)
    
ax.fill_between(scaledtime,SF,e,where=SF>=e,facecolor='cornflowerblue')

idx = np.argwhere(np.diff(np.sign(SF - e))).flatten()

f=scaledtime[idx[0]]
g=scaledtime[idx[-1]]

def unscaletime(x):
    return (((max(time)-min(time))*x)+min(time))

C=unscaletime(f)
d=unscaletime(g)

Tf=(d-C)*24

time_increment=(time[1]-time[0])*24*3600

flow = []
for i in Flow:
    if i>=qt:
        flow.append((i-qt)*(time_increment))

FEV=sum(flow)

Tfs=Tf*(60**2)

qm=(FEV/Tfs)+qt
scaledqm = (qm-min(RCFlow))/(max(RCFlow)-min(RCFlow))

hm=4.85679982
scaledhm = (hm-min(height))/(max(height)-min(height))

ax.plot([-scaledht,-scaledht],[-1,scaledqt],'black',linestyle='--',linewidth=1)
ax.plot([-scaledhm,-scaledhm],[-1,scaledqm],'black',linestyle='--',linewidth=1)
ax.plot([-scaledht,1],[scaledqt,scaledqt],'black',linestyle='--',linewidth=1)
ax.plot([-scaledhm,1],[scaledqm,scaledqm],'black',linestyle='--',linewidth=1)

ax.plot([f,f,f],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([g,g,g],[scaledqt,scaledqm,-1/5], 'black', linestyle='--', linewidth=1)
ax.plot([f,f],[scaledqm,scaledqt], 'black',linewidth=1.5)
ax.plot([f,g],[scaledqm,scaledqm], 'black',linewidth=1.5)
ax.plot([f,g],[scaledqt,scaledqt], 'black',linewidth=1.5)
ax.plot([g,g],[scaledqm,scaledqt], 'black',linewidth=1.5)
plt.annotate(text='', xy=(f-1/100,-1/5), xytext=(g+1/100,-1/5), arrowprops=dict(arrowstyle='<->'))

h=[]
for i in np.arange(1,number_of_days+1):
    h.append(i/number_of_days)


l=np.arange(0,max(Flow)+50,50)
m=bisect.bisect(l,min(Flow))

n=[]
for i in np.arange(l[m],max(Flow)+50,50):
    n.append(int(i))


o=np.arange(0,max(height)+0.5,0.5)
p=bisect.bisect(o,min(height))

q=[]
for i in np.arange(o[p],max(height)+0.5,0.5):
    q.append(i)

k=[]
for i in q:
    k.append(-(i-min(height))/(max(height)-min(height))) 

j=[]
for i in n:
    j.append((i-min(Flow))/(max(Flow)-min(Flow)))

ticks_x=k+h

r=[]
for i in h:
    r.append(-i)

ticks_y=r+j


s=[]
for i in np.arange(1,number_of_days+1):
    s.append(i)

Ticks_x=q+s
Ticks_y=s+n
    
ax.set_xticks(ticks_x)
ax.set_yticks(ticks_y)
ax.set_xticklabels(Ticks_x)
ax.set_yticklabels(Ticks_y)

ax.tick_params(axis='x',colors='black',direction='out',length=9,width=1)
ax.tick_params(axis='y',colors='black',direction='out',length=10,width=1)

plt.text(-scaledht+1/100, -1,'$h_T$', size=13)
plt.text(-scaledhm+1/100, -1,'$h_m$', size=13)
plt.text(1, scaledqm,'$Q_m$', size=13)
plt.text(1, scaledqt,'$Q_T$', size=13)
plt.text(((f+g)/2)-1/50,-0.18,'$T_f$',size=13)

plt.text(0.01, 1.05,'$Q$ [m$^3$/s]', size=13)
plt.text(0.95, -0.17,'$t$ [day]', size=13)
plt.text(0.01, -1.09,'$t$ [day]', size=13)
plt.text(-1.1, 0.02,'$\overline {h}$ [m]', size=13)

ax.scatter(0,0,color='white')

A=round(FEV/(10**6),2)
B=round(Tf,2)
C=round(ht,2)
D=round(hm,2)
E=round(qt,2)
F=round(qm,2)

plt.text(0.4,-0.4,'$FEV$ ≈ '+ str(A) +'Mm$^3$', size=15)
plt.text(0.4,-0.475,'$T_f$ = '+ str(B) +'hrs', size=15)
plt.text(0.4,-0.55,'$h_T$ = '+ str(C) +'m', size=15)
plt.text(0.4,-0.625,'$h_m$ = '+ str(D) +'m', size=15)
plt.text(0.4,-0.7,'$Q_T$ = '+ str(E) +'m$^3$/s', size=15)
plt.text(0.4,-0.775,'$Q_m$ = '+ str(F) +'m$^3$/s', size=15)
