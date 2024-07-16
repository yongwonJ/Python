import cv2

cap = cv2.VideoCapture(0) 
_, background = cap.read()
back = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)

while True:
    _, frame =cap.read()   
   
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     
    diff = cv2.absdiff(gray_frame, back )
    # 차이가 30이상 255(흰색), 30보다 작으면 0(검정색)
    _, thresh_binary = cv2.threshold(diff, 100, 255, cv2.THRESH_BINARY)
    cnt, _, stats, center = cv2.connectedComponentsWithStats(diff)

    # for stat in stats:
    #     x, y ,w, h, s = stat
    #     if s>500:
    #         print(s)
    #     cv2.rectangle(frame,(x,y),(x+w, x+h), (0,0.255),3)
    for i in range(1, cnt-1) :
        x, y ,w, h, s = stats
        if s>500:
            print(s)
        cv2.rectangle(frame,(x,y),(x+w, x+h), (0,0.255),3)


    cv2.imshow("Video", diff) 
    cv2.imshow("s", frame) 
    
    back = gray_frame 
       
 
    if cv2.waitKey(10) & 0xff ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
