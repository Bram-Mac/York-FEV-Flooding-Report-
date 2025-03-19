from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file_path = r'C:\Users\macha\Documents\Uni\Year 3\Project in Maths\Ouse Data\2015 Stage and Flow Data.csv'
df = pd.read_csv(file_path)

stage_vr = df["Viking Stage"].values
discharge_vr = df["Viking Flow"].values

dh_dt = np.diff(stage_vr, prepend=stage_vr[0])

rising_indices = np.where(dh_dt > 0)[0]
falling_indices = np.where(dh_dt < 0)[0]

stage_rising = stage_vr[rising_indices]
discharge_rising = discharge_vr[rising_indices]

stage_falling = stage_vr[falling_indices]
discharge_falling = discharge_vr[falling_indices]

plt.figure(figsize=(10, 6))
plt.scatter(stage_rising, discharge_rising, label="Rising Limb Data",
            color="red", s=10, marker='x', alpha=0.5)
plt.scatter(stage_falling, discharge_falling, label="Falling Limb Data",
            color="green", s=10, marker='x', alpha=0.5)
plt.xlabel("Stage (m)", fontsize=11, fontweight="bold", labelpad=10)
plt.ylabel("Discharge (m³/s)", fontsize=11, fontweight="bold", labelpad=6)
plt.legend()
plt.grid()


def power_law(h, a, b, h0):
    return a * (h - h0) ** b


poly_degree = 6

poly_coeffs = np.polyfit(stage_rising, discharge_rising, poly_degree)
poly_fit = np.poly1d(poly_coeffs)


print("Rising limb (degree 8 polynomial) equation:")
poly_equation = "Q = " + " + ".join([f"{coef:.5f} * h^{poly_degree - i}" for i, coef in enumerate(poly_coeffs)])
print(poly_equation)

h0_falling = np.min(stage_falling)
p0_falling = [np.mean(discharge_falling), 2, h0_falling]  # Initial guess
params_falling, _ = curve_fit(power_law, stage_falling, discharge_falling, p0=p0_falling, maxfev=10000)

a_fall, b_fall, h0_fall = params_falling
print(f"Falling limb (power-law) equation: Q = {a_fall:.5f} * (h - {h0_fall:.5f})^{b_fall:.5f}")

h_range = np.linspace(min(stage_vr), max(stage_vr), 300)

Q_rising_fit = poly_fit(h_range)  # Polynomial fit for rising limb
Q_falling_fit = power_law(h_range, *params_falling)  # Power-law for falling limb

plt.figure(figsize=(10, 6))

plt.scatter(stage_rising, discharge_rising, color= 'red', s=5, label='Rising Limb Data', marker='o')
plt.scatter(stage_falling, discharge_falling, color= 'green', s=5, label='Falling Limb Data', marker='o')

plt.plot(h_range, Q_rising_fit, 'r--', label='Rising Fit')
plt.plot(h_range, Q_falling_fit, 'g--', label='Falling Fit')

plt.xlabel('Stage (m)')
plt.ylabel('Discharge (m³/s')
plt.legend()
plt.grid(True)

# Compute predicted values for rising and falling limbs
Q_rising_pred = poly_fit(stage_rising)
Q_falling_pred = power_law(stage_falling, *params_falling)

# Compute RMSE manually
rmse_rising = np.sqrt(np.mean((discharge_rising - Q_rising_pred) ** 2))
rmse_falling = np.sqrt(np.mean((discharge_falling - Q_falling_pred) ** 2))

print(rmse_rising)
print(rmse_falling)
