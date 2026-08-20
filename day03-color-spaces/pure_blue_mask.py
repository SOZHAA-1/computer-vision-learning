import cv2
import matplotlib.pyplot as plt
import numpy as np


INPUT_PATH = "portrait_neon.jpg"
OUTPUT_PATH = "pure_blue_mask_result.jpg"

# 更窄的蓝色范围，并排除颜色太淡或太暗的像素。
LOWER_BLUE = np.array([105, 120, 60])
UPPER_BLUE = np.array([130, 255, 255])


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    blue_mask = cv2.inRange(image_hsv, LOWER_BLUE, UPPER_BLUE)
    selected_blue = cv2.bitwise_and(image, image, mask=blue_mask)

    figure, axes = plt.subplots(1, 3, figsize=(15, 5))

    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Original")
    axes[0].axis("off")

    axes[1].imshow(blue_mask, cmap="gray")
    axes[1].set_title("Pure Blue Mask")
    axes[1].axis("off")

    axes[2].imshow(cv2.cvtColor(selected_blue, cv2.COLOR_BGR2RGB))
    axes[2].set_title("Selected Blue")
    axes[2].axis("off")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.show()


if __name__ == "__main__":
    main()
