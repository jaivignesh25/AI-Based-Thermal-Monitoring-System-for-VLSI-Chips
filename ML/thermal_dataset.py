import numpy as np
import pandas as pd

np.random.seed(42)

data = []

for _ in range(5000):

    # Current temperature
    current_temp = np.random.randint(30, 101)

    # Temperature change
    temp_change = np.random.randint(-5, 6)

    # Previous temperature
    previous_temp = current_temp - temp_change

    # Future temperature
    future_change = np.random.randint(-3, 9)
    future_temp = current_temp + future_change

    # Thermal severity
    if current_temp > 75:
        thermal_status = 2
    elif current_temp > 60:
        thermal_status = 1
    else:
        thermal_status = 0

    # Temperature trend
    if temp_change > 0:
        trend = 0          # Heating
    elif temp_change < 0:
        trend = 2          # Cooling
    else:
        trend = 1          # Normal

    # Future hotspot
    if future_temp > 75:
        hotspot = 1
    else:
        hotspot = 0

    data.append([
        current_temp,
        previous_temp,
        temp_change,
        thermal_status,
        trend,
        future_temp,
        hotspot
    ])


columns = [
    "current_temp",
    "previous_temp",
    "temp_change",
    "thermal_status",
    "trend",
    "future_temp",
    "hotspot"
]


df = pd.DataFrame(data, columns=columns)

df.to_csv("thermal_dataset.csv", index=False)

print("Dataset generated successfully!")
print("Number of samples:", len(df))
print()
print(df.head(10))