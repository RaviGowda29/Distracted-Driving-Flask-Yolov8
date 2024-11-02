```markdown
# Distracted Driving Detection with YOLOv8 and Flask

This project utilizes YOLOv8 for real-time object detection to identify distracted driving behaviors. The application is built using Flask and requires a pre-trained model (`best.pt`) for predictions on images and videos.

## Table of Contents

1. [Installation](#installation)
2. [Setup](#setup)
3. [Model Download](#model-download)
4. [Project Structure](#project-structure)
5. [Usage](#usage)
6. [Additional Notes](#additional-notes)

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Distracted-Driving-Flask-Yolov8.git
cd Distracted-Driving-Flask-Yolov8
```

### Set Up the Environment

To ensure a consistent development environment, it’s recommended to create a virtual environment:

#### For Unix/macOS

```bash
python3 -m venv env
source env/bin/activate
```

#### For Windows

```bash
python -m venv env
env\Scripts\activate
```

### Install the Dependencies

After activating the environment, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Model Download

Download the pre-trained YOLOv8 model (`best.pt`) and place it in the project's root directory. This model is essential for detection and classification tasks.

- **Model Path:** Place `best.pt` in the same directory as `app.py`.

## Project Structure

Here’s an overview of the main project files:

```
├── app.py                          # Main Flask application file

├── data.yaml                       # YOLOv8 data configuration

├── index.html                      # Web application interface (HTML)

├── style.css                       # Styling for the interface

├── requirements.txt                # Python dependencies

├── yolov8_training_and_export.ipynb # Jupyter notebook for training and exporting YOLOv8 model

├── best.pt                        # YOLOv8 model (to be added by the user)

```

## Usage

### Run the Flask Application

Start the Flask server after confirming that all dependencies are installed and the model file (`best.pt`) is in place:

```bash
python app.py
```

### Access the Web Interface

Open your web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to interact with the application.

## Additional Notes

- The `yolov8_training_and_export.ipynb` notebook is included for those who wish to train and export a custom YOLOv8 model.
- You can customize `data.yaml` according to your specific class configurations.

Feel free to modify the project to suit your needs!
```

You can replace `your-username` in the clone URL with your actual GitHub username.
