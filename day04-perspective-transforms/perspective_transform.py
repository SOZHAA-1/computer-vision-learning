import cv2
import matplotlib.pyplot as plt
import numpy as np


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "perspective_photo.jpg"


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    height, width = image.shape[:2]

    source_points = np.float32(
        [[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]]
    )
    target_points = np.float32(
        [[40, 20], [width - 50, 0], [0, height - 1], [width - 20, height - 30]]
    )

    perspective_matrix = cv2.getPerspectiveTransform(source_points, target_points)
    transformed_image = cv2.warpPerspective(image, perspective_matrix, (width, height))

    cv2.imwrite(OUTPUT_PATH, transformed_image)

    figure, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Original")
    axes[0].axis("off")

    axes[1].imshow(cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB))
    axes[1].set_title("Perspective Transform")
    axes[1].axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
