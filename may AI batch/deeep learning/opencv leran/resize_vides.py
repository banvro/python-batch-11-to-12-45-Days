import cv2 


def resizeingframe(frame, scale = 0.25):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)

    dimmsion = (width, height)

    resized_image = cv2.resize(frame, dimmsion, interpolation = cv2.INTER_AREA)

    return resized_image


capture = cv2.VideoCapture("3141208-uhd_3840_2160_25fps.mp4")

while True:
    isTrue, frame = capture.read()

    resized_frame = resizeingframe(frame, scale = 0.10)

    cv2.imshow("resized Video", resized_frame)

    cv2.imshow("My Video", frame)

    if cv2.waitKey(3) & 0xff == ord("q"):
        break




















# import cv2

# capture = cv2.imread("images.jpeg")

# print(capture.shape)


# # (width, height, channel)
