import cv2
import matplotlib.pyplot as plt

image = cv2.imread("photo.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("gray_photo.jpg", gray_image)

plt.imshow(gray_image, cmap="gray")
plt.axis("off")
plt.show()