import cv2
import matplotlib.pyplot as plt
import numpy as np


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "perspective_comparison.jpg"


def transform_image(image, target_points):
    height, width = image.shape[:2]
    source_points = np.float32(
        [[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]]
    )
    perspective_matrix = cv2.getPerspectiveTransform(source_points, target_points)
    return cv2.warpPerspective(image, perspective_matrix, (width, height))


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    height, width = image.shape[:2]

    mild_points = np.float32(
        [[40, 20], [width - 50, 0], [0, height - 1], [width - 20, height - 30]]
    )
    strong_points = np.float32(
        [[120, 70], [width - 150, 0], [20, height - 1], [width - 50, height - 100]]
    )

    mild_image = transform_image(image, mild_points)
    strong_image = transform_image(image, strong_points)

    figure, axes = plt.subplots(1, 3, figsize=(15, 5))
    pictures = [
        (image, "Original"),
        (mild_image, "Mild Perspective"),
        (strong_image, "Strong Perspective"),
    ]

    for axis, (picture, title) in zip(axes, pictures):
        axis.imshow(cv2.cvtColor(picture, cv2.COLOR_BGR2RGB))
        axis.set_title(title)
        axis.axis("off")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.show()


if __name__ == "__main__":
    main()
