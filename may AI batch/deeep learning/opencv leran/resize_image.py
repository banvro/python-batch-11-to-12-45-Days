import cv2

def resizeingframe(frame, scale = 0.25):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)

    dimmsion = (width, height)

    resized_image = cv2.resize(frame, dimmsion, interpolation = cv2.INTER_AREA)

    return resized_image


img = cv2.imread("pexels-pixabay-45201.jpg")

resize_image = resizeingframe(img)

resize_image_more = resizeingframe(img, scale = 0.10)

cv2.imshow("resiszed image more", resize_image_more)

cv2.imshow("resiszed image", resize_image)

cv2.imshow("original image", img) 

cv2.waitKey(0)
