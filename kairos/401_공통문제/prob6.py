import cv2
import numpy as np

# 카메라 시작
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)  # Width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)  # Height
def nothing(x):
    pass

cv2.namedWindow('Color Detector')

# Create trackbars for color change
cv2.createTrackbar('Low H', 'Color Detector', 0, 179, nothing)
cv2.createTrackbar('Low S', 'Color Detector', 0, 255, nothing)
cv2.createTrackbar('Low V', 'Color Detector', 0, 255, nothing)
cv2.createTrackbar('High H', 'Color Detector', 179, 179, nothing)
cv2.createTrackbar('High S', 'Color Detector', 255, 255, nothing)
cv2.createTrackbar('High V', 'Color Detector', 255, 255, nothing)

while True:
    _, frame = cap.read()
    if frame is None:
        break

    # Get current positions of the trackbars
    low_h = cv2.getTrackbarPos('Low H', 'Color Detector')
    low_s = cv2.getTrackbarPos('Low S', 'Color Detector')
    low_v = cv2.getTrackbarPos('Low V', 'Color Detector')
    high_h = cv2.getTrackbarPos('High H', 'Color Detector')
    high_s = cv2.getTrackbarPos('High S', 'Color Detector')
    high_v = cv2.getTrackbarPos('High V', 'Color Detector')

    lower_color = np.array([low_h, low_s, low_v])
    upper_color = np.array([high_h, high_s, high_v])

 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)

    result = cv2.bitwise_and(frame, frame, mask=mask)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(max_contour) > 1000:
            x, y, w, h = cv2.boundingRect(max_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2.drawContours(frame, [max_contour], -1, (0, 255, 0), 3)

            M = cv2.moments(max_contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

 
                cv2.circle(frame, (cx, cy), 10, (0, 255, 0), -1)

 
    cv2.imshow('HSV', result)
    cv2.imshow('Frame', frame)


    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        save_hsv = [lower_color, upper_color]
        np.save("hsv_values.npy", save_hsv)

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()