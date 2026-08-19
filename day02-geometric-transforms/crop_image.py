import cv2
import matplotlib.pyplot as plt


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "cropped_photo.jpg"
CROP_RATIO = 0.6


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    height, width = image.shape[:2]
    crop_width = int(width * CROP_RATIO)
    crop_height = int(height * CROP_RATIO)

    start_x = (width - crop_width) // 2
    start_y = (height - crop_height) // 2

    cropped_image = image[
        start_y : start_y + crop_height,
        start_x : start_x + crop_width,
    ]

    cv2.imwrite(OUTPUT_PATH, cropped_image)

    image_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
