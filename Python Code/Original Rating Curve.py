import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

df = pd.read_csv(r'C:\Users\macha\Documents\Uni\Year 3\Project in Maths\Ouse Data\2015 Stage and Flow Data.csv')
stage_vr = df["Viking Stage"].values  
discharge_vr = df["Viking Flow"].values  

def rating_curve(h, c, b, a):
    return c * (h - a) ** b

a_guess = min(stage_vr)  
p0 = [1, 1, a_guess] 

params, covariance = curve_fit(rating_curve, stage_vr, discharge_vr, p0=p0)

c_fitted, b_fitted, a_fitted = params

stage_range = np.linspace(min(stage_vr), max(stage_vr), 100)  
fitted_discharge = rating_curve(stage_range, c_fitted, b_fitted, a_fitted)

plt.figure(figsize=(10, 5))
plt.scatter(stage_vr, discharge_vr, label="Observed Data", color="blue", s=20, marker = 'x')
plt.plot(stage_range, fitted_discharge, label= 'Rating Curve', color="red")
plt.xlabel("Stage (m)", fontsize=11,fontweight="bold", labelpad = 10)
plt.ylabel("Discharge (m³/s)", fontsize=11, fontweight="bold", labelpad = 6)
plt.legend()
plt.grid()
plt.show()

print(f"Estimated Rating Curve: Q = {c_fitted:.2f} (h - {a_fitted:.2f})^{b_fitted:.2f}")

residuals = discharge_vr - rating_curve(stage_vr, *params)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((discharge_vr - np.mean(discharge_vr))**2)
r2 = 1 - (ss_res / ss_tot)
print(r2)


residuals = discharge_vr - rating_curve(stage_vr, *params)
squared_residuals = residuals ** 2
mean_squared_residuals = np.mean(squared_residuals)
rmse = np.sqrt(mean_squared_residuals)

print(rmse)

