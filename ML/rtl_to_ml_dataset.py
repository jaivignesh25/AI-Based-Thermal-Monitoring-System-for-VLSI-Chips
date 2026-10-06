import pandas as pd
import numpy as np

# ============================================================
# RTL-STYLE THERMAL DATASET GENERATOR
# ============================================================

np.random.seed(42)

samples = []

def add_sequence(start_temp, steps):
    """
    Generate a thermal sequence similar to the RTL sensor.
    steps = list of temperature changes.
    """

    temp = start_temp

    for step in steps:
        previous_temp = temp

        # Same saturation behavior as RTL
        temp = temp + step
        temp = max(0, min(255, temp))

        temp_change = temp - previous_temp

        # RTL thermal status
        if temp > 75:
            thermal_status = 2       # CRITICAL
        elif temp > 60:
            thermal_status = 1       # WARNING
        else:
            thermal_status = 0       # NORMAL

        # RTL trend encoding
        if temp_change > 0:
            trend = 0                # HEATING
        elif temp_change < 0:
            trend = 2                # COOLING
        else:
            trend = 1                # NORMAL

        samples.append({
            "current_temp": temp,
            "previous_temp": previous_temp,
            "temp_change": temp_change,
            "thermal_status": thermal_status,
            "trend": trend
        })


# ============================================================
# 1. NORMAL TEMPERATURE SEQUENCES
# ============================================================

for _ in range(20):

    start = np.random.randint(35, 56)

    steps = np.random.choice(
        [-2, -1, 0, 1, 2],
        size=np.random.randint(8, 15)
    )

    add_sequence(start, steps)


# ============================================================
# 2. HEATING TO HOTSPOT
# ============================================================

for _ in range(25):

    start = np.random.randint(50, 66)

    steps = [3] * np.random.randint(8, 15)

    add_sequence(start, steps)


# ============================================================
# 3. COOLING FROM HOTSPOT
# ============================================================

for _ in range(20):

    start = np.random.randint(76, 91)

    steps = [-3] * np.random.randint(6, 12)

    add_sequence(start, steps)


# ============================================================
# 4. STABLE HIGH TEMPERATURE
# ============================================================

for _ in range(15):

    start = np.random.randint(76, 91)

    steps = [0] * np.random.randint(5, 10)

    add_sequence(start, steps)


# ============================================================
# 5. HEATING + COOLING CYCLES
# ============================================================

for _ in range(20):

    start = np.random.randint(45, 61)

    steps = (
        [3] * np.random.randint(5, 10)
        + [0] * np.random.randint(2, 5)
        + [-3] * np.random.randint(5, 10)
        + [3] * np.random.randint(5, 10)
    )

    add_sequence(start, steps)


# ============================================================
# CREATE DATAFRAME
# ============================================================

df = pd.DataFrame(samples)

# ------------------------------------------------------------
# Create future temperature
# ------------------------------------------------------------

df["future_temp"] = df["current_temp"].shift(-1)

# Remove final row because it has no future temperature
df = df.dropna()

# ------------------------------------------------------------
# AI TARGET
#
# Predict whether NEXT temperature becomes > 75°C
# ------------------------------------------------------------

df["hotspot"] = (df["future_temp"] > 75).astype(int)


# ============================================================
# SAVE DATASET
# ============================================================

df.to_csv("rtl_ml_dataset.csv", index=False)


# ============================================================
# DISPLAY RESULTS
# ============================================================

print()
print("==========================================")
print(" RTL-BASED ML DATASET CREATED")
print("==========================================")

print()
print("Total Samples:", len(df))

print()
print("Dataset Preview:")
print(df.head(20))

print()
print("==========================================")
print("HOTSPOT DISTRIBUTION")
print("==========================================")

print(df["hotspot"].value_counts())

print()
print("==========================================")
print("TREND DISTRIBUTION")
print("==========================================")

print(df["trend"].value_counts())

print()
print("==========================================")
print("THERMAL STATUS DISTRIBUTION")
print("==========================================")

print(df["thermal_status"].value_counts())

print()
print("Saved as:")
print("rtl_ml_dataset.csv")