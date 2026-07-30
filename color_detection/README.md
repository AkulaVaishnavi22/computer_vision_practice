# Real-Time Color Detection Using OpenCV

A beginner computer vision project that detects a selected color in real time using webcam input.

## Features

- Captures live video using a webcam
- Detects blue-colored objects in real time
- Applies Gaussian blur to reduce noise
- Converts video frames from BGR to HSV
- Generates a binary mask for the selected color
- Draws a bounding box around the detected color region

## Technologies Used

- Python
- OpenCV
- NumPy

## How It Works

1. The application captures live frames from the webcam.
2. Gaussian blur is applied to reduce noise.
3. Each frame is converted from the BGR color space to HSV.
4. A lower and upper HSV range is defined for the selected blue color.
5. A binary mask is generated using `cv2.inRange()`.
6. The detected color region is identified.
7. A bounding box is drawn around the detected object.
8. The live frame and mask are displayed.

## Project Output

![Color Detection Output](screenshots/output.png)

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_LINK