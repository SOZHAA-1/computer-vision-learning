import cv2
import matplotlib.pyplot as plt


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "edge_photo.jpg"


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edge_image = cv2.Canny(gray_image, 100, 200)

    cv2.imwrite(OUTPUT_PATH, edge_image)

    plt.imshow(edge_image, cmap="gray")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
