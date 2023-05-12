import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the answer sheet image
img = cv2.imread('Imges/ans1.jpeg', 0)

# Apply Canny edge detection
edges_canny = cv2.Canny(img, 100, 200)

# Apply Sobel edge detection
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
edges_sobel = np.sqrt(sobelx**2 + sobely**2).astype(np.uint8)

# Apply Prewitt edge detection
prewittx = cv2.filter2D(img, -1, np.array([[-1,0,1],[-1,0,1],[-1,0,1]]))
prewitty = cv2.filter2D(img, -1, np.array([[-1,-1,-1],[0,0,0],[1,1,1]]))
edges_prewitt = cv2.add(np.abs(prewittx), np.abs(prewitty))

# Plot the original image and the edge detection results
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 2, 2)
plt.imshow(edges_canny, cmap='gray')
plt.title('Canny Edge Detection')

plt.subplot(2, 2, 3)
plt.imshow(edges_sobel, cmap='gray')
plt.title('Sobel Edge Detection')

plt.subplot(2, 2, 4)
plt.imshow(edges_prewitt, cmap='gray')
plt.title('Prewitt Edge Detection')

plt.tight_layout()
plt.show()
