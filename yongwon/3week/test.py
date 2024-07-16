import cv2
import numpy as np


cap = cv2.VideoCapture(0)

cap.set(600,100)

def nothing(x):
    pass

cv2.namedWindow('Color Detector', cv2.WINDOW_NORMAL)

# Trackbar를 생성하여 'Lower'와 'Upper' 범위 설정
# 예시코드 주어질 예정
cv2.createTrackbar('low_h', 'Color Detector',0,179,nothing)
# 숙지 필요
cv2.createTrackbar('high_h', 'Color Detector',178,179,nothing)
cv2.createTrackbar('low_s', 'Color Detector',0,250,nothing)
cv2.createTrackbar('high_s', 'Color Detector',254,255,nothing)
cv2.createTrackbar('low_v', 'Color Detector',0,255,nothing)
cv2.createTrackbar('high_v', 'Color Detector',254,255,nothing)


while True:
    # 복사본 이미지 생성
    _, frame = cap.read()

    # 트랙바에서 현재 값 얻기
    # 예시코드 주어질 예정
    low_h = cv2.getTrackbarPos('low_h', 'Color Detector')
    low_s = cv2.getTrackbarPos('low_s', 'Color Detector')
    low_v = cv2.getTrackbarPos('low_v', 'Color Detector')
    high_h = cv2.getTrackbarPos('high_h', 'Color Detector')
    high_s = cv2.getTrackbarPos('high_s', 'Color Detector')
    high_v = cv2.getTrackbarPos('high_v', 'Color Detector')

    # 숙지 필요
    ##HSV 만들기
    
    # getTrackbarPos에서 얻은 값 array로 저장
    # 예시코드 주어질 예정
    low = np.array([low_h, low_s, low_v])
    high = np.array([high_h, high_s, high_v])

    # upper_color

    # lower/upper 임계값을 이용하여 마스크 생성
    # 예시코드 주어질 예정
    mask = cv2.inRange(img_hsv, low, high)

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
             # 윤곽선의 무게 중심 계산
            M = cv2.moments(max_contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # 추적된 위치에 원 그리기
                # rect_size = 50  # 사각형의 크기 설정
                # top_left = (cx - rect_size // 2, cy - rect_size // 2)
                # bottom_right = (cx + rect_size // 2, cy + rect_size // 2)
                # cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), -1)

    # 원본 이미지에 마스크 적용
    # 숙지 필요
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # 결과 표시
    # cv2.imshow('Original Image', frame)
    # cv2.imshow('Color Detector', result)

    # 키 입력 대기 (ESC를 누르면 종료)
    # 숙지 필요
    # hsv = [low, high]

    if cv2.waitKey(10) & 0xff == ord('q'):
        break
    elif cv2.waitKey(10) & 0xff == ord('s'):
        np.save("low_high.npy", hsv)

# 숙지 필요
cap.release()
cv2.destroyAllWindows()
