import cv2 as cv
import numpy as np
img = np.ones((500, 500, 3), np.uint8) * 255
cv.putText(img,"S",[150,350],cv.FONT_HERSHEY_COMPLEX,15,0,15)
cv.imwrite("img.png",img)
