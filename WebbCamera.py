import cv2
# video reader
video=cv2.VideoCapture('/home/rizzal/Documents/git/Python/Opencv/mny.mp4')
# webcamera index= 0,1,2,-1,-2 
video_web=cv2.VideoCapture(-1)  #it will run the web camera


# frames(sep frame ) and back to back control
while True:
    success,frame=video.read()
    if success==False:
        break

    print(success)



    cv2.imshow("video reader",frame)
    if cv2.waitKey(30) & 0xFF==27:
        break

# stop
video.release()
cv2.destroyAllWindows()