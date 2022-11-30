import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
fruit = cv2.imread('images/orange.jpg')


fruit = cv2.cvtColor(fruit, cv2.COLOR_BGR2RGB)

resized_image = cv2.resize(fruit, (200, 200), interpolation=cv2.INTER_CUBIC)

Titles = ["Fruit", "Resized fruit"]
images = [fruit, resized_image]
count = 2

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])

plt.show()
