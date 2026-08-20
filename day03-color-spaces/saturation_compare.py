import cv2
import matplotlib.pyplot as plt
import numpy as np


INPUT_PATH = "portrait_neon.jpg"
OUTPUT_PATH = "saturation_comparison.jpg"
SATURATION_SCALES = [0.4, 0.7, 1.0, 1.3, 1.6, 2.0]


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    figure, axes = plt.subplots(2, 3, figsize=(12, 8))

    for axis, scale in zip(axes.flat, SATURATION_SCALES):
        adjusted_hsv = image_hsv.copy()
        adjusted_hsv[:, :, 1] = np.clip(
            adjusted_hsv[:, :, 1].astype(float) * scale,
            0,
            255,
        ).astype(np.uint8)

        adjusted_image = cv2.cvtColor(adjusted_hsv, cv2.COLOR_HSV2RGB)
        axis.imshow(adjusted_image)
        axis.set_title(f"Saturation: {scale}")
        axis.axis("off")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.show()


if __name__ == "__main__":
    main()
