import cv2  # OpenCV library for image processing
import numpy as np  # NumPy for numerical operations

def block_average(image_path, block_size):
    # Load the input image in color
    img = cv2.imread(image_path)

    #Height (h), width (w), and channels (c)
    h, w, c = img.shape

    # Make a copy of the original image
    new_img = img.copy()

    # Traverse the image in non-overlapping blocks
    for i in range(0, h - block_size + 1, block_size):
        for j in range(0, w - block_size + 1, block_size):
            # Extract the current block
            block = img[i:i+block_size, j:j+block_size]

            # Ensure the block is complete
            if block.shape[0] == block_size and block.shape[1] == block_size:
                # Compute the average color of the block
                avg_color = block.mean(axis=(0, 1)).astype(np.uint8)

                # Replace the block in the new image with the average color
                new_img[i:i+block_size, j:j+block_size] = avg_color

    # Save the processed image with a filename indicating block size
    cv2.imwrite(f"outputImages/block_avg_{block_size}x{block_size}.jpg", new_img)

# Apply block averaging with block sizes 3x3, 5x5, and 7x7
for size in [3, 5, 7]:
    block_average("inputImage/frog.jpg", size)
