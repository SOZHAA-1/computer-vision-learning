import cv2
import matplotlib.pyplot as plt
import numpy as np


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "shifted_photo.jpg"
SHIFT_X = 100
SHIFT_Y = 50


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    height, width = image.shape[:2]
    shift_matrix = np.float32([[1, 0, SHIFT_X], [0, 1, SHIFT_Y]])
    shifted_image = cv2.warpAffine(image, shift_matrix, (width, height))

    cv2.imwrite(OUTPUT_PATH, shifted_image)

    figure, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Original")
    axes[0].axis("off")

    axes[1].imshow(cv2.cvtColor(shifted_image, cv2.COLOR_BGR2RGB))
    axes[1].set_title("Shifted Right and Down")
    axes[1].axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
