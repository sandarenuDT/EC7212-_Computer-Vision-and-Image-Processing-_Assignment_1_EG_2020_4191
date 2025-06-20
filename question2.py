import cv2

def spatial_average(image_path):
    image = cv2.imread(image_path, 0)
    for k in [3, 10, 20]:
        blurred = cv2.blur(image, (k, k))
        cv2.imwrite(f"outputImages/average_{k}x{k}.jpg", blurred)
spatial_average("inputImage/frog.jpg")