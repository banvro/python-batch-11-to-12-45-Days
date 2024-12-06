import cv2
import numpy as np

img = np.zeros((600, 600, 3), dtype = "uint8")

cv2.putText(img, "Hellow Word", (100, 100), 1, 3, (125, 250, 80), 2)
            # image, text, pixcel values, font_style, font_size, color, thikness
         
cv2.imshow("Blank Image", img)

cv2.waitKey(0)




# rgb = 80, 250, 125

# BGR = 125, 250, 80