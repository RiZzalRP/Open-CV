import cv2
img1=cv2.imread('/home/rizzal/Documents/git/Python/Opencv/tny1.jpeg')

# Drawing Rectangle in border

img_rect = cv2.rectangle(
    img1,
    pt1=(200,90),
    pt2=(130,170),
    color=(120,89,255),
    thickness=3)

cv2.imshow("Rectangle ",img_rect)
cv2.waitKey()
cv2.destroyAllWindows()



# Draw filled rectangle
img_rec = cv2.rectangle(
    img1,
    pt1=(200,69),
    pt2=(160,100),
    color=(120,245,107),
    thickness=cv2.FILLED
)

cv2.imshow("Rectangle with Filled",img_rec)
cv2.waitKey()
cv2.destroyAllWindows()