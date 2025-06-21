import cv2  # OpenCV library for image processing
import numpy as np  # NumPy for numerical operations on arrays

def reduce_intensity_levels(image_path, levels):
    # Read the image in grayscale mode (0 means grayscale)
    image = cv2.imread(image_path, 0)
    
    # Calculate the quantization factor for reducing intensity levels
    factor = 256 // levels
    
    # Apply intensity reduction by quantizing the pixel values
    # This maps each pixel to the nearest lower multiple of 'factor'
    reduced_image = (image // factor) * factor
    
    # Save the resulting image in the 'outputImages' folder
    cv2.imwrite(f"outputImages/reduce_intensity{levels}.jpg", reduced_image)

# (2,4,8,16,32,64,128,256 levels)
reduce_intensity_levels("inputImage/dog.jpg", 64)
