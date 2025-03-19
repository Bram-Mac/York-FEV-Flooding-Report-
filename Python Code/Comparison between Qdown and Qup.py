import matplotlib.pyplot as plt
import pandas as pd


Data = pd.read_csv(r'C:\Users\macha\Documents\Uni\Year 3\Project in Maths\Ouse Data\2015 Stage and Flow Data.csv')
time = Data['Day']
height = Data['Viking Stage']
Flow = Data['Viking Flow']

plt.rcParams["figure.figsize"] = [10,8]
plt.rcParams['axes.edgecolor']='white'
plt.plot(time, Flow,'black',linewidth=2)

QT = 408.77  
QTup = 504.14
QTdown = 394.10

plt.axhline(y=QTup+4, color='red', linestyle='--', linewidth=2)
plt.axhline(y=QTdown+4, color='blue', linestyle='--', linewidth=2)
plt.axhline(y=QT+3, color='black', linestyle='--', linewidth=1)

plt.xlabel('t [day]', size = 15)
plt.ylabel('Q(t) [$m^3$/s]', size = 15)

plt.text(5.3,QTdown,'$Q_{T_{down}}$', size = 15)
plt.text(5.3,QTup,'$Q_{T_{up}}$', size = 15)
plt.text(5.3,QT,'$Q_{T}$', size = 15)


plt.gca().spines['left'].set_color('black')   
plt.gca().spines['bottom'].set_color('black') 
plt.gca().spines['right'].set_color('black')   
plt.gca().spines['top'].set_color('black')     

plt.text(1.2,260,'$Q_{T_{up}}$ ≈ '+ '504.14' +'m$^3$/s' + '  $\Rightarrow$  ' + '$FEV$ ≈ '+ '1.88' +'Mm$^3$', size=15)
plt.text(1.2,240,'$Q_T$ ≈ '+ '408.77' +'m$^3$/s' + '  $\Rightarrow$  ' + '$FEV$ ≈ '+ '17.70' +'Mm$^3$', size=15)
plt.text(1.2,220,'$Q_{T_{down}}$ ≈ '+ '394.10' +'m$^3$/s' + '  $\Rightarrow$  ' + '$FEV$ ≈ ' + '20.8' +'Mm$^3$', size=15)



