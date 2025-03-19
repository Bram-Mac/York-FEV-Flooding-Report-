import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [9,9]
plt.rcParams['axes.edgecolor']='white'

sl = 2134

plt.xlim(0,2150)
plt.ylim(0,2150)

plt.xlabel('Side length [m]', size=17)
plt.ylabel('Side length [m]',size=17)

measure=['B4 & B12: £5.505M for 61.8% of FEV']



plt.plot([0,sl],[0,0],linewidth=5,color='black')
plt.plot([0,0],[0,sl],linewidth=5,color='black')
plt.plot([sl,sl],[sl,0],linewidth=3,color='black')
plt.plot([0,sl],[sl,sl],linewidth=3,color='black')

plt.bar(659.715,sl,width=1319.43,color='orange',label="B4 & B12: £5.505M for 61.8% of FEV")
plt.bar(1420,sl,width=201.44,color='blue',label="Tree Planting: £27M for 9.44% of FEV")
plt.bar(1520,sl,width=1.71,color='red',label="SuDS: £5M for 0.08% of FEV")

ticksx=[250,500,750,1000,1250,1500,1750,2134]
ticksy=[250,500,750,1000,1250,1500,1750,2134]

plt.xticks(ticksx)
plt.yticks(ticksy)

plt.tick_params(labelsize=15)

plt.legend(bbox_to_anchor=(0.015, 0.55), loc=2, borderaxespad=0.,prop={'size': 15})