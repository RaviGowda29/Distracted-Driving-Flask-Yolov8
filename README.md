Distracted-Driving-Flask-Yolov8


This project utilizes YOLOv8 for real-time object detection and classification to identify distracted driving behaviors. The application is built on Flask and requires a pre-trained model (best.pt) to perform predictions on images and videos.

Table of Contents

    Installation
    Setup
    Model Download
    Project Structure
    Usage

    
Installation

1. Clone the repository

bash

git clone https://github.com/your-username/Distracted-Driving-Flask-Yolov8.git
cd Distracted-Driving-Flask-Yolov8

2. Set up the environment

To ensure consistency, we recommend creating a virtual environment:

bash

# For Unix/macOS
python3 -m venv env
source env/bin/activate

# For Windows
python -m venv env
env\Scripts\activate

3. Install the dependencies

After activating the environment, install the dependencies:

bash

pip install -r requirements.txt

4. Download and Add YOLOv8 Model

Download the pre-trained YOLOv8 model (best.pt). Place it in the project’s root directory:

    Model Path: Place best.pt in the same directory as app.py.

    Note: The best.pt model is necessary for detection and classification tasks.

Project Structure

Below is an overview of the main project files:

bash

├── app.py                    # Main Flask application file
├── data.yaml                 # YOLOv8 data configuration
├── index.html                # Web application interface (HTML)
├── style.css                 # Styling for the interface
├── requirements.txt          # Python dependencies
├── yolov8_training_and_export.ipynb   # Jupyter notebook for training and exporting YOLOv8 model
├── best.pt                   # YOLOv8 model (to be added by the user) # Upload Ur Trained resulted Model

Usage

    Run the Flask Application: Start the Flask server after ensuring all dependencies are installed and the model file (best.pt) is in place.

    bash

python app.py 

Access the Web Interface: Open your browser and navigate to http://127.0.0.1:5000 to interact with the application.

Additional Notes

    The yolov8_training_and_export.ipynb notebook is provided for custom YOLOv8 model training and exporting, if required.
    You may update data.yaml as per your class configurations.
