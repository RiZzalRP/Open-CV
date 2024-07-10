import cv2
img1=cv2.imread('/home/rizzal/Documents/git/Python/Opencv/tny1.jpeg')

# Drawing circle
img_cirl=cv2.circle(
    img1,
    center=(100,90),
    radius=90,
    color=(120,190,230),
    thickness=4
)

cv2.imshow("Circle ",img_cirl)
cv2.waitKey()
cv2.destroyAllWindows()

