import cv2
img1=cv2.imread('/home/rizzal/Documents/git/Python/Opencv/tny1.jpeg')

# Add text on image

txt_img = cv2.putText(
    img1,
    org=(-5,215),
    text='iam IRON MAN',
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=1,
    color=(18,11,225),
    thickness=2
)
cv2.imshow("Text Image",txt_img)
cv2.waitKey()
cv2.destroyAllWindows()