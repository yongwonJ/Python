import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(600,100)

while True:
    # 복사본 이미지 생성
    _, frame = cap.read()
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # upper_color
    result =np.load("Color Detector.npy")
    # lower/upper 임계값을 이용하여 마스크 생성
    mask = cv2.inRange(img_hsv, result[0], result[1])

    # 노이즈 제거를 위한 모폴로지 연산 적용
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

     # 윤곽선 검출
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_contour = max(contours, key=cv2.contourArea)
        if cv2.contourArea(max_contour) > 100:
            cv2.drawContours(frame, [max_contour], -1, (0, 255,0), 2)
            #모멘츠를 추가 -> 에어리어의 중심을 잡는거?
            M = cv2.moments(max_contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # 추적된 위치에 원 그리기
                cv2.circle(frame, (cx, cy), 20, (0, 255, 0), -1)

    # 원본 이미지에 마스크 적용
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # 결과 표시
    cv2.imshow('Original Image', frame)
    cv2.imshow('Color Detector', result)

    # 키 입력 대기 (ESC를 누르면 종료)

   
    if cv2.waitKey(10) & 0xff== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()