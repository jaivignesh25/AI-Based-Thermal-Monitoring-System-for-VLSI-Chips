# AI-Based Thermal Monitoring System for VLSI Chips

<p align="center">
  <b>SystemVerilog RTL + Vivado + Python + Machine Learning</b>
</p>

<p align="center">
  An intelligent thermal monitoring system that combines VLSI RTL simulation with Machine Learning for thermal hotspot detection and prediction.
</p>

---

##  Overview

Thermal management is one of the important challenges in modern VLSI and semiconductor systems. Increasing chip temperature can affect performance, reliability, power consumption, and device lifetime.

This project presents an **AI-Based Thermal Monitoring System for VLSI Chips** that combines:

- SystemVerilog RTL design
- Digital thermal sensor modeling
- Multi-zone temperature monitoring
- Hotspot detection
- Thermal severity classification
- Temperature trend detection
- Vivado behavioral simulation
- CSV-based thermal data logging
- Python data preprocessing
- Random Forest Machine Learning
- Real-time hotspot risk prediction
- Thermal data visualization

The project demonstrates an **RTL-to-AI workflow**, where thermal information generated from the VLSI RTL simulation is transferred to a Python-based Machine Learning pipeline.

---

#  Objectives

The main objectives of this project are:

1. Model temperature variations in multiple VLSI thermal zones.
2. Design the thermal monitoring system using SystemVerilog RTL.
3. Detect thermal hotspots using threshold-based logic.
4. Classify thermal conditions as:
   - NORMAL
   - WARNING
   - CRITICAL
5. Detect temperature trends:
   - HEATING
   - NORMAL
   - COOLING
6. Generate thermal monitoring data during RTL simulation.
7. Store simulation results in CSV format.
8. Train a Machine Learning model using thermal data.
9. Predict potential hotspot risk using a Random Forest classifier.
10. Build a real-time RTL-to-Python monitoring pipeline.

---

#  System Architecture

The complete system is divided into two major sections:

```text
┌───────────────────────────────────────────────────────────────────────┐
│              VLSI RTL DESIGN AND SIMULATION                          │
│                         (Vivado)                                     │
│                                                                       │
│  ┌──────────────┐     ┌──────────────────┐     ┌─────────────────┐   │
│  │ VLSI Thermal │────►│ Temperature     │────►│ Data Aggregator │   │
│  │    Zones     │     │    Sensors      │     └────────┬────────┘   │
│  └──────────────┘     └──────────────────┘              │            │
│                                                         │            │
│                    ┌────────────────────────────────────┼────────┐   │
│                    │                                    │        │   │
│                    ▼                                    ▼        ▼   │
│            ┌───────────────┐                  ┌──────────────┐       │
│            │    Hotspot    │                  │   Thermal    │       │
│            │   Detector    │                  │   Severity   │       │
│            └───────┬───────┘                  │   Analyzer   │       │
│                    │                          └──────┬───────┘       │
│                    │                                 │               │
│                    │                          ┌──────▼───────┐       │
│                    │                          │    Trend     │       │
│                    │                          │   Detector   │       │
│                    │                          └──────┬───────┘       │
│                    │                                 │               │
│                    └──────────────┬──────────────────┘               │
│                                   ▼                                  │
│                           ┌──────────────┐                           │
│                           │ CSV Logger   │                           │
│                           │  Testbench   │                           │
│                           └──────┬───────┘                           │
│                                  ▼                                   │
│                       realtime_thermal.csv                           │
└──────────────────────────────────┬────────────────────────────────────┘
                                   │
                                   ▼
┌───────────────────────────────────────────────────────────────────────┐
│                 AI / ML PROCESSING AND MONITORING                     │
│                              (Python)                                 │
│                                                                       │
│  realtime_thermal.csv                                                │
│          │                                                            │
│          ▼                                                            │
│  ┌──────────────────┐                                                │
│  │ Data             │                                                │
│  │ Preprocessing    │                                                │
│  └────────┬─────────┘                                                │
│           ▼                                                           │
│  ┌──────────────────┐                                                │
│  │ Feature          │                                                │
│  │ Extraction       │                                                │
│  └────────┬─────────┘                                                │
│           ▼                                                           │
│  ┌──────────────────┐                                                │
│  │ Random Forest    │                                                │
│  │ Classifier       │                                                │
│  └────────┬─────────┘                                                │
│           ▼                                                           │
│  ┌──────────────────┐                                                │
│  │ Hotspot Risk     │                                                │
│  │ Prediction       │                                                │
│  └────────┬─────────┘                                                │
│           ▼                                                           │
│  ┌──────────────────┐                                                │
│  │ Real-Time AI     │                                                │
│  │ Monitor          │                                                │
│  └────────┬─────────┘                                                │
│           ▼                                                           │
│   NORMAL / HOTSPOT RISK                                               │
│   Probability + Thermal Status + Trend                               │
└───────────────────────────────────────────────────────────────────────┘
🌡️ Thermal Monitoring Zones

The RTL system models three independent thermal zones:

Zone 1
Zone 2
Zone 3

Each zone has a digital temperature sensor model.

Temperature Sensor 1 ──► Zone 1
Temperature Sensor 2 ──► Zone 2
Temperature Sensor 3 ──► Zone 3

The sensors support both positive and negative temperature changes.

The temperature is represented using an 8-bit digital value.

Temperature Range
0°C ─────────────────────────────► 255°C

Temperature values are saturated to prevent overflow or underflow.

🔧 RTL Design

The project is implemented using SystemVerilog.

RTL Modules
1. temp_sensor.sv

Models a digital temperature sensor.

Features:

Parameterized initial temperature
Positive temperature change
Negative temperature change
8-bit temperature output
Saturation between 0°C and 255°C
temp_step > 0
      ↓
Temperature increases

temp_step < 0
      ↓
Temperature decreases
2. thermal_monitor.sv

Instantiates three temperature sensors.

              ┌──────────────┐
Sensor Step 1 │ Temp Sensor  │──► temp1
─────────────►│      1       │
              └──────────────┘

              ┌──────────────┐
Sensor Step 2 │ Temp Sensor  │──► temp2
─────────────►│      2       │
              └──────────────┘

              ┌──────────────┐
Sensor Step 3 │ Temp Sensor  │──► temp3
─────────────►│      3       │
              └──────────────┘

Initial temperatures:

Sensor 1 → 25°C
Sensor 2 → 35°C
Sensor 3 → 45°C
3. data_aggregator.sv

Collects the temperature values and generates:

temp1 → zone1
temp2 → zone2
temp3 → zone3

The aggregator is implemented as a sequential RTL block.

Therefore, the zone outputs have the expected pipeline behavior relative to the sensor outputs.

4. hotspot_detector.sv

Detects whether a thermal hotspot is present.

The implemented hotspot threshold is:

Temperature > 75°C

Therefore:

Temperature ≤ 75°C
        ↓
No Hotspot

Temperature > 75°C
        ↓
Hotspot Detected

Output:

alert = 1 → Hotspot
alert = 0 → No Hotspot
5. thermal_severity.sv

Classifies the thermal condition.

Temperature	Thermal Status
≤ 60°C	NORMAL
61°C – 75°C	WARNING
> 75°C	CRITICAL

Encoding:

00 → NORMAL
01 → WARNING
10 → CRITICAL
6. trend_detector.sv

The trend detector compares the current temperature with the previous temperature.

The current implementation monitors Zone 3.

The temperature difference is calculated as:

Temperature Change =
Current Temperature - Previous Temperature

Trend encoding:

00 → HEATING
01 → NORMAL
10 → COOLING

Logic:

Current > Previous
       ↓
    HEATING


Current = Previous
       ↓
     NORMAL


Current < Previous
       ↓
    COOLING
7. thermal_system.sv

This is the top-level RTL integration module.

It connects:

thermal_monitor
       ↓
data_aggregator
       ↓
 ┌─────┼──────────────┐
 ▼     ▼              ▼
Hotspot  Severity    Trend
Detector Analyzer   Detector

The top-level module provides:

alert
thermal_status
temp_change
change
trend_valid
🧪 Testbench

The project includes a SystemVerilog testbench:

tb_thermal_system.sv

The testbench generates different thermal conditions.

Simulation Phases
Phase 1 — Initial Heating
Sensor 1 → +1
Sensor 2 →  0
Sensor 3 → +2
Phase 2 — Increased Heating
Sensor 1 → +1
Sensor 2 → +2
Sensor 3 → +3
Phase 3 — Stable Temperature
Sensor 1 → 0
Sensor 2 → 0
Sensor 3 → 0
Phase 4 — Cooling
Sensor 1 → -1
Sensor 2 → -2
Sensor 3 → -2
Phase 5 — Mixed Thermal Behavior
Sensor 1 → +2
Sensor 2 → -1
Sensor 3 → +3
Phase 6 — Stable Condition
Sensor 1 → 0
Sensor 2 → 0
Sensor 3 → 0
📊 Simulation Data Logging

The testbench records the thermal information and generates:

realtime_thermal.csv

Example data fields:

time
temp1
temp2
temp3
zone1
zone2
zone3
alert
status
temp_change
trend
trend_valid

The CSV file provides the interface between the RTL simulation and the Python Machine Learning pipeline.

 Thermal Analysis

The RTL system provides three major thermal analysis functions.

Hotspot Detection
Zone Temperature > 75°C
              ↓
       Hotspot Alert
Thermal Severity
NORMAL
   ↓
WARNING
   ↓
CRITICAL
Temperature Trend
HEATING
NORMAL
COOLING

Together, these provide a digital thermal state representation of the chip.

Machine Learning

The project uses a Random Forest Classifier to predict hotspot risk.

The Machine Learning pipeline is implemented using Python and Scikit-learn.

ML Features

The current model uses:

Current Temperature
Previous Temperature
Temperature Change
Thermal Status
Temperature Trend

The current ML feature generation is based on the Zone 3 temperature/trend path.

 Random Forest Classifier

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees.

Conceptually:

             Input Features
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
      Tree 1     Tree 2     Tree N
        │          │          │
        └──────────┼──────────┘
                   ▼
            Majority Voting
                   │
                   ▼
          Hotspot Prediction

Output:

NORMAL
     or
HOTSPOT RISK

The model also provides a probability estimate.

 Machine Learning Results

The current trained model achieved:

Accuracy = 95.20%
Classification Report
Class	Precision	Recall	F1-Score
NORMAL	0.97	0.96	0.97
HOTSPOT	0.91	0.93	0.92
Confusion Matrix
                    Predicted
                 NORMAL  HOTSPOT

Actual NORMAL       171      7

Actual HOTSPOT        5     67

This indicates that the model correctly identifies most normal and hotspot conditions in the test dataset.

Dataset

The thermal dataset was generated from the RTL simulation.

Dataset statistics:

Total Samples      : 1246
Normal Samples     : 886
Hotspot Samples    : 360
Training Samples   : 996
Testing Samples    : 250
Feature Importance

The trained model produced the following approximate feature importance:

Feature	Importance
Current Temperature	0.4262
Previous Temperature	0.2656
Thermal Status	0.2116
Temperature Change	0.0499
Trend	0.0467

This shows that the current and previous temperature values have the strongest influence on hotspot prediction in the current model.

Real-Time AI Monitoring

The project includes:

realtime_predict.py

This script connects the RTL simulation data to the trained Machine Learning model.

Working Flow
Vivado Simulation
       ↓
realtime_thermal.csv
       ↓
Python Monitor
       ↓
Read New Data
       ↓
Feature Extraction
       ↓
Random Forest Model
       ↓
Prediction
       ↓
Console Output
Real-Time Monitoring Process

The Python monitor performs the following steps:

Step 1

Deletes the previous CSV file.

Step 2

Loads the trained Machine Learning model.

rtl_thermal_hotspot_model.pkl
Step 3

Waits for a new CSV file generated by the Vivado testbench.

Step 4

Reads newly generated thermal samples.

Step 5

Extracts the required Machine Learning features.

Step 6

Runs the Random Forest prediction.

Step 7

Displays:

Zone 1 temperature
Zone 2 temperature
Zone 3 temperature
Temperature change
Thermal status
Temperature trend
AI hotspot prediction
Prediction probability
Step 8

Deletes the temporary CSV when monitoring is stopped.

Example Real-Time Output
Time=701000 ns |
Zone1=41°C |
Zone2=37°C |
Zone3=78°C |
Change=+3°C |
Status=CRITICAL |
Trend=HEATING |
AI=HOTSPOT RISK |
Probability=95.68%

This demonstrates the complete RTL-to-AI flow.

Complete Data Flow
        VLSI Thermal Model
                │
                ▼
       SystemVerilog Sensors
                │
                ▼
         Data Aggregator
                │
                ▼
    ┌───────────┼────────────┐
    │           │            │
    ▼           ▼            ▼
 Hotspot     Severity      Trend
 Detector    Analyzer     Detector
    │           │            │
    └───────────┼────────────┘
                ▼
           Testbench
                │
                ▼
     realtime_thermal.csv
                │
                ▼
       Python Preprocessing
                │
                ▼
        Feature Extraction
                │
                ▼
      Random Forest Model
                │
                ▼
       Hotspot Prediction
                │
                ▼
       Real-Time Monitor
                │
        ┌───────┼────────┐
        ▼       ▼        ▼
     Status   Trend   AI Prediction
Project Structure

Recommended repository structure:

AI-Based-Thermal-Monitoring-System-for-VLSI-Chips/
│
├── RTL/
│   ├── temp_sensor.sv
│   ├── thermal_monitor.sv
│   ├── data_aggregator.sv
│   ├── hotspot_detector.sv
│   ├── thermal_severity.sv
│   ├── trend_detector.sv
│   └── thermal_system.sv
│
├── Testbench/
│   └── tb_thermal_system.sv
│
├── ML/
│   ├── train_model.py
│   ├── realtime_predict.py
│   ├── dataset.csv
│   └── rtl_thermal_hotspot_model.pkl
│
├── Documentation/
│   ├── Architecture.png
│   └── Project_Report.docx
│
├── Results/
│   ├── simulation_results/
│   └── plots/
│
└── README.md
 Requirements
Hardware Design
AMD/Xilinx Vivado
SystemVerilog support
Behavioral simulation environment
Python

Recommended Python version:

Python 3.x

Required libraries:

pandas
numpy
scikit-learn
joblib
matplotlib
Installation

Clone the repository:

git clone https://github.com/jaivignesh25/AI-VLSI-Thermal-Monitoring

Move into the project:

cd AI-Based-Thermal-Monitoring-System-for-VLSI-Chips

Install Python dependencies:

pip install pandas numpy scikit-learn joblib matplotlib
▶️ Running the RTL Simulation
Step 1 — Open Vivado

Open the Vivado project.

Add the RTL modules:

temp_sensor.sv
thermal_monitor.sv
data_aggregator.sv
hotspot_detector.sv
thermal_severity.sv
trend_detector.sv
thermal_system.sv

Add the testbench:

tb_thermal_system.sv
Step 2 — Set Simulation Top

Set:

tb_thermal_system

as the simulation top module.

Step 3 — Run Behavioral Simulation

Run the simulation for approximately:

3500 ns

or long enough to cover all thermal phases.

The testbench generates:

realtime_thermal.csv
🤖 Training the ML Model

If the training script is included in the repository:

python ML/train_model.py

The trained model will be saved as:

rtl_thermal_hotspot_model.pkl
🚀 Running Real-Time AI Monitoring

Start the Python monitor:

python ML/realtime_predict.py

The program will display:

REAL-TIME VLSI THERMAL AI MONITOR

It will wait for new thermal data from the Vivado simulation.

Then start the Vivado behavioral simulation.

The Python program automatically detects:

realtime_thermal.csv

and starts processing new thermal samples.

Visualization

Thermal data can be visualized to analyze the behavior of the three zones over simulation time.

Typical visualization:

Temperature
    │
120 │                 Zone 3
100 │                /──────
 80 │       Zone 2  /
 60 │      /───────
 40 │ Zone 1
 20 │───────────────
    └──────────────────────► Time

The visualization helps identify:

Heating periods
Cooling periods
Stable periods
High-temperature regions
Differences between thermal zones
🔬 Verification

The system is verified by applying different temperature profiles to the three sensor models.

Verification checks include:

Reset Verification
Reset = 1
      ↓
Sensors initialized
Heating Verification
Positive temperature step
      ↓
Temperature increases
      ↓
Trend = HEATING
Cooling Verification
Negative temperature step
      ↓
Temperature decreases
      ↓
Trend = COOLING
Hotspot Verification
Temperature > 75°C
      ↓
Alert = 1
      ↓
Critical condition
Stable Temperature Verification
Temperature unchanged
      ↓
Trend = NORMAL

Key Features
✅ SystemVerilog RTL implementation
✅ Three thermal zones
✅ Parameterized digital temperature sensors
✅ Temperature saturation logic
✅ Thermal data aggregation
✅ Hotspot detection
✅ Thermal severity classification
✅ Heating / Normal / Cooling detection
✅ Vivado behavioral simulation
✅ Automated CSV logging
✅ Python data processing
✅ Random Forest Machine Learning
✅ Real-time hotspot prediction
✅ Prediction probability
✅ Thermal data visualization
✅ RTL-to-AI integration
💡 Why This Project?

Traditional threshold-based thermal monitoring can identify whether a temperature has crossed a predefined limit.

This project extends that concept by combining:

Hardware Monitoring
        +
Thermal Analysis
        +
Machine Learning
        =
Intelligent Thermal Monitoring

The AI layer provides an additional prediction mechanism that can potentially support proactive thermal management.

Future Enhancements

The following improvements can be added in future versions:

1. Fully Multi-Zone AI Prediction

Currently, the ML pipeline primarily uses the Zone 3 temperature path.

Future work can train the model using:

Zone 1
Zone 2
Zone 3

simultaneously.

2. Multi-Zone Trend Detection

The current trend detector focuses on Zone 3.

Future implementation:

Zone 1 → Trend Detector 1
Zone 2 → Trend Detector 2
Zone 3 → Trend Detector 3
3. FPGA Implementation

The RTL design can be deployed on an FPGA board.

Possible flow:

SystemVerilog
      ↓
Vivado Synthesis
      ↓
Implementation
      ↓
Bitstream
      ↓
FPGA Hardware
4. Physical Temperature Sensors

The digital sensor models can be replaced or interfaced with actual thermal sensors.

5. On-Chip Thermal Monitoring

The architecture can be extended for real semiconductor thermal monitoring applications.

6. Predictive Thermal Management

Instead of only detecting the current hotspot condition, the AI model can predict:

Future Temperature
Future Hotspot Risk

several cycles ahead.

7. Automatic Thermal Control

Future versions could automatically perform:

Hotspot Detected
       ↓
Clock Throttling
       ↓
Power Reduction
       ↓
Temperature Control
8. Advanced Machine Learning

Other algorithms can be evaluated:

Decision Tree
Support Vector Machine
XGBoost
Neural Networks
LSTM
TinyML models
📚 Learning Outcomes

This project provides practical experience in:

VLSI
RTL design
SystemVerilog
Sequential logic
Combinational logic
Module instantiation
Parameterization
Testbench development
Simulation
Thermal monitoring architecture
Machine Learning
Dataset generation
Data preprocessing
Feature extraction
Classification
Random Forest
Model evaluation
Prediction probability
Software Integration
Python
Pandas
Scikit-learn
Joblib
CSV data pipelines
Real-time file monitoring

 Project Highlights
RTL Technology      : SystemVerilog
Simulation Tool     : AMD/Xilinx Vivado
Temperature Zones   : 3
Temperature Width   : 8-bit
Hotspot Threshold   : >75°C
Warning Threshold   : 61–75°C
Normal Threshold    : ≤60°C
ML Algorithm        : Random Forest
ML Accuracy         : 95.20%
Data Interface      : CSV
AI Language         : Python


👨‍💻 Author
# Jaivignesh M
B.E. Electronics and Communication Engineering
University College of Engineering Kanchipuram
Anna University
Batch: 2023–2027
