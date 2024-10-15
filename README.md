OpenCV Operations


This repository contains various Python scripts that demonstrate the use of OpenCV for different image processing operations. Each file in the repository focuses on a specific operation such as blurring, contour detection, circle dropping, edge detection, and face detection.

Requirements

Before running any of the scripts, make sure to install the following dependencies: pip install opencv-python
You may also need to install additional packages depending on the functionality of the specific script. For example, numpy may be required for certain operations.
pip install numpy

Files and Functionality
Bluroperation.py
This script demonstrates how to apply different blurring techniques to an image, such as:

Gaussian blur
Median blur
Bilateral filter
contour_detection.py
This script detects contours in an image and highlights them using the OpenCV contour detection functions. It helps in identifying object boundaries and shapes in an image.

drop_circle.py
This script drops circles on a canvas or an image at random positions or user-defined positions. It demonstrates how to draw geometric shapes using OpenCV.

edge.py
This script applies edge detection to an image using the Canny edge detection algorithm. It outlines the edges within an image, helping in image segmentation and object detection.

face.py
This script performs face detection using OpenCV's Haar cascades. It identifies and marks faces in an input image or video stream.
