import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
fruit = cv2.imread('images/orange.jpg')
fruit_rgb = cv2.cvtColor(fruit, cv2.COLOR_BGR2RGB)

grayscaled_fruit = cv2.cvtColor(fruit, cv2.COLOR_BGR2GRAY)

Titles = ["colored image of Fruit", "grayscale image of fruit"]
images = [fruit_rgb, grayscaled_fruit]
count = 2

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i], cmap=plt.cm.gray)

plt.show()
