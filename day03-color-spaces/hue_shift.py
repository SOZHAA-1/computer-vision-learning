import cv2
import matplotlib.pyplot as plt


INPUT_PATH = "portrait_neon.jpg"
OUTPUT_PATH = "hue_shifted_portrait.jpg"
HUE_SHIFT = 5


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image_hsv[:, :, 0] = (image_hsv[:, :, 0] + HUE_SHIFT) % 180

    shifted_image = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)
    cv2.imwrite(OUTPUT_PATH, shifted_image)

    figure, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Original")
    axes[0].axis("off")

    axes[1].imshow(cv2.cvtColor(shifted_image, cv2.COLOR_BGR2RGB))
    axes[1].set_title("Hue Shifted")
    axes[1].axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
