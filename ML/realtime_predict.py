import os
import time
import pandas as pd
import joblib


# ============================================================
# FILE PATHS
# ============================================================

CSV_FILE = (
    r"E:\VLSI projects\AI-Based Thermal Monitoring System"
    r"\ML\realtime_thermal.csv"
)

MODEL_FILE = (
    r"E:\VLSI projects\AI-Based Thermal Monitoring System"
    r"\ML\rtl_thermal_hotspot_model.pkl"
)


# ============================================================
# DELETE OLD CSV
# ============================================================

def delete_old_csv():

    if os.path.exists(CSV_FILE):

        try:
            os.remove(CSV_FILE)

            print("Old thermal CSV deleted.")

        except PermissionError:

            print(
                "ERROR: Cannot delete old CSV."
            )

            print(
                "Make sure Vivado is not currently using realtime_thermal.csv."
            )

            return False

    return True


# ============================================================
# HEADER
# ============================================================

print("==========================================")
print(" REAL-TIME VLSI THERMAL AI MONITOR")
print("==========================================")
print()


# ============================================================
# CLEAN PREVIOUS DATA
# ============================================================

print("Cleaning previous thermal data...")

if not delete_old_csv():

    print()
    print("Monitoring cannot start.")
    raise SystemExit


print("Previous data cleared.")
print()


# ============================================================
# LOAD AI MODEL
# ============================================================

print("Loading AI model...")

try:

    model = joblib.load(MODEL_FILE)

except Exception as e:

    print(f"ERROR: Could not load AI model: {e}")

    raise SystemExit


print("AI model loaded.")
print()


# ============================================================
# WAIT FOR NEW VIVADO CSV
# ============================================================

print("Waiting for NEW Vivado thermal data...")
print()
print("Start Vivado Behavioral Simulation now.")
print()


while not os.path.exists(CSV_FILE):

    time.sleep(0.05)


# ============================================================
# NEW CSV DETECTED
# ============================================================

print()
print("NEW Vivado thermal CSV detected!")
print()

print("Starting real-time monitoring...")
print()


# ============================================================
# TRACK PROCESSED DATA
# ============================================================

processed_time = None


# ============================================================
# REAL-TIME MONITORING
# ============================================================

try:

    while True:

        # ----------------------------------------------------
        # READ CSV
        # ----------------------------------------------------

        try:

            df = pd.read_csv(CSV_FILE)

        except (
            pd.errors.EmptyDataError,
            PermissionError,
            FileNotFoundError
        ):

            time.sleep(0.05)

            continue


        # ----------------------------------------------------
        # EMPTY CSV
        # ----------------------------------------------------

        if len(df) == 0:

            time.sleep(0.05)

            continue


        # ----------------------------------------------------
        # FIND NEW ROWS
        # ----------------------------------------------------

        new_rows = []

        for _, row in df.iterrows():

            simulation_time = int(row["time"])

            if (
                processed_time is None
                or simulation_time > processed_time
            ):

                new_rows.append(row)


        # ====================================================
        # PROCESS NEW ROWS
        # ====================================================

        for row in new_rows:

            simulation_time = int(row["time"])


            # ------------------------------------------------
            # THREE THERMAL ZONES
            # ------------------------------------------------

            zone1 = float(row["zone1"])

            zone2 = float(row["zone2"])

            zone3 = float(row["zone3"])


            # ------------------------------------------------
            # CURRENT MODEL
            #
            # Current trained model uses Zone 3.
            # ------------------------------------------------

            current_temp = zone3

            temp_change = float(
                row["temp_change"]
            )

            previous_temp = (
                current_temp - temp_change
            )

            thermal_status = int(
                row["status"]
            )

            trend = int(
                row["trend"]
            )


            # ------------------------------------------------
            # ML INPUT
            # ------------------------------------------------

            input_data = pd.DataFrame([
                {
                    "current_temp": current_temp,

                    "previous_temp": previous_temp,

                    "temp_change": temp_change,

                    "thermal_status": thermal_status,

                    "trend": trend
                }
            ])


            # ------------------------------------------------
            # AI PREDICTION
            # ------------------------------------------------

            prediction = model.predict(
                input_data
            )[0]

            probability = (
                model.predict_proba(
                    input_data
                )[0][1] * 100
            )


            # =================================================
            # THERMAL STATUS
            # =================================================

            if thermal_status == 0:

                status_name = "NORMAL"

            elif thermal_status == 1:

                status_name = "WARNING"

            elif thermal_status == 2:

                status_name = "CRITICAL"

            else:

                status_name = "UNKNOWN"


            # =================================================
            # TREND
            # =================================================

            if trend == 0:

                trend_name = "HEATING"

            elif trend == 1:

                trend_name = "NORMAL"

            elif trend == 2:

                trend_name = "COOLING"

            else:

                trend_name = "UNKNOWN"


            # =================================================
            # AI RESULT
            # =================================================

            if prediction == 1:

                prediction_name = "HOTSPOT RISK"

            else:

                prediction_name = "NORMAL"


            # =================================================
            # REAL-TIME OUTPUT
            # =================================================

            print(
                f"Time={simulation_time} ns | "
                f"Zone1={zone1:.0f}°C | "
                f"Zone2={zone2:.0f}°C | "
                f"Zone3={zone3:.0f}°C | "
                f"Change={temp_change:+.0f}°C | "
                f"Status={status_name} | "
                f"Trend={trend_name} | "
                f"AI={prediction_name} | "
                f"Probability={probability:.2f}%",
                flush=True
            )


            # ------------------------------------------------
            # MARK ROW AS PROCESSED
            # ------------------------------------------------

            processed_time = simulation_time


        # ----------------------------------------------------
        # POLLING INTERVAL
        # ----------------------------------------------------

        time.sleep(0.02)


# ============================================================
# TERMINATION
# ============================================================

except KeyboardInterrupt:

    print()
    print()
    print("Stopping real-time monitoring...")


# ============================================================
# DELETE CSV AFTER TERMINATION
# ============================================================

finally:

    print()

    print("Deleting thermal CSV...")

    try:

        if os.path.exists(CSV_FILE):

            os.remove(CSV_FILE)

            print("Thermal CSV deleted successfully.")

        else:

            print("Thermal CSV already removed.")

    except PermissionError:

        print(
            "WARNING: Could not delete CSV."
        )

        print(
            "Close Vivado simulation and delete it manually."
        )


    print()

    print("==========================================")
    print(" THERMAL MONITORING STOPPED")
    print("==========================================")