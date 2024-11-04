Distracted Driving Detection with YOLOv8 and Flask

**Project Overview**  
This project leverages YOLOv8 for real-time object detection to identify distracted driving behaviors. Built using Flask, it provides a web application that utilizes a pre-trained model (`best.pt`) for predictions on images and videos.

**Components**  
1. **Object Detection**: The core functionality utilizes YOLOv8 to detect and classify various distracted driving behaviors in real time.

2. **Web Application Interface**: The application is built with Flask, allowing users to upload images or videos and view detection results through a user-friendly web interface.

3. **Model Integration**: The project requires a pre-trained YOLOv8 model (`best.pt`), which is essential for the detection tasks.

**Installation Instructions**  
- **Clone the Repository**: 
   ```bash
   git clone https://github.com/your-username/Distracted-Driving-Flask-Yolov8.git
   cd Distracted-Driving-Flask-Yolov8
   ```

- **Set Up the Environment**: Create a virtual environment to maintain a consistent development setup:
  - For Unix/macOS:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
  - For Windows:
    ```bash
    python -m venv env
    env\Scripts\activate
    ```

- **Install Dependencies**: After activating the environment, install the required packages:
  ```bash
  pip install -r requirements.txt
  ```

- **Model Download**: Download the pre-trained YOLOv8 model (`best.pt`) and place it in the project's root directory.

**Project Structure**  
Here’s an overview of the main project files:
```
├── app.py                          # Main Flask application file
├── data.yaml                       # YOLOv8 data configuration
├── index.html                      # Web application interface (HTML)
├── style.css                       # Styling for the interface
├── requirements.txt                # Python dependencies
├── yolov8_training_and_export.ipynb # Jupyter notebook for training and exporting YOLOv8 model
├── best.pt                         # YOLOv8 model (to be added by the user)
```

**Usage**  
- **Run the Flask Application**: Start the server after confirming all dependencies are installed and the model file (`best.pt`) is in place:
   ```bash
   python app.py
   ```

- **Access the Web Interface**: Open your web browser and navigate to `http://127.0.0.1:5000` to interact with the application.

**Additional Notes**  
- The `yolov8_training_and_export.ipynb` notebook is included for users interested in training and exporting a custom YOLOv8 model.
- Customize `data.yaml` according to your specific class configurations.
- Feel free to modify the project to suit your needs!

---
