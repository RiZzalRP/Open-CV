import cv2
video=cv2.VideoCapture('/home/rizzal/Documents/git/Python/Opencv/mny.mp4')

while True:
    success,frame = video.read()
    if success==False:
        break
    video_grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    cv2.imshow("Grey Video",video_grey)
    if cv2.waitKey(30)& 0xFF==27:
        break
video.release()
cv2.destroyAllWindows()
