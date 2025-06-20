import cv2  # OpenCV library for image processing

def spatial_average(image_path):
    # Read the image in grayscale mode
    image = cv2.imread(image_path, 0)

    # Apply averaging filter with different kernel sizes
    for k in [3, 10, 20]:
        # Apply spatial averaging filter
        blurred = cv2.blur(image, (k, k))  

        # Save the blurred image
        cv2.imwrite(f"outputImages/average_{k}x{k}.jpg", blurred)


spatial_average("inputImage/frog.jpg")
