from flask import Flask, render_template, request
import cv2
import os

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

    width, height, _ = measure_object(path)

    dim_result = check_dimensions(width, height)

    anomaly_status, _ = detect_anomaly(path)

    final_status = "PASS"

    if dim_result == "NOT OK" or anomaly_status == "DEFECT DETECTED":
        final_status = "FAIL"

    save_result(width, height, final_status)

    return f"""
    Width: {width:.2f} mm <br>
    Height: {height:.2f} mm <br>
    Dimension Result: {dim_result} <br>
    Anomaly: {anomaly_status} <br>
    <h2>Final Result: {final_status}</h2>
    """


if __name__ == "__main__":
    app.run(debug=True)