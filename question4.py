import cv2
import numpy as np

def block_average(image_path, block_size):
    # Load color image
    img = cv2.imread(image_path)
    h, w, c = img.shape
    new_img = img.copy()

    for i in range(0, h - block_size + 1, block_size):
        for j in range(0, w - block_size + 1, block_size):
            block = img[i:i+block_size, j:j+block_size]
            if block.shape[0] == block_size and block.shape[1] == block_size:
                avg_color = block.mean(axis=(0, 1)).astype(np.uint8)
                new_img[i:i+block_size, j:j+block_size] = avg_color

    cv2.imwrite(f"outputImages/block_avg_{block_size}x{block_size}.jpg", new_img)

# Run for 3×3, 5×5, and 7×7 blocks
for size in [3, 5, 7]:
    block_average("inputImage/frog.jpg", size)
