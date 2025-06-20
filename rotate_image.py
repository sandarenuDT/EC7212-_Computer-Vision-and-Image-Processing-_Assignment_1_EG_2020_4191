import cv2  # OpenCV library for image processing

def rotate_image(image_path):
    # Read the image in color mode
    img = cv2.imread(image_path)

    # Get the dimensions of the image (rows = height, cols = width)
    rows, cols = img.shape[:2]

    # --- Rotation by 45 degrees ---
    # Get the rotation matrix centered at the image center, rotating by 45 degrees with no scaling (scale=1)
    M_45 = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)

    # Apply the affine transformation (rotation)
    rotated_45 = cv2.warpAffine(img, M_45, (cols, rows))

    # Save the rotated image to the output folder
    cv2.imwrite("outputImages/rotated_45.jpg", rotated_45)

    # --- Rotation by 90 degrees clockwise ---
    # Use OpenCV’s built-in rotate function for exact 90-degree rotation
    rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Save the 90-degree rotated image
    cv2.imwrite("outputImages/rotated_90.jpg", rotated_90)

# Call the function with the image path
rotate_image("inputImage/frog.jpg")
