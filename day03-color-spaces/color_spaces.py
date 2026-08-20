import cv2
import matplotlib.pyplot as plt


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "hsv_channels.jpg"


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hue, saturation, value = cv2.split(image_hsv)

    figure, axes = plt.subplots(2, 2, figsize=(10, 8))

    axes[0, 0].imshow(image_rgb)
    axes[0, 0].set_title("Original Image")
    axes[0, 0].axis("off")

    axes[0, 1].imshow(hue, cmap="hsv")
    axes[0, 1].set_title("Hue: Color Type")
    axes[0, 1].axis("off")

    axes[1, 0].imshow(saturation, cmap="gray")
    axes[1, 0].set_title("Saturation: Color Strength")
    axes[1, 0].axis("off")

    axes[1, 1].imshow(value, cmap="gray")
    axes[1, 1].set_title("Value: Brightness")
    axes[1, 1].axis("off")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.show()


if __name__ == "__main__":
    main()
