from flask import Flask, request, jsonify
import cv2
import numpy as np
from measurement import measure_object
from anomaly import detect_anomaly

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Inspection System Running"

@app.route("/inspect", methods=["POST"])
def inspect():

    file = request.files["image"]
    
    file_bytes = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    width, height, dimension_status = measure_object(image)
    anomaly_status = detect_anomaly(image)

    if dimension_status == "OK" and anomaly_status == "NO DEFECT":
        final_status = "PASS"
    else:
        final_status = "FAIL"

    result = {
        "width": width,
        "height": height,
        "dimension_result": dimension_status,
        "anomaly_status": anomaly_status,
        "final_status": final_status
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)

    from flask import Flask, request, jsonify, render_template
import os
from main import run_inspection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/inspect", methods=["POST"])
def inspect():
    file = request.files["image"]
    
    filepath = os.path.join("images", file.filename)
    file.save(filepath)

    result = run_inspection(filepath)

    return jsonify(result)

if __name__ == "__main__":
    app.run()