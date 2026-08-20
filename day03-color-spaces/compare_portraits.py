import cv2
import matplotlib.pyplot as plt


IMAGE_FILES = ["portrait_natural.jpg", "portrait_neon.jpg"]
IMAGE_TITLES = ["Natural Light Portrait", "Neon Light Portrait"]
OUTPUT_PATH = "portrait_hsv_comparison.jpg"


def show_hsv_channels(axes, image_file, image_title):
    image = cv2.imread(image_file)

    if image is None:
        print(f"无法读取图片：{image_file}")
        return

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue, saturation, value = cv2.split(image_hsv)

    pictures = [
        (image_rgb, "Original", None),
        (hue, "Hue", "hsv"),
        (saturation, "Saturation", "gray"),
        (value, "Brightness", "gray"),
    ]

    for axis, (picture, label, color_map) in zip(axes, pictures):
        axis.imshow(picture, cmap=color_map)
        axis.set_title(f"{image_title}\n{label}")
        axis.axis("off")


def main():
    figure, axes = plt.subplots(2, 4, figsize=(16, 8))

    for axis_row, image_file, image_title in zip(axes, IMAGE_FILES, IMAGE_TITLES):
        show_hsv_channels(axis_row, image_file, image_title)

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.show()


if __name__ == "__main__":
    main()
