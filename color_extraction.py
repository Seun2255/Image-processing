# importing neccesary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# reading image
image = cv2.imread('images/orange.jpg')

# Converting Image to Image HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Defining lower and upper bound HSV values
lower = np.array([5, 100, 100])
upper = np.array([25, 255, 255])

# Defining mask for detecting color
mask = cv2.inRange(image_hsv, lower, upper)
mask = cv2.bitwise_not(mask)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

Titles = ["Fruit", "Mask"]
images = [image, mask]
count = 2

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i], cmap=plt.cm.gray)

plt.show()
