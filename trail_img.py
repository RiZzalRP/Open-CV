import cv2
img1 = cv2.imread('/home/rizzal/Documents/git/Python/Opencv/selfe.jpeg')

img_rec = cv2.rectangle(
    img1,
    pt1=(265,177),
    pt2=(50,135),
    color=(120,120,255),
    thickness=cv2.FILLED
)

img_cir = cv2.circle(
    img_rec,
    center=(90,155),
    radius=20,
    color=(198,30,189),
    thickness=cv2.FILLED
)

img_text = cv2.putText(
    img_cir,
    org=(150,164),
    text="Smile...",
    fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
    fontScale=1,
    color=(255,220,120),
    thickness=2
)


cv2.imshow("Trail Image",img_text)
cv2.waitKey()
cv2.destroyAllWindows()