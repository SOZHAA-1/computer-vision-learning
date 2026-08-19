import cv2
import matplotlib.pyplot as plt


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "rotated_photo.jpg"
ANGLE = 45


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    height, width = image.shape[:2]
    center = (width / 2, height / 2)

    rotation_matrix = cv2.getRotationMatrix2D(center, ANGLE, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    cv2.imwrite(OUTPUT_PATH, rotated_image)

    image_rgb = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
