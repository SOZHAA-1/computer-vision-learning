import cv2
import matplotlib.pyplot as plt


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "threshold_comparison.jpg"
THRESHOLD_VALUES = [60, 128, 200]


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    figure, axes = plt.subplots(1, 3, figsize=(15, 5))

    for axis, threshold_value in zip(axes, THRESHOLD_VALUES):
        _, binary_image = cv2.threshold(
            gray_image,
            threshold_value,
            255,
            cv2.THRESH_BINARY,
        )

        axis.imshow(binary_image, cmap="gray")
        axis.set_title(f"Threshold: {threshold_value}")
        axis.axis("off")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.show()


if __name__ == "__main__":
    main()
