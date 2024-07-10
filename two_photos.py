import cv2
img1=cv2.imread('/home/rizzal/Documents/git/Python/Opencv/tny1.jpeg')
img2=cv2.imread('/home/rizzal/Documents/git/Python/Opencv/tny2.jpeg')


print(img1)


cv2.imshow("IMGE 1",img1)
cv2.waitKey(2000)
cv2.destroyAllWindows()
cv2.imshow("IMGE 2",img2)
cv2.waitKey(2000)
cv2.destroyAllWindows()