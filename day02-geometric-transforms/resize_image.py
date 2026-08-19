import cv2
import matplotlib.pyplot as plt


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "resized_photo.jpg"
SCALE = 0.5


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    resized_image = cv2.resize(
        image,
        None,
        fx=SCALE,
        fy=SCALE,
        interpolation=cv2.INTER_AREA,
    )

    cv2.imwrite(OUTPUT_PATH, resized_image)

    image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
