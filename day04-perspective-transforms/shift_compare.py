import cv2
import matplotlib.pyplot as plt
import numpy as np


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "shift_comparison.jpg"
SHIFT_OPTIONS = [(100, 50), (-100, -50), (100, -50)]


def shift_image(image, shift_x, shift_y):
    height, width = image.shape[:2]
    shift_matrix = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
    return cv2.warpAffine(image, shift_matrix, (width, height))


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    figure, axes = plt.subplots(2, 2, figsize=(10, 8))
    pictures = [(image, "Original")]

    for shift_x, shift_y in SHIFT_OPTIONS:
        shifted = shift_image(image, shift_x, shift_y)
        pictures.append((shifted, f"Shift: x={shift_x}, y={shift_y}"))

    for axis, (picture, title) in zip(axes.flat, pictures):
        axis.imshow(cv2.cvtColor(picture, cv2.COLOR_BGR2RGB))
        axis.set_title(title)
        axis.axis("off")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.show()


if __name__ == "__main__":
    main()
