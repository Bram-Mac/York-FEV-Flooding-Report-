import matplotlib.pyplot as plt
import numpy as np

mitigations = ['Completed', 'Raised Flood Walls','Flood Storage Basin','SuDS', 'Tree Planting']
price = [89077, 144110,175394,6250000,2860000]
colour = ['#ffb3ba', '#b3cde3','#FFB347','#D8BFD8', '#c2f0c2']


fig, ax = plt.subplots(figsize=(16, 9)) 
ax.bar(mitigations,price,0.5, color = colour)
ax.set_xlabel('Mitigation Strategy', fontweight = 'bold', fontsize = 25, labelpad = 15)
ax.set_ylabel('Price per 1% of FEV Mitigated (£)', fontweight = 'bold', fontsize = 25, labelpad = 10)
ax.set_yticks(np.linspace(1000000,6000000,6))
ax.set_yticklabels(['1M','2M','3M','4M','5M','6M'],fontsize = 17)
ax.set_xticklabels(mitigations, fontsize = 17)

