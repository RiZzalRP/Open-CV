import cv2
web = cv2.VideoCapture(0)

while True:
    success,frame = web.read()
    if success == False:
        break


    web_gry = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Web Camera Video",web_gry)
    if cv2.waitKey(30)&0xFF==27:
        break

web.release()
cv2.destroyAllWindows()