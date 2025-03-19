import matplotlib.pyplot as plt
import pandas as pd

Data = pd.read_csv(r'C:\Users\macha\Documents\Uni\Year 3\Project in Maths\Ouse Data\Comparing stage at Viking and Skelton.csv')
time = Data['Day']
VikingStage = Data['Viking Stage']
SkeltonStage = Data['Skelton Stage'] 

plt.figure(figsize=(10,5))
plt.plot(time, VikingStage, label = "Viking Recorder Stage",
         linestyle = "-", linewidth = 2.5)
plt.plot(time, SkeltonStage, label = "Skelton Recorder Stage",
         linestyle = "-", linewidth = 2.5)

plt.xlabel("Time (days)", fontsize=11, fontweight="bold", labelpad = 6)
plt.ylabel("Stage (m)", fontsize=11,fontweight="bold", labelpad = 10)
plt.legend(fontsize=11)
plt.xticks(rotation=45) 
plt.grid(True)

