
import cv2

cap = cv2.imread("Asana3808_Dashboard_Standard.jpg")


# (660, 710)

# opencv ---> it always use RGB color

cv2.putText(cap, "My Cat", (50, 150), 20, 3, (51, 245, 29), 10, cv2.FONT_ITALIC)

cv2.imshow("My Video", cap)


cv2.waitKey(0)