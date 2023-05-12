# OMR System Project

This is a Python-based Optical Mark Recognition (OMR) System. It uses Streamlit for the user interface and the Canny edge detection algorithm for image processing.

# Installation
To run the project, you'll need to install Python and the following libraries:
- OpenCV: 'pip install opencv-python'
- Streamlit: 'pip install streamlit'

# Usage
To run the OMR System, simply navigate to the project directory in your terminal and run the following command:
- streamlit run /OMR_System_Project/script/app.py

This will start a local Streamlit server, and the application will be accessible in your web browser at http://localhost:8501.

# Features
The OMR System has the following features:
- Upload an image of an OMR sheet
- Detect and extract bubbles from the image using the Canny edge detection algorithm
- Analyze the extracted bubbles to identify which options were selected by the user
- Display the results of the analysis in a user-friendly format
