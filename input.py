import cv2 as cv
import numpy as np
x= int(input("x:"))
x1=int(input("y:"))
img = np.ones((x, x1, 3), np.uint8) * 255

cv.imwrite("img.png",img)
