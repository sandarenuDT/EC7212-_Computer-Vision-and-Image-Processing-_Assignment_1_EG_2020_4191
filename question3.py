import cv2

def rotate_image(image_path):
    img = cv2.imread(image_path)
    rows, cols = img.shape[:2]

    # Rotate by 45 degrees
    M_45 = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
    rotated_45 = cv2.warpAffine(img, M_45, (cols, rows))
    cv2.imwrite("outputImages/rotated_45.jpg", rotated_45)

    # Rotate by 90 degrees
    rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite("outputImages/rotated_90.jpg", rotated_90)

rotate_image("inputImage/frog.jpg")
