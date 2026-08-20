import cv2
import matplotlib.pyplot as plt
import numpy as np


INPUT_PATH = "portrait_neon.jpg"
OUTPUT_PATH = "preferred_color_result.jpg"
HUE_SHIFT = 5
SATURATION_SCALE = 1.0
BRIGHTNESS_SCALE = 1.0


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    adjusted_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    adjusted_hsv[:, :, 0] = (adjusted_hsv[:, :, 0] + HUE_SHIFT) % 180
    adjusted_hsv[:, :, 1] = np.clip(
        adjusted_hsv[:, :, 1].astype(float) * SATURATION_SCALE,
        0,
        255,
    ).astype(np.uint8)
    adjusted_hsv[:, :, 2] = np.clip(
        adjusted_hsv[:, :, 2].astype(float) * BRIGHTNESS_SCALE,
        0,
        255,
    ).astype(np.uint8)

    adjusted_image = cv2.cvtColor(adjusted_hsv, cv2.COLOR_HSV2BGR)
    cv2.imwrite(OUTPUT_PATH, adjusted_image)

    figure, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Original")
    axes[0].axis("off")

    axes[1].imshow(cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2RGB))
    axes[1].set_title("Preferred Color Settings")
    axes[1].axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
