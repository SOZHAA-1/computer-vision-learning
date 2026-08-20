import cv2
import matplotlib.pyplot as plt


INPUT_PATH = "portrait_neon.jpg"
OUTPUT_PATH = "hue_shift_comparison.jpg"
HUE_SHIFT_VALUES = [0, 15, 30, 45, 60, 90]


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    figure, axes = plt.subplots(2, 3, figsize=(12, 8))

    for axis, hue_shift in zip(axes.flat, HUE_SHIFT_VALUES):
        shifted_hsv = image_hsv.copy()
        shifted_hsv[:, :, 0] = (shifted_hsv[:, :, 0] + hue_shift) % 180

        shifted_image = cv2.cvtColor(shifted_hsv, cv2.COLOR_HSV2RGB)
        axis.imshow(shifted_image)
        axis.set_title(f"Hue Shift: {hue_shift}")
        axis.axis("off")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.show()


if __name__ == "__main__":
    main()
