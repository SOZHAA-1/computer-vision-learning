import cv2
import matplotlib.pyplot as plt


INPUT_PATH = "photo.jpg"
OUTPUT_PATH = "flip_comparison.jpg"


def to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def main():
    image = cv2.imread(INPUT_PATH)

    if image is None:
        print(f"无法读取图片：{INPUT_PATH}")
        return

    horizontal_flip = cv2.flip(image, 1)
    vertical_flip = cv2.flip(image, 0)

    figure, axes = plt.subplots(1, 3, figsize=(15, 5))
    pictures = [
        (image, "Original"),
        (horizontal_flip, "Horizontal Flip"),
        (vertical_flip, "Vertical Flip"),
    ]

    for axis, (picture, title) in zip(axes, pictures):
        axis.imshow(to_rgb(picture))
        axis.set_title(title)
        axis.axis("off")

    plt.tight_layout()
    plt.savefig(OUTPUT_PATH)
    plt.show()


if __name__ == "__main__":
    main()
