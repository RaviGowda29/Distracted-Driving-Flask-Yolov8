import argparse
import io
import os
import time
import cv2
import numpy as np
from flask import Flask, render_template, request, redirect, send_file, Response
from werkzeug.utils import secure_filename
from PIL import Image
from ultralytics import YOLO

app = Flask(__name__)

# Initialize YOLO model
# 1.Download Your Model Weights: You can train your own model using the provided dataset, or use a pre-trained model available from the Ultralytics YOLO repository.
# 2.Place the Model Weights: After obtaining the `best.pt` file, place it in the root directory of the project where the application code is located.
model = YOLO('The application uses a pre-trained model weights file named `best.pt`')

@app.route("/", methods=["GET", "POST"])
def predict_img():
    if request.method == "POST":
        if 'file' in request.files:
            f = request.files['file']
            basepath = os.path.dirname(__file__)
            filepath = os.path.join(basepath, "uploads", secure_filename(f.filename))
            f.save(filepath)

            file_extension = f.filename.rsplit('.', 1)[1].lower()
            if file_extension in ['jpg', 'jpeg', 'png']:
                img = cv2.imread(filepath)
                results = model(img)
                # Optional: Save results or process further as needed
            elif file_extension == 'mp4':
                video_path = filepath
                cap = cv2.VideoCapture(video_path)
                frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (frame_width, frame_height))
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    results = model(frame)
                    res_plotted = results[0].plot()
                    out.write(res_plotted)
                cap.release()
                out.release()
                return redirect(url_for('video_feed'))

    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(get_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

def get_frame():
    video = cv2.VideoCapture('output.mp4')
    while True:
        success, image = video.read()
        if not success:
            break
        ret, jpeg = cv2.imencode('.jpg', image)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
    video.release()

@app.route("/live_feed")
def live_feed():
    return Response(generate_live_feed(), mimetype='multipart/x-mixed-replace; boundary=frame')

def generate_live_feed():
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        res_plotted = results[0].plot()
        ret, jpeg = cv2.imencode('.jpg', res_plotted)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
    cap.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", type=str, default="web", help="Mode of the application: web or live_camera")
    args = parser.parse_args()

    if args.mode == "live_camera":
        process_live_camera()
    else:
        app.run(debug=True)
