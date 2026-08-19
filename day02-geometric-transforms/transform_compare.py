import cv2
import matplotlib.pyplot as plt


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "transform_comparison.jpg"


def to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    resized_image = cv2.resize(
        image,
        None,
        fx=0.5,
        fy=0.5,
        interpolation=cv2.INTER_AREA,
    )

    height, width = image.shape[:2]
    center = (width / 2, height / 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    crop_width = int(width * 0.6)
    crop_height = int(height * 0.6)
    start_x = (width - crop_width) // 2
    start_y = (height - crop_height) // 2
    cropped_image = image[
        start_y : start_y + crop_height,
        start_x : start_x + crop_width,
    ]

    figure, axes = plt.subplots(2, 2, figsize=(10, 8))
    pictures = [
        (image, "Original"),
        (resized_image, "Resize"),
        (rotated_image, "Rotate"),
        (cropped_image, "Crop"),
    ]

    for axis, (picture, title) in zip(axes.flat, pictures):
        axis.imshow(to_rgb(picture))
        axis.set_title(title)
        axis.axis("off")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.show()


if __name__ == "__main__":
    main()
