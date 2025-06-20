import cv2
import numpy as np

def reduce_intensity_levels(image_path, levels):
    image = cv2.imread(image_path, 0) 
    factor = 256 // levels
    reduced_image = (image // factor) * factor
    cv2.imwrite(f"outputImages/reduce_intensity{levels}.jpg", reduced_image) 

reduce_intensity_levels("inputImage/frog.jpg", 256)  
