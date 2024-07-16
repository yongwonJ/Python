import cv2
cap = cv2.VideoCapture(0)
_, background = cap.read()
back = cv2.cvtColor(background, cv2.COLOR_RGB2GRAY)

while True:
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # absdiff는 차 영상에 절대값
    diff = cv2.absdiff(gray_frame, back)
    # 차이가 30이상 255(흰색), 30보다 작으면 0(검정색)
    _, diff = cv2.threshold(diff, 127, 255, cv2.THRESH_BINARY)

     # 레이브링을 이용하여 바운딩 박스 표시
    cnt, _, stats, center = cv2.connectedComponentsWithStats(diff)
    # cnt: 움직이는것이 몇개나 있나
    # stats: 움직이는 점과 면적의 좌표값을 넘겨준다.
    # center: 면적의 중앙점을 알려준다.
    #retval, labels, stats, centroids = cv2.connectedComponentsWithStats(src, connectivity=8, ltype=cv2.CV_32S)
    print(cnt)
    for stat in stats:
        x, y, w, h, s = stat
        if s > 300:
            cv2.rectangle(frame, (x,y),(x+w, y+h),(0,0,255),3)

    cv2.imshow("DIFF",diff)
    cv2.imshow("Video",frame)
    back = gray_frame.copy()

    # 각 임계값 유형에 대해 임계값 처리
    # 127보다 커지면 255 흰색으로 변한다.
    # _, thresh_binary = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)
    # print(thresh_binary)
    # _, thresh_binary_inv = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY_INV)
    # _, thresh_trunc = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_TRUNC)
    # _, thresh_tozero = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_TOZERO)
    # _, thresh_tozero_inv = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_TOZERO_INV)
    # cv2.imshow("Video_bi",thresh_binary)
    # cv2.imshow("Video_bi_inv",thresh_binary_inv)
    # cv2.imshow("Video_tr",thresh_trunc)
    # cv2.imshow("Video_toz",thresh_tozero)
    # cv2.imshow("Video_toz_inv",thresh_tozero_inv)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()