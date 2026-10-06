import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ============================================================
# LOAD DATASET
# ============================================================

DATASET = "rtl_ml_dataset.csv"
MODEL_FILE = "rtl_thermal_hotspot_model.pkl"

df = pd.read_csv(DATASET)

print("==========================================")
print(" RTL-BASED THERMAL AI TRAINING")
print("==========================================")

print()
print("Total samples:", len(df))

# ============================================================
# FEATURES
# ============================================================

features = [
    "current_temp",
    "previous_temp",
    "temp_change",
    "thermal_status",
    "trend"
]

X = df[features]
y = df["hotspot"]

print()
print("Features:")
print(features)

print()
print("Target:")
print("hotspot")

print()
print("Class distribution:")
print(y.value_counts())

# ============================================================
# TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print()
print("Training samples:", len(X_train))
print("Testing samples :", len(X_test))

# ============================================================
# RANDOM FOREST
# ============================================================

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=6,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# ============================================================
# PREDICTION
# ============================================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print()
print("==========================================")
print("MODEL PERFORMANCE")
print("==========================================")

print()
print(f"Accuracy: {accuracy * 100:.2f}%")

print()
print("Classification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=["NORMAL", "HOTSPOT"],
    zero_division=0
))

print()
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ============================================================
# FEATURE IMPORTANCE
# ============================================================

print()
print("==========================================")
print("FEATURE IMPORTANCE")
print("==========================================")

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance.to_string(index=False))

# ============================================================
# SAVE MODEL
# ============================================================

joblib.dump(model, MODEL_FILE)

print()
print("==========================================")
print("MODEL SAVED")
print("==========================================")

print(MODEL_FILE)