import cv2
import numpy as np
def block_average(image_path, block_size):
    img = cv2.imread(image_path, 0)
    h, w = img.shape
    new_img = img.copy()

    for i in range(0, h - block_size + 1, block_size):
        for j in range(0, w - block_size + 1, block_size):
            block = img[i:i+block_size, j:j+block_size]
            avg = np.mean(block, dtype=np.uint8)
            new_img[i:i+block_size, j:j+block_size] = avg

    cv2.imwrite(f"outputImages/block_avg_{block_size}x{block_size}.jpg", new_img)

for size in [3, 5, 7]:
    block_average("inputImage/frog.jpg", size)
