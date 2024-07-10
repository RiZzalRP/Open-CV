import cv2
img1=cv2.imread('/home/rizzal/Documents/git/Python/Opencv/tny1.jpeg')
img2=cv2.imread('/home/rizzal/Documents/git/Python/Opencv/tny2.jpeg')
img3=cv2.imread('/home/rizzal/Documents/git/Python/Opencv/s1.jpeg')
img4=cv2.imread('/home/rizzal/Documents/git/Python/Opencv/lk.jpeg')
img5=cv2.imread('/home/rizzal/Documents/git/Python/Opencv/avngers1.jpeg')

imgs=[img1,img2,img3,img4,img5]
for img in imgs:
    cv2.imshow("Image",img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows() 