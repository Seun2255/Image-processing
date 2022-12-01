# importing neccesary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

# reading image
image = cv2.imread('images/orange.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# generation of histogram
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
normalized_hist = cv2.calcHist([image], [0], None, [256], [0, 256])

normalized_hist /= hist.sum()

# displaying result
Titles = ["grayscale image", "image histogram", 'normalized histogram']
images = [image, hist, normalized_hist]
count = 3

for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i], cmap=plt.cm.gray)

plt.show()
