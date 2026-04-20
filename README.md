AI-Based Surface Defect Detection & Measurement System for Iron Materials
Project Overview
This project implements an AI-based system to detect and analyze surface defects in iron materials using computer vision techniques.
Unlike basic classification projects, this system not only identifies whether a surface is defective but also:

highlights defect regions using heatmaps
estimates material size using pixel-based calibration

The goal is to demonstrate a practical approach toward automated inspection in manufacturing environments.

Key Features
Defect detection using a CNN-based model
Heatmap visualization to highlight defect regions
Pixel calibration for approximate defect size measurement
Flask-based web interface for easy interaction
End-to-end pipeline from image input to analysis
Tech Stack
Python
TensorFlow / Keras – model training
OpenCV – image processing & measurement
NumPy – numerical operations
Flask – web application
System Workflow
Input Image 
   ↓
Preprocessing (Resize, Normalize)
   ↓
CNN Model Prediction
   ↓
Heatmap Generation (Defect Localization)
   ↓
Pixel Calibration (Size Estimation)
   ↓
Result Display (UI)
📂 Project Structure
├── app.py                  # Main Flask application
├── model/
│   └── model.h5           # Trained CNN model
├── utils/
│   ├── heatmap.py        # Heatmap generation logic
│   └── measurement.py    # Pixel calibration & size estimation
├── static/
│   └── uploads/
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
Installation & Setup
1. Clone Repository
git clone https://github.com/Naviket-aggarwal/automated-iron-defect-detection-using-ai .git
2. Install Dependencies
pip install -r requirements.txt
3. Run Application
python app.py
4. Open in Browser
http://127.0.0.1:5000/
Model Details
Model Type: Convolutional Neural Network (CNN)
Task: Binary classification (Defective / Non-Defective)
Input: Iron surface images
Output: Prediction + visual explanation

The model learns visual patterns such as cracks, rust, and irregular textures from training data.

Heatmap Visualization

The system generates heatmaps to highlight regions in the image that contribute most to the prediction.

This helps in:

understanding model decisions
locating defect areas visually
improving interpretability of results
Defect Measurement (Pixel Calibration)

A basic measurement system is implemented using pixel calibration:

Pixel-to-real-world ratio is estimated
measurment is calculated using iron scale per pixel
Approximate size of material is calculated

This provides a rough estimation of metal dimensions, which can be useful for inspection purposes.

Results
Successfully detects defective vs non-defective surfaces
Heatmaps correctly highlight defect regions in most cases
Measurement system provides approximate size estimation

Performance depends on dataset quality and calibration accuracy.

Example Use Case
Upload an image of an iron surface
System detects defect presence
Heatmap shows defect location
Approximate material size is displayed
Applications
Metal and steel industries
Automated quality inspection systems
Manufacturing process monitoring
Future Improvements
Multi-class defect classification
More accurate measurement using calibrated hardware
Real-time camera integration
Deployment on edge devices (Jetson Nano / Raspberry Pi)
Limitations
Measurement is approximate (depends on calibration accuracy)
Model performance limited by dataset size
Works best on clear and well-lit images
