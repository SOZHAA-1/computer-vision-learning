import cv2
import matplotlib.pyplot as plt
import numpy as np


INPUT_PATH = "portrait_neon.jpg"
OUTPUT_PATH = "blue_purple_mask_result.jpg"

# 选择蓝色到紫色的颜色范围。
LOWER_COLOR = np.array([100, 80, 50])
UPPER_COLOR = np.array([170, 255, 255])


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    color_mask = cv2.inRange(image_hsv, LOWER_COLOR, UPPER_COLOR)
    selected_color = cv2.bitwise_and(image, image, mask=color_mask)

    figure, axes = plt.subplots(1, 3, figsize=(15, 5))

    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Original")
    axes[0].axis("off")

    axes[1].imshow(color_mask, cmap="gray")
    axes[1].set_title("Blue-Purple Mask")
    axes[1].axis("off")

    axes[2].imshow(cv2.cvtColor(selected_color, cv2.COLOR_BGR2RGB))
    axes[2].set_title("Selected Colors")
    axes[2].axis("off")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.show()


if __name__ == "__main__":
    main()
