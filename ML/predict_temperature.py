import joblib
import pandas as pd


# ==========================================
# Load RTL-trained model
# ==========================================

model = joblib.load(
    "rtl_thermal_hotspot_model.pkl"
)


print("===================================")
print("RTL-BASED AI THERMAL PREDICTOR")
print("===================================")


# ==========================================
# Get temperature inputs
# ==========================================

current_temp = float(
    input("Enter current temperature: ")
)

previous_temp = float(
    input("Enter previous temperature: ")
)


# ==========================================
# Calculate temperature change
# ==========================================

temp_change = (
    current_temp - previous_temp
)


# ==========================================
# Thermal severity
# ==========================================

if current_temp > 75:
    thermal_status = 2

elif current_temp > 60:
    thermal_status = 1

else:
    thermal_status = 0


# ==========================================
# Temperature trend
# ==========================================

if temp_change > 0:
    trend = 0          # HEATING

elif temp_change < 0:
    trend = 2          # COOLING

else:
    trend = 1          # NORMAL


# ==========================================
# Prepare ML input
# ==========================================

input_data = pd.DataFrame([
    {
        "current_temp": current_temp,
        "previous_temp": previous_temp,
        "temp_change": temp_change,
        "thermal_status": thermal_status,
        "trend": trend
    }
])


# ==========================================
# AI prediction
# ==========================================

prediction = model.predict(
    input_data
)[0]

probability = model.predict_proba(
    input_data
)[0][1]


# ==========================================
# Display information
# ==========================================

print()
print("-----------------------------------")

print(
    f"Current Temperature : "
    f"{current_temp:.1f} °C"
)

print(
    f"Previous Temperature: "
    f"{previous_temp:.1f} °C"
)

print(
    f"Temperature Change  : "
    f"{temp_change:+.1f} °C"
)


if trend == 0:
    trend_name = "HEATING"

elif trend == 1:
    trend_name = "NORMAL"

else:
    trend_name = "COOLING"


print(
    f"Trend               : "
    f"{trend_name}"
)


if thermal_status == 0:
    status_name = "NORMAL"

elif thermal_status == 1:
    status_name = "WARNING"

else:
    status_name = "CRITICAL"


print(
    f"Thermal Status      : "
    f"{status_name}"
)


print(
    f"Hotspot Probability : "
    f"{probability * 100:.2f}%"
)


if prediction == 1:
    print(
        "AI Prediction       : "
        "HOTSPOT RISK"
    )
else:
    print(
        "AI Prediction       : "
        "NORMAL"
    )


print("-----------------------------------")