import cv2
import matplotlib.pyplot as plt


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "edge_comparison.jpg"
THRESHOLD_PAIRS = [(50, 150), (100, 200), (150, 250)]


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    figure, axes = plt.subplots(1, 3, figsize=(15, 5))

    for axis, (low_threshold, high_threshold) in zip(axes, THRESHOLD_PAIRS):
        edge_image = cv2.Canny(gray_image, low_threshold, high_threshold)

        axis.imshow(edge_image, cmap="gray")
        axis.set_title(f"Canny: {low_threshold}, {high_threshold}")
        axis.axis("off")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.show()


if __name__ == "__main__":
    main()
