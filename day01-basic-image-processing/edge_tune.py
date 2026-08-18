import cv2
import matplotlib.pyplot as plt


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "tuned_edge_photo.jpg"

# 只需要修改这两个数字，就能改变边缘检测效果。
LOW_THRESHOLD = 80
HIGH_THRESHOLD = 160


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edge_image = cv2.Canny(gray_image, LOW_THRESHOLD, HIGH_THRESHOLD)

    cv2.imwrite(OUTPUT_PATH, edge_image)

    plt.imshow(edge_image, cmap="gray")
    plt.title(f"Canny: {LOW_THRESHOLD}, {HIGH_THRESHOLD}")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
