import cv2
video =cv2.VideoCapture('/home/rizzal/Documents/git/Python/Opencv/mny1.mp4')

while True:
    success,frame=video.read()
    if success==False:
        break
    rotate_frame=cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
    grey_img = cv2.cvtColor(rotate_frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('Video Frame',grey_img)
    if cv2.waitKey(30) & 0xFF==27:
        break

video.realse()
cv2.destroyAllWindows()
