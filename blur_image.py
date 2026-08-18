import cv2
import matplotlib.pyplot as plt


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "blurred_photo.jpg"


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imwrite(OUTPUT_PATH, blurred_image)

    image_rgb = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
