import cv2

cap = cv2.VideoCapture(0)
#미리 프레임을 하나 잡고 이후에 달라지는 점을 찾아야한다.
_, background = cap.read()
back = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)

while True:
    _, frame = cap.read() #계속 바뀌는 값이라 기준이 되질 않음
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 검정 0, 흰색 255. 127을 기준으로 그 아래는 0 그 위는 1
    _, thresh_binary = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)
    diff = cv2.absdiff(gray_frame, back)
    cnt, _, stats, center = cv2.connectedComponentsWithStats(diff)
    #( 몇개가 달라지는지 확인?, , ,에어리어의 중앙값)
    for stat in stats:
        x, y ,w, h, s = stat
        if s>200:
            print(s)

    print(cnt)
    # _, thresh_binary_inv = cv2.threshold(gray_frame1, 80, 255, cv2.THRESH_BINARY_INV)
    # print(thresh_binary_inv)

    # absdiff는 차 영상에 절대값
     #frame BGR값이라 안됨. 

    # 차이가 30이상 255(흰색), 30보다 작으면 0(검정색)
    _, diff = cv2.threshold(diff, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow("binary",diff)
    # cv2.imshow("INV",thresh_binary_inv)

    back = gray_frame #프레임마다 이전 값을 저장해서 비교

    if cv2.waitKey(10) & 0xff == ord('q'):
        break   
cap.release()
cv2.destroyAllWindows()