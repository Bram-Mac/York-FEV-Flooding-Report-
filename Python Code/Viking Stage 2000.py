import matplotlib.pyplot as plt
import pandas as pd

Data = pd.read_csv(r'C:\Users\macha\Documents\Uni\Year 3\Project in Maths\Ouse Data\2000 Stage and Flow Data.csv')
time = Data['Day']
VikingStage = Data['Viking Stage']
SkeltonStage = Data['Skelton Stage']

plt.figure(figsize=(10,5))

plt.plot(time, SkeltonStage, label = "Skelton Recorder Stage",
         linestyle = "-", linewidth = 2.5, color = "#ff7f0eff")
plt.plot(time, VikingStage, label = "Viking Recorder Stage",
         linestyle = "-", linewidth = 2.5)


plt.xlabel("Time (days)", fontsize=11, fontweight="bold")
plt.ylabel("Stage (m)", fontsize=11,fontweight="bold", labelpad = 10)
plt.legend()
plt.grid(True)

