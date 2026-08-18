import cv2
import matplotlib.pyplot as plt


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "threshold_photo.jpg"
THRESHOLD_VALUE = 128


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, binary_image = cv2.threshold(
        gray_image,
        THRESHOLD_VALUE,
        255,
        cv2.THRESH_BINARY,
    )

    cv2.imwrite(OUTPUT_PATH, binary_image)

    plt.imshow(binary_image, cmap="gray")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
