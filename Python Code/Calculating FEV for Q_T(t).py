import pandas as pd

Data = pd.read_csv(r'C:\Users\macha\Documents\Uni\Year 3\Project in Maths\Ouse Data\2015 Stage and Flow Data.csv')
time = Data['Day']
Flow = Data['Viking Flow']

time_increment = (time[1]-time[0])*24*3600

def Q_T(t):
    return -46.2490 * t + 552.1974

fev = []
for i, t in enumerate(time):
    QT_value = Q_T(t) 
    if Flow[i] >= QT_value:
        difference = (Flow[i] - QT_value) * time_increment
        fev.append(difference)

FEV=sum(fev)

print(FEV)

