import cv2
import matplotlib.pyplot as plt
import numpy as np


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "corrected_photo.jpg"


def main():
    image = cv2.imread(INPUT_PATH)
    if image is None:
        raise FileNotFoundError(f"找不到图片：{INPUT_PATH}")

    height, width = image.shape[:2]

    # 原图的四个角。
    original_corners = np.float32(
        [[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]]
    )

    # 模拟拍摄时产生的轻微倾斜。
    tilted_corners = np.float32(
        [[40, 20], [width - 50, 0], [0, height - 1], [width - 20, height - 30]]
    )

    tilt_matrix = cv2.getPerspectiveTransform(original_corners, tilted_corners)
    tilted_image = cv2.warpPerspective(image, tilt_matrix, (width, height))

    # 把倾斜后的四个角映射回原图四角，完成“校正”。
    correction_matrix = cv2.getPerspectiveTransform(tilted_corners, original_corners)
    corrected_image = cv2.warpPerspective(tilted_image, correction_matrix, (width, height))

    cv2.imwrite(OUTPUT_PATH, corrected_image)

    images = [image, tilted_image, corrected_image]
    titles = ["Original", "Tilted", "Corrected"]

    plt.figure(figsize=(15, 5))
    for index, (picture, title) in enumerate(zip(images, titles), start=1):
        plt.subplot(1, 3, index)
        plt.imshow(cv2.cvtColor(picture, cv2.COLOR_BGR2RGB))
        plt.title(title)
        plt.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
