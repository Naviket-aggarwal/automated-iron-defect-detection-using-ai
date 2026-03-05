from flask import Flask, render_template, request
import cv2
import os
import base64

from measurement import measure_object
from anomaly import detect_anomaly
from inspection import check_dimensions
from logger import save_result

app = Flask(__name__)

UPLOAD_FOLDER = "images"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/inspect", methods=["POST"])
def inspect():

    file = request.files["image"]

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    # Measure dimensions
    width, height, _ = measure_object(path)

    # Dimension check
    dim_result = check_dimensions(width, height)

    # Detect anomaly + heatmap
    anomaly_status, heatmap, confidence = detect_anomaly(path)

    # Final decision
    final_status = "PASS"

    if dim_result == "NOT OK" or anomaly_status == "DEFECT DETECTED":
        final_status = "FAIL"

    # Save log
    save_result(width, height, final_status)

    # Convert heatmap to web format
    _, buffer = cv2.imencode(".jpg", heatmap)
    img_base64 = base64.b64encode(buffer).decode("utf-8")

    return f"""
    <h2>Inspection Result</h2>

    Width: {width:.2f} mm <br>
    Height: {height:.2f} mm <br>
    Dimension Result: {dim_result} <br>
    Anomaly Status: {anomaly_status} <br>
    AI confidence: {confidence}% <br>

    <h2>Final Status: {final_status}</h2>

    <h3>Defect Heatmap</h3>
    <img src="data:image/jpeg;base64,{img_base64}" width="400">
    """


if __name__ == "__main__":
    app.run(debug=True)